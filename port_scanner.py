import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = input("Enter the IP address you want to scan: ")
port = int(input("Enter the Port you want to scan: "))

def port_scanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed.")
    else:
        print("The port is open.")

port_scanner(port)