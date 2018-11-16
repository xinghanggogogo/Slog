
class DisIndexHandler(BaseHandler):

    # 分销首页
    @check_openid
    async def get(self):
        try:
            ktv_id = int(self.get_argument('ktv_id'))
            s_openid = self.get_argument('s_openid')
        except Exception as e:
            logging.error(e)
            raise utils.APIError(errcode=10001)

        coupon_card_info = await ctrl.custom.get_ktv_coupon_info(ktv_id)
        coupon_create_his = await ctrl.custom.get_ktv_coupon_info()
        earn_sum_rank = ctrl.custom.get_earn_sum_rank()
        config = await utils.async_common_api('/wx/share/config', dict(url=self.request.full_url()))

        self.render('dis_index.tpl',
                    coupon_card_info=coupon_card_info,
                    coupon_create_his = coupon_create_his,
                    earn_sum_rank=earn_sum_rank,
                    config=config,
                    s_openid=s_openid,
                    ktv_id=ktv_id
                    )


class DisInfoHandler(BaseHandler):

    async def get(self):
        try:
            openid = self.get_cookie('agent_openid')
        except Exception as e:
            logging.error(e)
            return self.render('custom/error.tpl')

        user_info = ctrl.custom.get_dis_user(openid)

        config = await utils.async_common_api('/wx/share/config', dict(url=self.request.full_url()))

        self.render('dis_info.tpl',
                    flag=user_info['flag'],
                    config=config
                    )


class DisOrderHandler(BaseHandler):

    # 购买会员卡按钮,跳转到公共支付页面
    def post(self):
        try:
            openid = self.get_secure_cookie('agent_openid')
            s_openid = self.get_argument('openid', '')
            phone_num = int(self.get_argument('phone_num'))
            ktv_id = int(self.get_argument('ktv_id'))
            total_fee = int(self.get_argument('total_fee'))
            card_type = int(self.get_argument('card_type'))
        except Exception as e:
            logging.error(e)
            raise utils.APIError(errcode=10001)

        data = dict(openid=openid, s_openid=s_openid, phone_num=phone_num, ktv_id=ktv_id, total_fee=total_fee, card_type=card_type)
        info = '会员卡分销'
        order_id = 'SO' + str(phone_num) + 'D' + str(ktv_id)+ 'T' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        ctrl.custom.update_dis_order(order_id, data)
        self.send_json(dict(total_fee=total_fee, order_id=order_id, ktv_id=ktv_id, info=info, s_openid=s_openid))

    # 公共支付页面支付成功跳转
    async def get(self):
        try:
            order_id = self.get_argument('order_id')
            s_openid = self.get_argument('s_openid', '')
            total_fee = int(self.get_argument('total_fee'))
        except Exception as e:
            logging.error(e)
            return self.render('custom/error.tpl')

        try:
            res = res = await self.pay_query(order_id)
            if res['is_pay']:
                data = dict(payed=1)
                ctrl.custom.update_dis_order(order_id, data)
                ctrl.custom.update_dis_user_earn_sum(s_openid, total_fee/10)
                if not s_openid:
                    # 发红包
                    pass
                order_info = ctrl.custom.get_dis_order(order_id)
                # 发短信
                self.send_json(dict(payed='success'))
            else:
                self.send_json(dict(payed='failed'))
        except Exception as e:
            logging.info(e)


    async def pay_query(self, order_id, loop=1):
        logging.info('query dis_order loop %s'%loop)
        try:
            http_client = utils.get_async_client()
            request = utils.http_request(COMMON_ORDER_URL.format(order_id=order_id))
            res = await utils.fetch(http_client, request)
            res = json.loads(res.body.decode())
            logging.info('query order result: %s'%res)
            return res
        except Exception as e:
            logging.error(e)
            if loop>0:
                IOLoop.current().add_timeout(time.time()+60, self._pay_query, order_id, loop-1)
            raise utils.APIError(errcode=19004, errmsg='查单失败')
