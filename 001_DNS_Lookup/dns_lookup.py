# =============================================
#  Entry Level ID
# =============================================

import socket

def dns_lookup(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return "Domain not found"
    
def main():
    domain = input("Enter domain name: ").strip()

    if not domain:
        print("Domain name cannot be empty!")
        return
    
    ip_address = dns_lookup(domain)
    print(f"IP Address for {domain}: {ip_address}")

if __name__ =="__main__":
    main()
