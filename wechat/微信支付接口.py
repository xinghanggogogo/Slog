# 微信快速唤起支付
# http://pay.ktvsky.com/wx
# post
class PayHandler(BaseHandler):

    @gen.coroutine
    def get_pay_getorder(self, data):
        order_id = generate_order_id(data)
        try:
            try:
                total_fee=int(float(self.get_argument('fee'))*100)
            except:
                total_fee=int(data['paraTotalFee'])
            ktv_id=self.get_argument('ktvid')
            ktv = yield ctrl.api.get_ktv_ctl(ktv_id)
            assert(ktv)
        except:
            raise utils.APIError(errcode=10001, errmsg='支付参数不合法')
        ctrl.api.add_wxorder(
            ktv_id=ktv_id,
            erp_id=self.get_argument('erpid', ''),
            openid=data.get('paraOpenId', ''),
            erp_date=self.get_argument('date', '').replace('/', '-'),
            remark=self.get_argument('mark', ''),
            other=self.get_argument('other', ''),
            total_fee=total_fee,
            rate_fee=utils.calc_rate(total_fee, ktv, WXCONF),
            rt_rate_fee=utils.calc_rt_rate(total_fee, ktv, WXCONF),
            order_id=order_id
        )
        return dict(order=order_id, type=2, coupon_fee=0,coupon_detail='')

	@gen.coroutine
    def post_pay(self, data):
        order_id = data['order_id']
        action=data['action'].lower()
        order = get_order(order_id)
        if (not order or order['state'] != OrderState['CREATED'] or order['total_fee'] != int(data['paraTotalFee']) or action not in ('sweepcode', 'micropay', 'gzh')):
            raise utils.APIError(errcode=10001, errmsg='订单id错误或者已下单或者金额错误')
        tp = self.get_argument('tp', '')
        new_order = dict(
            order_id=order_id,
            action=DB_ACTION[action],
            body=data['paraBody'],
            dogname=data['dogname'],
            ktv_id=data['ktv_id'],
            coupon_send_id=data['coupon_send_id'],
            coupon_value=data['coupon_value'],
            c_openid=data['c_openid'],
            c_staffname=data['c_staffname'],
            tp=utils.get_order_tp_number(tp)
        )
        res = yield getattr(self, action)(data)
        if ctrl.api.get_paymax_is_enable_ctl():
            if res['lkl_order_id']:
                new_order.update(dict(lkl_order_id=res['lkl_order_id']))
        if res['return_code'] == 'SUCCESS' and res['result_code'] == 'SUCCESS':
            new_order.update(dict(wx_pay_id=res['transaction_id'], state=OrderState['PAYED']) if 'transaction_id' in res else dict(state=OrderState['UNPAY']))
        ctrl.api.update_wxorder(**new_order)
        return res

	@gen.coroutine
	def post_fastpay(self, data):
		order = yield self.get_pay_getorder(data)
		data['order_id'] = order['order']
		wx_order = yield self.post_pay(data)
		wx_order.update(order)
	return wx_order

	@gen.coroutine
    def route_api(self, method='post'):
        try:
            func = method.lower()+'_'+self.get_argument('op', '')
            print('func ==> %s'%func)
            data = self.check_args()
            func = getattr(self, func)
        except Exception as e:
            logging.error(e)
            raise utils.APIError(errcode=10001, errmsg='不存在的接口')
		#调用function处理data
        res = yield func(data)
        [res.pop(o) for o in ('appid', 'mch_id', 'sub_appid', 'sub_mch_id') if o in res]
        self.send_json(res)

	@gen.coroutine
    def post(self):
        yield self.route_api()
        return

    @gen.coroutine
    def get(self):
        yield self.route_api(method='get')
        return
