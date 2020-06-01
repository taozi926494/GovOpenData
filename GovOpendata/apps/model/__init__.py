from GovOpendata.apps import app
from typing import List

from flask_restful import abort
from flask_sqlalchemy import SQLAlchemy
import base64
from sqlalchemy import DateTime, Date, Numeric, LargeBinary
import datetime
db = SQLAlchemy(app, session_options=dict(autocommit=False, autoflush=True))
db.init_app(app)


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    def to_dict(self) -> "dict":
        dic = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            if isinstance(column.type, Date):
                value = value.strftime('%Y-%m-%d') and value
            elif isinstance(column.type, DateTime) and value:
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(column.type, Numeric):
                value = float(value)
            elif isinstance(column.type, LargeBinary):
                value = str(base64.b64encode(value))
                value = value.replace("b'", '')
                value = value[:-1]
            dic[column.name] = value
        return dic

    def set(self, dic: dict):
        columns = [col.name for col in self.__table__.columns]
        for key, val in dic.items():
            if key not in columns:
                raise KeyError('%s has no column %s' % (self.__table__, key))
            else:
                setattr(self, key, val)

    @classmethod
    def save(cls, dic: dict) -> "Dict or None":
        try:
        # TODO 多个联合主键在新增和更新的时候需要进行存在性判断（参照servermachine）
            if 'id' in dic:
                item = cls.query.filter(cls.id == dic['id']).first()
                if item is None:
                    raise ValueError('Table %s has no data where id %s' % (cls.__table__, dic['id']))
                else:
                    item.set(dic)
                    dic = item.to_dict()
            else:
                item = cls()
                item.set(dic)
                db.session.add(item)
            db.session.commit()
            dic['id'] = item.id
            return dic
        except Exception as err:
            abort(500, message=str(err))

    @classmethod
    def delete(cls, filters: dict) -> bool:
        try:
            objs = cls.query.filter_by(**filters).all()
            for item in objs:
                db.session.delete(item)
                db.session.commit()
            return True
        except IOError as err:
            abort(500, message=str(err))

    @classmethod
    def find_by_id(cls, _id: int, _to_dict: bool = True) -> "Base":
        item = cls.query.filter(cls.id == _id).first()
        return item.to_dict() if _to_dict and item is not None else item

    @classmethod
    def all(cls, _to_dict: bool = True) -> "List":
        data = cls.query.all()
        return [item.to_dict() for item in data] if _to_dict else data

    @classmethod
    def page_query(cls, page_index, page_size) -> dict:
        pagination = cls.query.paginate(
            page=page_index, per_page=page_size, error_out=False)
        res = {
            "total": pagination.total,
            "data": [item.to_dict() for item in pagination.items]
        }
        return res

