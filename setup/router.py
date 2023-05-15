import json
from core.conn import Connect
import logging
logger = logging.getLogger('component_log')


class Router:
    def __init__(self, data, monitor):
        self._conn = Connect(data.address, data.user,
                             data.key)
        self.monitor = monitor

    def get_state(self):
        logger.info('getting state')
        pass

    def redirect(self):
        pass
