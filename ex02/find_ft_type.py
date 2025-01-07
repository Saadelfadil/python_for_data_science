def all_thing_is_obj(object: any) -> int:
    obj_type = type(object)
    if obj_type == list:
        print("List : <class 'list'>")
    elif obj_type == tuple:
        print("Tuple : <class 'tuple'>")
    elif obj_type == set:
        print("Set : <class 'set'>")
    elif obj_type == dict:
        print("Dict : <class 'dict'>")
    elif obj_type == str:
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")

    return 42
