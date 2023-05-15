from abc import ABC, abstractmethod
from core.conn import Connect
import logging
logger = logging.getLogger('component_log')


class Cache(ABC):

    @abstractmethod
    def get_content(self, path: str):
        raise NotImplementedError

    @abstractmethod
    def remove_content(self, path: str):
        raise NotImplementedError

    @abstractmethod
    def return_state(self, path: str):
        raise NotImplementedError


class AWSCache(Cache):

    def __init__(self, data, origin_server):
        self._conn = Connect(data.address, data.user,
                             data.key)
        self.origin_server = origin_server
        self.data = data

    def get_content(self, path: str):
        logger.info('getting_content')
        pass

    def remove_content(self, path: str):
        pass

    def return_state(self, path: str):
        pass

    def modify_cpu(self):
        pass

    def modify_ram(self):
        pass

    def modify_storage(self):
        pass


class InternalCache(Cache):

    def __init__(self, data, origin_server):
        self._conn = Connect(data.origin_server.address, data.origin_server.user,
                             data.origin_server.key)
        self.origin_server = origin_server
        self.data = data

    def get_content(self, path: str):
        pass

    def remove_content(self, path: str):
        pass

    def return_state(self, path: str):
        pass
