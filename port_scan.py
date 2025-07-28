# modules/port_scan.py

import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

def scan_ports(target, ports=COMMON_PORTS.keys()):
    open_ports = []
    for port in ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((target, port))
            open_ports.append((port, COMMON_PORTS.get(port, "Unknown")))
            s.close()
        except:
            continue
    return open_ports
