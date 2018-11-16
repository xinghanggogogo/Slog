1.下单接口:
/bar/order        POST接口
参数：
{
    sp_id,        服务商id
    store_id,     门店id
    mac_id,       机器id
    tp,           支付类型 （0 coin， 1 wx,  2 ali,  3 free, 4会员）
    pay_coin,     支付金币部分，为支持混合支付
    pay_fee,      线上支付部分 单位分
    info,         商品描述信息（如“XX店购买了5首”或者“XX店购买了30分钟”）
    pay_order_id, 线下订单号 仅 投币 和 免费类型 使用 （最好小于32个字符）
    create_time,  订单时间 如： 2016-12-22 15:27:22
}
返回{
    pay_url,      支付二维码对应的url，
    order_id,     订单id，查单和关单需要
}
