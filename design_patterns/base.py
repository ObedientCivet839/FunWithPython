import sys
import syslog

class Logger(object):
    def __init__(self, file):
        self.file = file
    
    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()

# Two subclasses that send messages to different destinations.

class SocketLogger(Logger):
    """Subclass of Logger that sends message to Unix socket.

    Args:
        Logger (_type_): _description_
    """
    def __init__(self, sock):
        self.sock = sock
    
    def log(self, message):
        """Overwrite parent's default behavior to log message to a file.
        Instead, send message to a Unix socket.

        Args:
            message (str): message to log
        """
        self.sock.sendall((message + '\n').encode('ascii'))

class SyslogLogger(Logger):
    """Subclass of Logger that sends message to syslog.

    Args:
        Logger (_type_): _description_
    """
    def __init__(self, priority):
        self.priority = priority
    
    def log(self, message):
        syslog.syslog(self.priority, message)


# Subclass that does a different action that other subclasses
# i.e. filtering logs instead of setting message destination.

class FilteredLogger(Logger):
    def __init__(self, pattern, file):
        self.pattern = pattern
        super().__init__(file)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

# BUG(P0): Subclass explosion - we have to define all subclasses for each combination of behaviors.
class FilteredSocketLogger(Logger):
    def __init__(self, pattern, sock):
        self.sock = sock
        self.pattern = pattern
    
    def log(self, message):
        if self.pattern in message:
            self.sock.sendall((message + '\n').encode('ascii'))

def main():
    f = FilteredLogger('Error', sys.stdout)
    f.log('Ignored: not important message')
    f.log('Error: important meesage')
    
if __name__ == "__main__":
    main()