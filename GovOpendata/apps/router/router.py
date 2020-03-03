from ...apps import restful_api
from ..controller.government import Gov
from ..controller.dataset import DatasetDetailController, FileDownloadController, DatasetViewController, DatasetDepartmentController

from GovOpendata.apps.controller.DatasetSearchCtrl import DatasetSearchCtrl


def regist_router():
    restful_api.add_resource(Gov, '/government')
    restful_api.add_resource(DatasetDetailController, '/detailInfo')
    restful_api.add_resource(FileDownloadController, '/download/<path>')
    # 数据总览
    restful_api.add_resource(DatasetViewController, '/datasetView')
    # 来源部门数据查询数据
    restful_api.add_resource(DatasetDepartmentController, '/datasetDepartment')
    restful_api.add_resource(DatasetSearchCtrl, '/search')
