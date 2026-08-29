from mappings import BUILDING_VALUES, STATIC_MAP


def convert_ppoe(code):
    code = code.strip().upper()

    if len(code) < 3:
        raise ValueError("Invalid code.")

    building = code[0]

    if building not in BUILDING_VALUES:
        raise ValueError(f"Unknown building: {building}")

    numbers = code[1:]

    if not numbers.isdigit():
        raise ValueError("The code must contain numbers after the building.")

    floor = int(numbers[:-2])
    unit = int(numbers[-2:])

    return f"10.{BUILDING_VALUES[building]}.{floor}.{unit}"


def convert_static(code):
    code = code.strip().upper()

    if len(code) < 5:
        raise ValueError("Invalid static code. Example: K1515")

    building = code[0]
    numbers = code[1:]

    if building not in STATIC_MAP:
        raise ValueError(f"Unknown static building: {building}")

    if not numbers.isdigit():
        raise ValueError("The code must contain numbers after the building.")

    # First part = floor
    # Last two digits = host/unit
    floor = int(numbers[:-2])
    host = int(numbers[-2:])

    if floor < 2 or floor > 17:
        raise ValueError("Floor must be between 2 and 17.")

    third_octet = STATIC_MAP[building][floor]

    return f"172.18.{third_octet}.{host}", floor, host