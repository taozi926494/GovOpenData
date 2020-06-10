from GovOpendata.apps.model import Base


class BaseSrv(object):
    @classmethod
    def inject(cls, orm: Base) -> "BaseSrv":
        cls.orm = orm
        return cls

    def save(self, **kwargs):
        return self.orm.save(kwargs)

    def all(self, _to_dict: bool = True):
        return self.orm.all(_to_dict)

    def delete(self, **kwargs):
        return self.orm.delete(kwargs)

    def find_by_id(self, _id: int, _to_dict: bool = True):
        return self.orm.find_by_id(_id, _to_dict=_to_dict)
