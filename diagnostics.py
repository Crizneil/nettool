import subprocess
import socket


def copy_to_clipboard(text):
    """Copy text to the Linux clipboard using xclip."""
    try:
        process = subprocess.Popen(
            ["xclip", "-selection", "clipboard"],
            stdin=subprocess.PIPE
        )

        process.communicate(input=text.encode())

        return process.returncode == 0

    except (FileNotFoundError, OSError):
        return False


def ping_host(host):
    """Ping a host once and return the response time."""
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "2", host],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if "time=" in line:
                    return line.split("time=")[1].split()[0]

            return "OK"

        return None

    except Exception:
        return None


def get_gateway():
    """Get the default network gateway."""
    try:
        result = subprocess.run(
            ["ip", "route", "show", "default"],
            capture_output=True,
            text=True
        )

        parts = result.stdout.split()

        if "via" in parts:
            return parts[parts.index("via") + 1]

    except Exception:
        pass

    return None


def internet_diagnostics():
    """Run basic internet connectivity tests."""

    print("\nINTERNET DIAGNOSTICS")
    print("────────────────────")

    gateway = get_gateway()

    # Gateway test
    if gateway:
        gateway_ping = ping_host(gateway)

        print(f"\nGateway     : {gateway}")

        if gateway_ping:
            print(f"Gateway Ping: ✓ {gateway_ping} ms")
        else:
            print("Gateway Ping: ✗ FAILED")

    else:
        print("\nGateway     : NOT FOUND")
        print("Gateway Ping: ✗ FAILED")

    # Internet test
    print("\nInternet Test")

    google_ping = ping_host("8.8.8.8")

    if google_ping:
        print(f"8.8.8.8     : ✓ {google_ping} ms")
    else:
        print("8.8.8.8     : ✗ FAILED")

    # DNS test
    print("\nDNS Test")

    dns_ping = ping_host("google.com")

    if dns_ping:
        print(f"google.com  : ✓ {dns_ping} ms")
    else:
        print("google.com  : ✗ FAILED")

    print("\n────────────────────")

    if google_ping and dns_ping:
        print("Internet Status : ✓ ONLINE")
    elif google_ping:
        print("Internet Status : ⚠ DNS ISSUE")
    else:
        print("Internet Status : ✗ OFFLINE")

    print("\n────────────────────")


def speed_test():
    """Run an animated speed test using speedtest-cli."""

    import time
    import shutil
    import re

    print()
    print("╔══════════════════════════════════════════════╗")
    print("║              CRIZ SPEED TEST                 ║")
    print("╠══════════════════════════════════════════════╣")
    print("║                                              ║")

    if not shutil.which("speedtest-cli"):
        print("║  ✗ speedtest-cli is not installed.           ║")
        print("╚══════════════════════════════════════════════╝")
        return

    # -------------------------------------------------
    # STARTING ANIMATION
    # -------------------------------------------------

    print("║  Initializing", end="", flush=True)

    for _ in range(4):
        time.sleep(0.3)
        print(".", end="", flush=True)

    print(" ✓")

    print("║  Finding best server", end="", flush=True)

    for _ in range(4):
        time.sleep(0.3)
        print(".", end="", flush=True)

    print(" ✓")

    print("║")
    print("╠══════════════════════════════════════════════╣")
    print("║              RUNNING SPEED TEST              ║")
    print("╠══════════════════════════════════════════════╣")
    print("║")

    try:

        # Run normal speedtest-cli output
        process = subprocess.Popen(
            ["speedtest-cli"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        output_lines = []

        # Read output while speedtest is running
        while True:

            line = process.stdout.readline()

            if line == "" and process.poll() is not None:
                break

            if line:

                line = line.strip()

                if not line:
                    continue

                output_lines.append(line)

                # -----------------------------------------
                # DOWNLOAD
                # -----------------------------------------

                if "Retrieving speedtest.net configuration" in line:
                    print("║  ✓ Configuration retrieved")

                elif "Testing from" in line:
                    print(f"║  {line}")

                elif "Retrieving speedtest.net server list" in line:
                    print("║  ✓ Finding servers...")

                elif "Retrieving information" in line:
                    print("║  ✓ Selecting best server...")

                elif "Hosted by" in line:
                    print(f"║  ✓ {line}")

                elif "Testing download" in line:

                    print("║")
                    print("║  DOWNLOAD")
                    print("║  ", end="", flush=True)

                    # Animated indicator
                    for _ in range(20):
                        print("█", end="", flush=True)
                        time.sleep(0.03)

                    print("")

                # -----------------------------------------
                # UPLOAD
                # -----------------------------------------

                elif "Testing upload" in line:

                    print("║")
                    print("║  UPLOAD")
                    print("║  ", end="", flush=True)

                    for _ in range(20):
                        print("█", end="", flush=True)
                        time.sleep(0.03)

                    print("")

                # -----------------------------------------
                # RESULTS
                # -----------------------------------------

                elif line.startswith("Ping:"):
                    print(f"║  {line}")

                elif line.startswith("Download:"):
                    print(f"║  {line}")

                elif line.startswith("Upload:"):
                    print(f"║  {line}")

        process.wait()

        # ---------------------------------------------
        # FINAL RESULT
        # ---------------------------------------------

        ping = None
        download = None
        upload = None

        for line in output_lines:

            if line.startswith("Ping:"):
                ping = line.replace("Ping:", "").strip()

            elif line.startswith("Download:"):
                download = line.replace("Download:", "").strip()

            elif line.startswith("Upload:"):
                upload = line.replace("Upload:", "").strip()

        print("║")
        print("╠══════════════════════════════════════════════╣")
        print("║              FINAL RESULT                    ║")
        print("╠══════════════════════════════════════════════╣")

        print(f"║  Ping       : {ping or 'N/A':<27}║")
        print(f"║  Download   : {download or 'N/A':<27}║")
        print(f"║  Upload     : {upload or 'N/A':<27}║")

        print("╠══════════════════════════════════════════════╣")
        print("║              ✓ TEST COMPLETE                 ║")
        print("╚══════════════════════════════════════════════╝")

        # Copy result
        summary = (
            f"CRIZ SPEED TEST\n"
            f"Ping: {ping or 'N/A'}\n"
            f"Download: {download or 'N/A'}\n"
            f"Upload: {upload or 'N/A'}"
        )

        if copy_to_clipboard(summary):
            print("\n✓ Results copied to clipboard")

    except Exception as error:

        print()
        print(f"║  ✗ Error: {error}")
        print("╚══════════════════════════════════════════════╝")