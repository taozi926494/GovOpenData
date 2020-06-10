from GovOpendata.apps.model import db, Base


class Dataset(Base):
    """数据集表"""
    __tablename__ = 'dataset'
    name = db.Column(db.String(255), comment="数据文件子路径，用于查找文件及下载")
    abstract = db.Column(db.Text, comment="数据简介")
    
    gov_id = db.Column(db.Integer, comment="数据集所属得开放平台id")
    department = db.Column(db.String(255), comment="数据发布部门")
    subject_origin = db.Column(db.String(255), comment="源网站的主题分类")
    subject_auto = db.Column(db.String(255), comment="自动分级分类的主题分类")
    industry = db.Column(db.String(255), comment="行业分类")
    update_date = db.Column(db.DateTime, comment="更新时间")
    
    extra_info = db.Column(db.Text, comment="其他信息")
    field_info = db.Column(db.Text, comment="字段信息")
    
    view_num = db.Column(db.Integer, comment="浏览量", default=0)
    download_num = db.Column(db.Integer, comment="下载量", default=0)
    collect_num = db.Column(db.Integer, comment="收藏量", default=0)


