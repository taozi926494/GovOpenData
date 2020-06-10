from ..model.SpiderRecord import SpiderRecord
from GovOpendata.apps.service import BaseSrv


class SpiderRecordSrv(BaseSrv):
    orm = SpiderRecord

