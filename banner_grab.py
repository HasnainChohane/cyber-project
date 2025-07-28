# modules/banner_grab.py

import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner if banner else "No banner returned"
    except Exception as e:
        return f"[ERROR] Could not grab banner: {e}"


