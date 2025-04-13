# =============================================
#  Entry Level ID
# =============================================

import whois

def whois_lookup(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        return domain_info
    except Exception as e:
        return str(e)
    
domain_name = input("Enter the domain name: ")
result = whois_lookup(domain_name)
print(result)