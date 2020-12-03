import sys
import os
import logging
import concurrent_log_handler
import logging.config

def initlog(serverconf):
    logdir=serverconf.getoption('log', 'logroot')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logconf=serverconf.getoption('log', 'logconfig')
    logging.config.fileConfig(logconf)
