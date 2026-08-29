import subprocess
import socket


def show_network_info():
    print("\nNETWORK INFORMATION")
    print("───────────────────")

    hostname = socket.gethostname()

    try:
        local_ip = socket.gethostbyname(hostname)
    except socket.error:
        local_ip = "Unavailable"

    try:
        result = subprocess.run(
            ["ip", "route", "show", "default"],
            capture_output=True,
            text=True
        )

        parts = result.stdout.split()

        if "via" in parts:
            gateway = parts[parts.index("via") + 1]
        else:
            gateway = "Unavailable"

    except Exception:
        gateway = "Unavailable"

    print(f"\nHostname : {hostname}")
    print(f"Local IP : {local_ip}")
    print(f"Gateway  : {gateway}")