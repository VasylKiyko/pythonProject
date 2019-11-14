import socket
import pickle
BUFFER = 4096
IP = "127.0.0.1"
PORT = 1230


class Client:
    def __init__(self):
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __del__(self):
        self.close_connection()

    def close_connection(self):
        self.__client_socket.close()


if __name__ == '__main__':
    log_in_data = ['Vasyl', 'kiko']
    data_to_send = pickle.dumps(log_in_data)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    client_socket.sendall(data_to_send)
    client_socket.settimeout(10)
    try:
        all_answer = bytearray()
        answer = client_socket.recv(BUFFER)
        all_answer += answer
        answer_ = pickle.loads(all_answer)
    except Exception as e:
        print('Exception - ', e)
    client_socket.close()
