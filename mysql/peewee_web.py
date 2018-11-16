import peewee as pw

DB = pw.MySQLDatabase("songs",
                       host="127.0.0.1",
                       port=3306,
                       user="root",
                       passwd="thunder5166")


class MySQLModel(pw.Model):

    class Meta:
        database = DB


class ThunderSong(MySQLModel):
    id = pw.IntegerField()
    thunder_id = pw.CharField()
    name = pw.CharField()
    artist1 = pw.CharField()
    artist2 = pw.CharField()
    artist3 = pw.CharField()
    artist4 = pw.CharField()
    duration = pw.IntegerField()
    download_link = pw.CharField()
    has_krc = pw.IntegerField()
    state = pw.IntegerField()
    about = pw.CharField()
    ori_ks_url = pw.CharField()
    bt_ks_url = pw.CharField()
    krc_ks_url = pw.CharField()

    class Meta:
        db_table = 'thunder_song'


class KugouKrcSong(MySQLModel):
    id = pw.IntegerField()
    o2o_id = pw.IntegerField()
    krc_link = pw.CharField()
    download_link = pw.CharField()
    sim_hash = pw.CharField()

    class Meta:
        db_table = 'kugou_krc_song'


DB.connect()

# usage
# from db.py import KugouKrcSong
# KugouKrcSong.update(name=name).where(KugouKrcSong.id == 1)
