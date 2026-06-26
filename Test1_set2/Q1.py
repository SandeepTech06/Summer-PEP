dct = {
    "student": {
        "name": "John",
        "rollNo.": "10",
        "class": "1st"
    },
    "teacher": {
        "school": "xyz school"
    }
}

def get_dict_value(dct, path):
    keys = path.split(".")

    for key in keys:
        if key in dct:
            dct = dct[key]
        else:
            return None
    return dct

print(get_dict_value(dct, "student.name"))
print(get_dict_value(dct, "teacher.school"))
print(get_dict_value(dct, "teacher.rollNo."))












