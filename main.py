#!/usr/bin/env python3

from converters import convert_ppoe, convert_static
from diagnostics import internet_diagnostics, speed_test
from concerns import concern_tracker


def main():
    while True:
        print()
        print("╔══════════════════════════════════════╗")
        print("║          CRIZ_GH0STR1D3R_IT          ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. PPOE / Dalo IP Converter         ║")
        print("║  2. Static IP Converter              ║")
        print("║  3. Internet Diagnostics             ║")
        print("║  4. Speed Test                       ║")
        print("║  5. Concern Tracker                  ║")
        print("║  6. Exit                             ║")
        print("╚══════════════════════════════════════╝")

        choice = input("\nSelect: ").strip()

        # -----------------------------------------
        # PPOE / DALO IP CONVERTER
        # -----------------------------------------

        if choice == "1":
            code = input("\nEnter PPOE/Dalo code: ")

            try:
                ip = convert_ppoe(code)

                print(f"\nCode : {code.upper()}")
                print(f"IP   : {ip}")
                print("VLAN : 10")

            except ValueError as error:
                print(f"\nError: {error}")

        # -----------------------------------------
        # STATIC IP CONVERTER
        # -----------------------------------------

        elif choice == "2":
            print("\nSTATIC IP CONVERTER")
            print("───────────────────")

            code = input("Enter static code: ")

            try:
                ip, floor, host = convert_static(code)

                print(f"\nCode     : {code.upper()}")
                print(f"Building : {code[0].upper()}")
                print(f"Floor    : {floor}")
                print(f"Host     : {host}")
                print(f"IPv4     : {ip}")
                print("VLAN     : 20")

            except ValueError as error:
                print(f"\nError: {error}")

        # -----------------------------------------
        # INTERNET DIAGNOSTICS
        # -----------------------------------------

        elif choice == "3":
            internet_diagnostics()

        # -----------------------------------------
        # SPEED TEST
        # -----------------------------------------

        elif choice == "4":
            speed_test()

        # -----------------------------------------
        # CONCERN TRACKER
        # -----------------------------------------

        elif choice == "5":
            concern_tracker()

        # -----------------------------------------
        # EXIT
        # -----------------------------------------

        elif choice == "6":
            print("\nGoodbye.")
            break

        # -----------------------------------------
        # INVALID OPTION
        # -----------------------------------------

        else:
            print("\nInvalid selection.")


if __name__ == "__main__":
    main()