from GovOpendata.apps import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


def set_model_by_dict(model: Base, data_dict: dict):
    """ 通过字典设置模型实例的值 """
    for key in data_dict:
        setattr(model, key, data_dict[key])
