import socket
import time

recv_port = 0
host_port = 0
ip = '127.0.0.1'
username = ''
connected = False

def chat(socket):
  while True:
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
      socket.connect(('127.0.0.1', int(host_port)))

    except Exception, e:
      print '-------SOCKET ERROR------\n' + str(e)
    socket.send(raw_input(""))
    print "This should not be shown"
    data = s.recv(1024)
    socket.close()
    print 'Recived', repr(data)

def main():
  connect()

def connect():
  recv_port = raw_input("Choose recieving port: ")
  host_port = raw_input("Connect to host: ")
  username = raw_input("Choose a username: ")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  connected = False
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.bind((ip, recv_port))
  while connected == False:
    try:
      s.connect(('127.0.0.1', int(host_port)))
      connected = True
      chat(s)
      
    except (Exception):
      print "Not connected"
      time.sleep(1)

if __name__ == "__main__":
  main()
