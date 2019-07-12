def funkcja(dict1, dict2):
    if set(dict1.keys()) == set(dict2.keys()):
        return True
    else:
        return False


s1 = {"a": 2, "b": 3, "c": 5}
s2 = {"a": 8, "b": 4, "c": 1}
s3 = {"a": 8, "b": 4, "c": 1, "d": -2}
print(funkcja(s1, s2))
print(funkcja(s1, s3))
print(funkcja(s2, s3))
