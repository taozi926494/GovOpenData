from GovOpendata.apps.model import Base


class BaseSrv(object):
    orm = Base

    @classmethod
    def save(cls, **kwargs):
        return cls.orm.save(kwargs)

    @classmethod
    def all(cls, _to_dict: bool = True):
        return cls.orm.all(_to_dict)

    @classmethod
    def delete(cls, **kwargs):
        return cls.orm.delete(kwargs)

    @classmethod
    def find_by_id(cls, _id: int, _to_dict: bool = True):
        return cls.orm.find_by_id(_id, _to_dict=_to_dict)

