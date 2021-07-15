import time
import socket


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self._data = {}
        self._host = host
        self._port = port
        self._timeout = timeout
        self._sock = socket.socket()
        self._sock_connect = (self._host, self._port)

    def get(self, metric):
        try:
            request = ('get ' + metric + '\n').encode()
            with socket.create_connection(self._sock_connect, timeout=self._timeout) as sock:
                sock.sendall(request)
                data = sock.recv(4096).decode().rstrip('\n')
                print("Data - ", data)

                if data.pop(0) != 'ok':
                    raise ClientError

                result_data = dict()
                for inf in data:
                    print(f'Inf - {inf};;;;;;Data - {data}')
                    if inf == '':
                        break
                    inf = inf.split()
                    key, value, timestamp = inf
                    if key in result_data:
                        result_data[key].append((int(float(timestamp)), float(value), ))
                        result_data[key].sort(key=lambda x: x[0])
                    else:
                        result_data[key] = [(int(float(timestamp)), float(value), )]
            return self.sort_dict(result_data)
        except ValueError:
            raise ClientError

    def put(self, metric, value, timestamp=None):
        try:
            def is_int(n):
                return int(n) == float(n)

            value = int(value) if is_int(value) else float(value)
            timestamp = int(time.time()) if not timestamp else int(timestamp)

            request = ('put ' + metric + ' ' + str(value) + ' ' + str(timestamp) + '\n').encode()

            with socket.create_connection(self._sock_connect, timeout=self._timeout) as sock:
                sock.sendall(request)

                answer = sock.recv(1024).decode()
                print('answer - ', answer)
                if answer != 'ok\n\n':
                    raise ClientError

        except ValueError:
            raise ClientError

    @staticmethod
    def sort_dict(data):
        list_data = list(data.items())
        list_data.sort(key=lambda x: x[1][0])
        return dict(list_data)
