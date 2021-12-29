import socket
import warnings
from typing import Optional

try:
    import requests as ret


    class request:
        @staticmethod
        def GET(ip: str = socket.gethostbyname(socket.gethostname()), localhost: int = 8080, mapping: str = '/') -> \
                Optional[ret.Response]:
            try:
                return ret.get(f'http://{ip}:{localhost}{mapping}')
            except ret.exceptions.ConnectionError:
                return None

        @staticmethod
        def POST(ip: str = socket.gethostbyname(socket.gethostname()), localhost: int = 8080, mapping: str = '/') -> \
                Optional[ret.Response]:
            try:
                return ret.post(f'http://{ip}:{localhost}{mapping}')
            except ret.exceptions.ConnectionError:
                return None

except ImportError:
    warnings.warn('Not found module named requests. Please try the command \'pip install requests\' to install web '
                  'module.')


    def GET():
        ...


    def POST():
        ...
