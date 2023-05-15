from core.conn import Connect
import json
import logging
logger = logging.getLogger('component_log')


class Monitor:
    def __init__(self, data, cache_servers):
        self._conn = Connect(data.address, data.user,
                             data.key)
        self.cache_servers = cache_servers
        self.cache_data = None

    def cache_data_update(self):
        logger.info('updating cache')
        with open('../cache_data.json') as f:
            self.cache_data = json.load(f)

    def cache_data_status(self):
        return self.cache_data
