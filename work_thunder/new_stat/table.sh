class PosOrder(Base):
    __tablename__ = 'pos_order'

    order_id = Column(INTEGER(11), primary_key=True)
    ktv_id = NotNullColumn(INTEGER(11)) # 歌厅ID
    amount = NotNullColumn(INTEGER(11)) # 金额
    term_id = NotNullColumn(VARCHAR(32)) # POS终端号 device_info
    merchant_id = NotNullColumn(VARCHAR(32)) # 平台商户号 mch_id
    pay_type = NotNullColumn(TINYINT(1)) # 0:借记卡 1:微信 2:支付宝 3:贷记卡
    term_serno = NotNullColumn(VARCHAR(32)) # 终端流水号
    order_no = NotNullColumn(VARCHAR(32)) # 订单编号 参考号
    rate_fee = NotNullColumn(INTEGER(11)) # 雷石手续费
    rt_rate_fee = NotNullColumn(INTEGER(11), default=0) # 返还手续费
    state = NotNullColumn(TINYINT(1)) # 支付,退款(成功、失败)
    card_type = NotNullColumn(TINYINT(1)) # 卡类型
    card_no = NotNullColumn(VARCHAR(32)) # 交易卡号
    finish_time = NotNullColumn(DATETIME, default=func.now())# 支付完成时间 time_end
    orderid_scan = NotNullColumn(VARCHAR(32)) # 扫码订单号 (微信,支付宝扫码支付订单号)
    batchbillno = NotNullColumn(VARCHAR(32)) # 批次号
    systraceno = NotNullColumn(VARCHAR(32)) # 凭证号
    bank_type = NotNullColumn(VARCHAR(16))
    err_code = NotNullColumn(VARCHAR(32)) # 错误代码
    pos_rate_fee = NotNullColumn(INTEGER(11)) # pos手续费

CREATE TABLE `archive_order` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `order_id` varchar(32) NOT NULL DEFAULT '',
      `erp_id` varchar(128) NOT NULL DEFAULT '' COMMENT 'erp端id',
      `ktv_id` int(11) NOT NULL DEFAULT '0',
      `total_fee` int(11) NOT NULL DEFAULT '0',
      `ch_rate_fee` int(11) NOT NULL DEFAULT '0' COMMENT '渠道商收取的手续费',
      `ls_rate_fee` int(11) NOT NULL DEFAULT '0' COMMENT '雷石收取的手续费',
      `channel` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0:微信, 1:支付宝, 2:pos',
      `tp` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0:普通, 1:电影, 2:红包, 7:bar',
      `mch_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0:商户, 1:代理商,',
      `state` tinyint(1) NOT NULL DEFAULT '0' COMMENT '已支付, 已退款',
      `finish_time` datetime DEFAULT NULL COMMENT '支付完成时间',
      `body` varchar(128) NOT NULL DEFAULT '' COMMENT '商品详情',
      `income_time` datetime DEFAULT NULL,
      `income_id` int(11) NOT NULL DEFAULT '0' COMMENT 'mch_income id',
      `term_id` varchar(32) NOT NULL DEFAULT '' COMMENT '终端号',
      `card_no` varchar(32) NOT NULL DEFAULT '' COMMENT '卡号',
      `pos_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'pos交易类型 0:借记卡 1:微信 2:支付宝 3:贷记卡',
      `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
      `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
      PRIMARY KEY (`id`),
      KEY `ktv_id` (`ktv_id`,`channel`,`tp`,`finish_time`,`state`),
      KEY `order_id` (`order_id`),
      KEY `income_id` (`income_id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1144318 DEFAULT CHARSET=utf8 |
