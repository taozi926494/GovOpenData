import os
import platform
import sys
from optparse import OptionParser
sys.path.append(os.getcwd())
from GovOpendata.apps import app

if __name__ == '__main__':
    data_root_path = r"E:\code\systems2020\GovOpendataCrawlers"
    app.config.update(dict(
        DATA_ROOT_PATH=data_root_path
    ))
    app.run(host='0.0.0.0', port=5009, debug=True)
