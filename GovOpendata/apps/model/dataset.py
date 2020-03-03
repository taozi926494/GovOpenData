from ...apps import Base, db
from typing import List
from flask_sqlalchemy import Pagination
from sqlalchemy import and_


class Dataset(Base):
    __tablename__ = 'dataset'
    gov_id = db.Column(db.Integer, comment="数据集所属得开放平台id")
    source = db.Column(db.String(255), comment="信息来源")
    subject = db.Column(db.String(255), comment="主题分类")
    update_date = db.Column(db.DateTime, comment="更新时间")
    acquire_date = db.Column(db.DateTime, comment="采集时间")
    abstract = db.Column(db.Text, comment="数据简介")
    view_num = db.Column(db.Integer, comment="浏览量")
    download_num = db.Column(db.Integer, comment="下载量")
    collect_num = db.Column(db.Integer, comment="收藏量")
    exract_info = db.Column(db.Text, comment="基础信息")
    field_info = db.Column(db.Text, comment="字段信息")
    path = db.Column(db.String(255), comment="数据文件子路径，用于查找文件及下载")

    def to_dict(self):
        return {
            "gov_id": self.gov_id,
            "source": self.source,
            "subject": self.subject,
            "update_date": self.update_date,
            "acquire_date": self.acquire_date,
            "abstract": self.abstract,
            "view_num": self.view_num,
            "download_num": self.download_num,
            "collect_num": self.collect_num,
            "exract_info": self.exract_info,
            "field_info": self.field_info,
            "path": self.path,
        }
