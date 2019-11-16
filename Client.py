import socket
import pickle
BUFFER = 4096
IP = "127.0.0.1"
PORT = 4578


class Client:
    def __init__(self):
        self.__name = 'None'
        self.__surname = 'None'
        self.__location = 'None'
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_socket.connect((IP, PORT))

    def __del__(self):
        self.close_connection()

    def close_connection(self):
        self.__client_socket.close()

    def set_personal_data(self, map_):
        self.__name = map_['name']
        self.__surname = map_['surname']
        self.__location = map_['location']

    def log_in(self, data):
        data_send = pickle.dumps(data)
        self.__client_socket.sendall(data_send)
        self.__client_socket.settimeout(10)
        try:
            answer = bytearray()
            b_answer = self.__client_socket.recv(BUFFER)
            answer += b_answer
            personal_data = pickle.loads(answer)
        except Exception as e:
            print('Exception - ', e)


if __name__ == '__main__':
    log_in_data = ['Vasyl', 'kiko']
    client = Client()
    client.log_in(log_in_data)
    client.close_connection()
