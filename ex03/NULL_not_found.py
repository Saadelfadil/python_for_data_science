def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
        return 0
    elif isinstance(object, float) and object != object:  # Check for NaN
        print(f"Cheese: {object} <class 'float'>")
        return 0
    elif isinstance(object, bool):
        print(f"Fake: {object} <class 'bool'>")
        return 0
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} <class 'int'>")
        return 0
    elif isinstance(object, str):
        if object == "":
            print(f"Empty: {object} <class 'str'>")
            return 0
        else:
            print("Type not found")
            return 1
    else:
        print("Type not found")
        return 2