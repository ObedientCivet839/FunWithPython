import sys
import syslog
import socket

class Logger:
    def __init__(self, handler):
        # Move the work into the Handler class.
        self.handler = handler
    
    def log(self, message):
        self.handler.emit(message)

class FilteredLogger(Logger):
    def __init__(self, pattern, handler):
        self.pattern = pattern
        super().__init__(handler)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

# Instead of subclass the message destination, adapt the destination into a file.
# Duck-typing.

class FileLikeSocket:
    def __init__(self, sock):
        self.sock = sock
    
    def write(self, message_and_newline):
        self.sock.sendall(message_and_newline.encode('ascii'))
    
    def flush(self):
        pass

class FileLikeSyslog:
    def __init__(self, priority):
        self.priority = priority
    
    def write(self, message_and_newline):
        message = message_and_newline.rstrip('\n')
        syslog.syslog(self.priority, message)
    
    def flush(self):
        pass


def main():
    sock1, sock2 = socket.socketpair()
    
    fs1 = FileLikeSocket(sock1)
    f1 = FilteredLogger('Error', fs1)
    f1.log('Ignored: not important message')
    f1.log('Error: important message')
    print('Socket2: The socket received: %r' % sock2.recv(512))
    
    fs2 = FileLikeSocket(sock2)
    f2 = FilteredLogger('Warning', fs2)
    f2.log('Ignored: not important message')
    f2.log('Warning: warning message')
    f2.log('Error: important message')
    print('Socket1: The socket received: %r' % sock1.recv(512))
    
if __name__ == "__main__":
    main()