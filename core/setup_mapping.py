from setup import cache, server, monitor, router, client
import json


class Cluster:
    def __init__(self):
        self.conf_file = None
        self.cluster = {}
        self.origin_server = None
        self.cache_servers = []
        self.router = None
        self.monitor_server = None
        self.clients = []
        self.init_setup()

    def init_setup(self):
        with open('/setup_configuration.json') as f:
            self.conf_file = json.load(f)
            self.origin_server = server.OriginServer(self.conf_file.origin_server)
            for cache_server in self.conf_file.cache_servers:
                if cache_server.type == 'aws':
                    self.cache_servers.append(cache.AWSCache(cache_server, self.origin_server))
                if cache_server.type == 'internal':
                    self.cache_servers.append(cache.InternalCache(cache_server, self.origin_server))
            self.monitor_server = monitor.Monitor(self.conf_file.monitor, self.cache_servers)
            self.router = router.Router(self.conf_file.router, self.monitor_server)
            for _client in self.conf_file.clients:
                self.clients.append(client(_client, self.router, self.cache_servers))

    def build_cluster(self, tag, obj):
        pass

    def clear_cluster(self):
        pass
