import os
import platform
import sys
from optparse import OptionParser
sys.path.append(os.getcwd())
from GovOpendata.apps import app, initialize


def main():
    opts, args = parse_opts(app.config)
    if opts.dev:
        sys_type = platform.system()
        # linux系统下
        if sys_type == "Linux":
            print("Please Force Input --dev Option !")
            return

        data_root_path = r"D:\Code\0CETC_Projects\GovOpendataCenter\GovOpendataCrawlers"
        debug = True
    else:
        data_root_path = r"/mnt/nfs/GovOpenDataCrawlers"
        debug = False
    app.config.update(dict(
        SQLALCHEMY_DATABASE_URI=opts.database_url,
        DATA_ROOT_PATH = data_root_path
    ))
    initialize()
    app.run(host=opts.host, port=opts.port, debug=debug, threaded=True)

def parse_opts(config):
    parser = OptionParser(usage="%prog [options]",
                          description="Admin ui for spider service")
    parser.add_option("--host",
                      help="host, default:0.0.0.0",
                      dest='host',
                      default='0.0.0.0')
    parser.add_option("--port",
                      help="port, default:5000",
                      dest='port',
                      type="int",
                      default=5009)
    parser.add_option("--database-url",
                      help='database default: %s' % config.get('SQLALCHEMY_DATABASE_URI'),
                      dest='database_url',
                      default=config.get('SQLALCHEMY_DATABASE_URI'))
    parser.add_option("--dev",
                      help="develop or production model",
                      default=True)
    return parser.parse_args()


if __name__ == '__main__':
    main()