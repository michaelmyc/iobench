import paramiko

client = paramiko.SSHClient()

k = paramiko.PKey.from_path("/Users/michaelmao/.ssh/test")

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="localhost", username="michaelmao", pkey=k)

transport = client.get_transport()
session = transport.open_session()
session.exec_command("/opt/homebrew/bin/blender")
