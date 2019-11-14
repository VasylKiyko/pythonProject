import pickle
import socket

BUFFER = 4096
IP = "127.0.0.1"
PORT = 1230
users = [
    {'name': "Vasyl", 'password': 'kiko', 'city': 'Lviv'},
    {'name': "Bogdan", 'password': 'arab', 'city': 'Lviv'},
    {'name': "Oleh", 'password': 'sopr', 'city': 'Lviv'}
]


def send_data(client, name):
    try:
        data = {}
        for maps in users:
            if maps['name'] == name:
                data = maps
                break

        data_to_send = pickle.dumps(data)
        client.sendall(data_to_send)
    except Exception as e:
        print('Exception ', e)
        return False


def check_client(person):
    for maps in users:
        if maps['name'] == person[0]:
            if maps['password'] == person[1]:
                return True
    return False


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen(10)

    while True:
        try:
            client, address = server_socket.accept()
        except KeyboardInterrupt:
            server_socket.close()
            break
        except Exception as e:
            print("Exception", e)
            server_socket.close()
            break
        else:
            all_data = bytearray()
            data = client.recv(BUFFER)
            all_data += data
            log_in_data = pickle.loads(all_data)
            print(f"Info from {address} is {log_in_data}")
            if check_client(log_in_data):
                send_data(client, log_in_data[0])
            client.close()


if __name__ == '__main__':
    main()