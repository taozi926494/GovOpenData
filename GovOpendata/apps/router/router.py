from GovOpendata.apps import restful_api
from GovOpendata.apps.controller.GovernmentCtrl import GovernmentCtrl
from GovOpendata.apps.controller.DatasetCtrl import DatasetCtrl
from GovOpendata.apps.controller.DatasetSearchCtrl import DatasetSearchCtrl
from GovOpendata.apps.controller.DatasetFileDownloadCtrl import DatasetFileDownloadCtrl


def regist_router():
    restful_api.add_resource(GovernmentCtrl, '/government')
    restful_api.add_resource(DatasetCtrl, '/detail')
    restful_api.add_resource(DatasetSearchCtrl, '/search')
    restful_api.add_resource(DatasetFileDownloadCtrl, '/download')

