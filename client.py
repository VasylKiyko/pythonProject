import socket
import json
HEADER_BUFFER = 10
IP = "127.0.0.1"
PORT = 10145


def send_data(sock, data):
    """ надстлає data на вказаний sock у вигляді json рядка"""
    data_send = json.dumps(data).encode('utf-8')
    data_length = len(data_send)
    message_header = f"{data_length :< {HEADER_BUFFER}}".encode("utf-8")
    sock.sendall(message_header + data_send)


def receive(sock: socket):
    """отримує повідомлення з socket у вигляді json рядка"""
    try:
        message_header = sock.recv(HEADER_BUFFER)
        if not len(message_header):
            return False
        message_length = int(message_header.decode('utf-8').strip())
        data = sock.recv(message_length)
        json_data = json.loads(data.decode('utf-8'))
        #print(json_data)
        return True, json_data
    except:
        return False, {}


class Client:
    def __init__(self):
        self.__username = None
        self.__name = None
        self.__surname = None
        self.__city = None
        self.__client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client_socket.connect((IP, PORT))

    def __del__(self):
        self.close_connection()

    def close_connection(self):
        self.__client_socket.close()

    def set_personal_data(self, map_):
        self.__name = map_['name']
        self.__surname = map_['surname']
        self.__city = map_['city']
        self.__username = map_['username']

    def log_in(self, log_in_data):
        data = {'action': 'log in', 'username': log_in_data[0], 'password': log_in_data[1]}
        send_data(self.__client_socket, data)
        #print("Send data")
        isdata, data = receive(self.__client_socket)
        if isdata:
            #print("Received data")
            if data['answer']:
                self.set_personal_data(data)
                #print(data)
            else:
                pass
                #print('Wrong input data')

    def sign_up(self, registration_data):
        data = {'action': 'sign up', 'username': registration_data[0], 'password': registration_data[1],
                'name': registration_data[2], 'surname': registration_data[3],
                'city': registration_data[4]}
        send_data(self.__client_socket, data)
        #print("Send data")
        isdata, data = receive(self.__client_socket)
        if isdata:
            pass
            #print("Received data")
            #print(data)
        return data['answer']