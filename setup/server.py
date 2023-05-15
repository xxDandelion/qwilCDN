from core.conn import Connect
import logging

logger = logging.getLogger('component_log')


class OriginServer:
    def __init__(self, data):
        self._conn = Connect(data.origin_server.address, data.origin_server.user,
                             data.origin_server.key)

    def transfer_file(self, destination):
        logger.info(f'transferring file to {destination}')
        pass
