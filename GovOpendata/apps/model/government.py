from GovOpendata.apps.model import db, Base


class Government(Base):
    """政府开放平台表"""
    __tablename__ = 'governmment'
    province = db.Column(db.String(255), comment="平台所属省")
    region = db.Column(db.String(255), comment="平台所属行政区域， 如贵阳市")
    dir_path = db.Column(db.String(255), unique=True, comment="该工程的文件目录名")

    file_num = db.Column(db.Integer, comment="文件数量")
    file_size = db.Column(db.Integer, comment="文件总大小")
    dataset_num = db.Column(db.Integer, comment="数据集数量")

    acquire_date = db.Column(db.DateTime, comment="采集时间")
    # path = db.Column(db.String(255), comment="数据文件路径，用于查找文件及下载")