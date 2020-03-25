from GovOpendata.apps import restful_api
from GovOpendata.apps.controller.JobCtrl import JobCtrl
from GovOpendata.apps.controller.GovernmentCtrl import GovernmentCtrl
from GovOpendata.apps.controller.DatasetCtrl import DatasetCtrl
from GovOpendata.apps.controller.DatasetSearchCtrl import DatasetSearchCtrl
from GovOpendata.apps.controller.DatasetFilesCtrl import DatasetFilesCtrl
from GovOpendata.apps.controller.NewsCtrl import NewsCtrl


def regist_router():
    restful_api.add_resource(GovernmentCtrl, '/government')
    restful_api.add_resource(DatasetCtrl, '/dataset')
    restful_api.add_resource(DatasetSearchCtrl, '/search')
    restful_api.add_resource(DatasetFilesCtrl, '/files')
    restful_api.add_resource(JobCtrl, '/job')
    restful_api.add_resource(NewsCtrl, '/news')

