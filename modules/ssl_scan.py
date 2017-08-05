import os

def getCiphers(server):
    command='pysslscan scan --scan=server.ciphers --tls10'+' '+server
    out=os.system(command)


def heartBleed(server):
    command="pysslscan scan --scan=vuln.heartbleed --tls10"+' '+server
    os.system(command)

