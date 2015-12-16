if callfunc == 'initialize':
  ip = callargs[0]
  port = int(callargs[1])
  message = callargs[2]
  try:
    socket = openconn(ip, port)
    socket.send(message)
    socket.close()
  except Exception, e:
    print '-------SOCKET ERROR------\n' + str(e)