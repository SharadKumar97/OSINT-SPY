import os


def get_ciphers(server):
    command = f'pysslscan scan --scan=server.ciphers --tls10 {server}'
    os.system(command)


def heart_bleed(server):
    command = f'pysslscan scan --scan=vuln.heartbleed --tls10 {server}'
    os.system(command)
