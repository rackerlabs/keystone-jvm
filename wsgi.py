#!/usr/bin/env python


def get_application(configure=True):
    import os
    import sys
    import java.util
    from java.io import File
    from org.python.util import jython

    jar_location = (jython()
                    .getClass()
                    .getProtectionDomain()
                    .getCodeSource()
                    .getLocation()
                    .getPath())
    sys.executable = jar_location

    import pbr.version
    pbr.version.VersionInfo.version_string = lambda x: ''

    from keystone import backends
    from keystone import config
    from keystone.common import sql
    from oslo.db import options as db_options
    from keystone.common import dependency
    import logging
    from paste import deploy
    from java.lang import System

    logging.basicConfig()
    if configure:
        config.configure()
    CONF = config.CONF

    sql.initialize()

    prop_dir = System.getProperty("config_dir", "etc")

    if len(sys.argv) > 0:
        saved_argv = sys.argv
        sys.argv = [sys.argv[0]]

    config_file = ['{prop_dir}/keystone.conf'.format(prop_dir=prop_dir)]
    CONF(project='keystone', prog='keystone', default_config_files=config_file)

    name = 'main'
    name = 'admin'

    config.setup_logging()
    if CONF.debug:
        CONF.log_opt_values(logging.getLogger(CONF.prog), logging.DEBUG)
    elif CONF.verbose:
        CONF.log_opt_values(logging.getLogger(CONF.prog), logging.INFO)
    else:
        CONF.log_opt_values(logging.getLogger(CONF.prog), logging.WARNING)

    backends.load_backends()

    application = deploy.loadapp('config:{prop_dir}/keystone-paste.ini'.format(
        prop_dir=prop_dir), name=name, relative_to='.')

    dependency.resolve_future_dependencies()

    if len(sys.argv) > 0:
        sys.argv = saved_argv

    return application

application = get_application()


def run():
    from paste import httpserver

    httpserver.serve(application, host='127.0.0.1', port='35357')

if __name__ == "__main__":
    run()
