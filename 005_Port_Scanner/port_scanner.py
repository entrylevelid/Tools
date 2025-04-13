# =============================================
#  Entry Level ID
# =============================================

import socket

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        sock.close()

    except KeyboardInterrupt:
        print("\nExiting...")
        exit()
    
    except socket.error:
        print("Unable to connect to the server")

if __name__ == '__main__':
    host = input("Enter target IP or domain: ")
    ports = [21, 22, 25, 53, 23, 80, 110, 143, 445, 443]

    print(f"\nScanning {host}...\n")

    for port in ports:
        scan_port(host, port)