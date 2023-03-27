import sys
import syslog

# The loggers all perform real output

class FileLogger:
    def __init__(self, file):
        self.file = file
    
    def log(self, message):
        self.file.write(message + '\n')
        self.file.flush()

class SocketLogger:
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

class SyslogLogger:
    """Subclass of Logger that sends message to syslog.

    Args:
        Logger (_type_): _description_
    """
    def __init__(self, priority):
        self.priority = priority
    
    def log(self, message):
        syslog.syslog(self.priority, message)

# The filter calls the same method it offers.


class LogFilter:
    def __init__(self, pattern, logger):
        self.pattern = pattern
        self.logger = logger
    
    def log(self, message):
        # Filtering code is moved outside of the logger class.
        # Now it can be wrapped around any logger we want.
        if self.pattern in message:
            self.logger.log(message)

def main():
    log1 = FileLogger(sys.stdout)
    log2 = LogFilter('Error', log1)
    log1.log('log1: Noisy: this logger always produces output')
    
    log2.log('log2: Ignored: not important message')
    log2.log('log2: Error: important meesage')

    # Decorator allows stacking objects on top of each other since they have the same interface. (They are all loggers)
    log3 = LogFilter('severe', log2)
    log3.log('log3: Error: this is bad, but not that bad')
    log3.log('log3: Error: this is pretty severe')
    
if __name__ == "__main__":
    main()