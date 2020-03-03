from GovOpendata.apps.model import db, Base


class Dataset(Base):
    """数据集表"""
    __tablename__ = 'dataset'
    name = db.Column(db.String(255), comment="数据文件子路径，用于查找文件及下载")
    abstract = db.Column(db.Text, comment="数据简介")
    
    gov_id = db.Column(db.Integer, comment="数据集所属得开放平台id")
    department = db.Column(db.String(255), comment="数据发布部门")
    subject = db.Column(db.String(255), comment="主题分类")
    industry = db.Column(db.String(255), comment="行业分类")
    
    extra_info = db.Column(db.Text, comment="其他信息")
    field_info = db.Column(db.Text, comment="字段信息")
    
    view_num = db.Column(db.Integer, comment="浏览量")
    download_num = db.Column(db.Integer, comment="下载量")
    collect_num = db.Column(db.Integer, comment="收藏量")

    update_date = db.Column(db.DateTime, comment="更新时间")
    acquire_date = db.Column(db.DateTime, comment="采集时间")

    def to_dict(self):
        return {
            "name": self.name,
            "abstract": self.abstract,
            "gov_id": self.gov_id,
            "department": self.department,
            "subject": self.subject,
            "industry": self.industry,
            "extra_info": self.extra_info,
            "field_info": self.field_info,
            "view_num": self.view_num,
            "download_num": self.download_num,
            "collect_num": self.collect_num,
            "update_date": self.update_date,
            "acquire_date": self.acquire_date,
        }
