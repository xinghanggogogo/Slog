#数量查询：
num = self.slave.query(func.count('1').label('count')).filter(KtvAgent.province_id!=0, KtvAgent.province_id!=1, KtvAgent.city_id==0, KtvAgent.payed==1).scalar()
#总量查询：
sum = self.slave.query(func.sum(CustomKtvOrder.fee)).filter(CustomKtvOrder.state==2, CustomKtvOrder.fee!=1).scalar()
#日期 :
count = self.slave.query(func.count('1').label('count')).filter(func.date(MusicOrder.create_time) == date).scalar()
#多查询：
res = self.slave.query(KtvStore).filter(KtvStore.store_id.in_(ktvids)).all()
res = self.slave.query(KtvStore).filter(KtvStore.store_id)
#删除：
self.master.query(WxWithdraw).filter(WxWithdraw.ktv_id == ktv_id).filter(func.date(WxWithdraw.create_time) == date).delete()
self.master.commit()
#增改的update：
def update(self, order_id, data):
    q = self.master.query(GzhDisOrder).filter_by(order_id=order_id)
    if q.scalar():
        q.update(data)
    else:
        self.master.add(GzhDisOrder(**data))
    self.master.commit()
