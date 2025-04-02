import os
import platform

def ping(host):
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    response = os.system(f"ping {param} {host} > nul 2>&1" if platform.system() == "Windows" else f"ping {param} {host} >/dev/null 2>&1")

    if response == 0:
        print(f"{host} is Online")
    else:
        print(f"{host} is Offline")

if __name__ == "__main__":
    target = input("Enter IP or domain to ping: ")
    ping(target)