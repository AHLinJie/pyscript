# coding=utf-8
from __future__ import unicode_literals, absolute_import
import threading
import socket
import sys
import logging

logger = logging.getLogger(__name__)


def simple_tcp_server(bind_ip="0.0.0.0", bind_port=9999):
    # multi-threaded tcp server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print "[*] Listening on %s:%d" % (bind_ip, bind_port)

    # this is our client-handling thread
    def handle_client(client_socket):
        # print out what the client sends
        request = client_socket.recv(1024)
        print "[*] Received: %s" % request
        # send back a packet
        client_socket.send("ACK!")
        client_socket.close()

    while True:
        client, addr = server.accept()
        print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
        # spin up our client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def simple_udp_server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print >> sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)
    while True:
        print >> sys.stderr, '\nwaiting to receive message'
        data, address = sock.recvfrom(4096)
        print >> sys.stderr, 'received %s bytes from %s' % (len(data), address)
        print >> sys.stderr, data
        if data:
            sent = sock.sendto(data, address)
            print >> sys.stderr, 'sent %s bytes back to %s' % (sent, address)


if __name__ == '__main__':
    # simple_udp_server()
    simple_tcp_server()
