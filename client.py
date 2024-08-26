import socket
import time
def send_command(host, port, command):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.sendall(command.encode())
        print(f"Command '{command}' sent to {host}:{port}")
        client_socket.close()
    except Exception as e:
        print(f"Error sending command '{command}' to {host}:{port}: {str(e)}")



if _name_ == "_main_":
    host = "10.4.11.27"
    port = 6565  

    # Send commands
 send_command(host, port, "disable_ethernet")
    time.sleep(1)
