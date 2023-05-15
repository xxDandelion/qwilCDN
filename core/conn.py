import SSHClient as SSHClient


class Connect:

    def __init__(self, host, user, key):
        self.host = host
        self.user = user
        self.key = key
        self.client = None
        self.__connect()

    def __connect(self):
        try:
            self.client = SSHClient()
            self.client.load_system_host_keys()
            self.client.connect(hostname=self.host,
                                username=self.user,
                                key_filename=self.key)

        except Exception as err:
            print('Authentication Failed: Please check your network/ssh key')
        finally:
            return self.client

    def disconnect(self):
        self.client.close()

    def exec_command(self, command):
        if self.client is None:
            self.client == self.__connect()
        stdin, stdout, stderr = self.client.exec_command(command)
        status = stdout.channel.recv_exit_status()
        if status is 0:
            return stdout.read()
        else:
            return None
