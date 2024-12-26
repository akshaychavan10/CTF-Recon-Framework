import socket

# A small wordlist for brute-forcing; expand this as needed
WORDLIST = [
    "www", "mail", "ftp", "dev", "staging", "test", "api", "blog", "shop", "news"
]

def brute_force_subdomains(domain):
    """Brute force subdomains for a given domain using a wordlist."""
    subdomains = []
    print("Starting brute-force subdomain enumeration...")
    
    for word in WORDLIST:
        subdomain = f"{word}.{domain}"
        try:
            # Attempt to resolve the subdomain
            socket.gethostbyname(subdomain)
            print(f"Found subdomain: {subdomain}")
            subdomains.append(subdomain)
        except socket.gaierror:
            # Subdomain does not resolve; skip it
            continue
    
    return subdomains
