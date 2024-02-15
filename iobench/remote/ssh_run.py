from os import PathLike
from typing import Union

import paramiko


class SSHRunner:
    def __init__(
        self,
        hostname: str,
        username: str,
        key_path: Union[PathLike, bytes, str],
        port: int = 22,
    ) -> None:
        self.client = paramiko.SSHClient()
        key = paramiko.PKey.from_path(key_path)
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=hostname, username=username, pkey=key, port=port)

    def run_non_blocking(self, command: str) -> None:
        transport = self.client.get_transport()
        session = transport.open_session()
        session.exec_command(command)
