if args.active:
    logger.info("Running Active Recon...")

    # 1. Port Scan
    print("\n[+] Scanning Common Ports...")
    open_ports = port_scan.scan_ports(args.target)
    if not open_ports:
        print("[!] No open common ports found.")
    else:
        for port, service in open_ports:
            print(f"Port {port} OPEN ({service})")

    # 2. Banner Grabbing
    print("\n[+] Grabbing Banners...")
    for port, _ in open_ports:
        banner = banner_grab.grab_banner(args.target, port)
        print(f"Banner for port {port}: {banner}")

    # 3. Technology Detection
    print("\n[+] Detecting Technologies (WhatWeb)...")
    techs = tech_detect.detect_tech(args.target)
    print(techs)
