from core.conn import Connect
import logging
logger = logging.getLogger('component_log')


class Client:
    def __init__(self, data, router, cache_servers):
        self._conn = Connect(data.address, data.user,
                             data.key)
        self.cache_servers = cache_servers
        self.router = router

    def request_content(self):
        logger.info('requesting content')
        pass

    def get_content(self):
        pass
