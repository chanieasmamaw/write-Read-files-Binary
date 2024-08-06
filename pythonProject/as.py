def is_substring(small, big):
    return small in big
try:
    print(is_substring("", "hey"))
    if not "":
        raise Exception("The string must not empty")
    print(is_substring("h", "hey"))
except Exception as e:
    print(f"{e}")

