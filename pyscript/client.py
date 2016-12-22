# coding=utf-8
from __future__ import unicode_literals, absolute_import
import socket
import logging

logger = logging.getLogger(__name__)


def simple_tcp_client(host='developers.google.cn', port=80, bytes_num=4096):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send('GET / HTTP/1.1\r\nHost: developers.google.cn\r\n\r\n')
    return client.recv(bytes_num)


def simple_udp_client(host='developers.google.cn', port=80, bytes_num=4096):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto('This is a udp client by python', (host, port))
    data, addr = client.recvfrom(bytes_num)
    return data, addr


if __name__ == '__main__':
    response = simple_tcp_client(host='0.0.0.0', port=9999)
    print 'test simple tcp client :', response
    # data, addr = simple_udp_client('127.0.0.1', port=10000)
    # print 'test simple udp client :', data, addr
