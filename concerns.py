import json
import os
from datetime import datetime


CONCERNS_FILE = "concerns.json"


def load_concerns():
    """Load saved concerns from the JSON file."""

    if not os.path.exists(CONCERNS_FILE):
        return []

    try:
        with open(CONCERNS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_concerns(concerns):
    """Save concerns to the JSON file."""

    with open(CONCERNS_FILE, "w", encoding="utf-8") as file:
        json.dump(concerns, file, indent=4)


def add_concern():
    """Create a new concern."""

    print("\nADD CONCERN")
    print("────────────────────")

    unit = input("Unit / Code : ").strip().upper()
    concern = input("Concern     : ").strip()

    if not unit:
        print("\n✗ Unit / Code cannot be empty.")
        return

    if not concern:
        print("\n✗ Concern cannot be empty.")
        return

    concerns = load_concerns()

    new_concern = {
        "id": len(concerns) + 1,
        "unit": unit,
        "concern": concern,
        "status": "PENDING",
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "completed": None
    }

    concerns.append(new_concern)

    save_concerns(concerns)

    print("\n✓ Concern added.")
    print(f"Unit    : {unit}")
    print(f"Concern : {concern}")
    print(f"Time    : {new_concern['created']}")


def view_concerns():
    """Display all concerns."""

    concerns = load_concerns()

    print("\nCONCERN LIST")
    print("────────────────────────────────────────")

    if not concerns:
        print("No concerns recorded.")
        return

    for item in concerns:
        print(f"\n[{item['id']}] {item['unit']}")
        print(f"    Concern  : {item['concern']}")
        print(f"    Status   : {item['status']}")
        print(f"    Created  : {item['created']}")

        if item["completed"]:
            print(f"    Completed: {item['completed']}")

    print("\n────────────────────────────────────────")


def mark_done():
    """Mark a concern as completed."""

    concerns = load_concerns()

    if not concerns:
        print("\nNo concerns recorded.")
        return

    view_concerns()

    try:
        concern_id = int(input("\nEnter concern ID: "))

    except ValueError:
        print("\n✗ Invalid ID.")
        return

    for item in concerns:

        if item["id"] == concern_id:

            if item["status"] == "DONE":
                print("\n✓ This concern is already marked as DONE.")
                return

            item["status"] = "DONE"
            item["completed"] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            save_concerns(concerns)

            print("\n✓ Concern marked as DONE.")
            print(f"Unit      : {item['unit']}")
            print(f"Completed : {item['completed']}")

            return

    print("\n✗ Concern ID not found.")


def delete_concern():
    """Delete a concern."""

    concerns = load_concerns()

    if not concerns:
        print("\nNo concerns recorded.")
        return

    view_concerns()

    try:
        concern_id = int(input("\nEnter concern ID to delete: "))

    except ValueError:
        print("\n✗ Invalid ID.")
        return

    for item in concerns:

        if item["id"] == concern_id:

            concerns.remove(item)

            save_concerns(concerns)

            print("\n✓ Concern deleted.")
            return

    print("\n✗ Concern ID not found.")


def concern_tracker():
    """Main concern tracker menu."""

    while True:

        print()
        print("╔══════════════════════════════════════╗")
        print("║          CONCERN TRACKER             ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Add Concern                     ║")
        print("║  2. View Concerns                   ║")
        print("║  3. Mark as Done                    ║")
        print("║  4. Delete Concern                  ║")
        print("║  5. Back                             ║")
        print("╚══════════════════════════════════════╝")

        choice = input("\nSelect: ").strip()

        if choice == "1":
            add_concern()

        elif choice == "2":
            view_concerns()

        elif choice == "3":
            mark_done()

        elif choice == "4":
            delete_concern()

        elif choice == "5":
            break

        else:
            print("\n✗ Invalid selection.")