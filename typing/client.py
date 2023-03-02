from typing import Optional


class NetworkClient:
    def __init__(self):
        self.connection = None
        self.remote_addr = None

    def connect(self, address):
        ...
        """
        (self.connection, self.remote_addr) = connect_to_server(address)
        """

    def send_message(self, msg):
        self.connection.send(msg)

    def close(self):
        self.connection.close()
        self.connection = None
        self.remote_addr = None



class ConnectedClient:
    def __init__(self, connection: ..., remote_addr: str):
        self.connection = connection
        self.remote_addr = remote_addr

    def send_message(self, msg):
        ...

    def close(self):
        pass


def connect_to(address) -> Optional[ConnectedClient]:
    pass
