def trim(str):
    if str == " ":
        return str
    while str[0] == " ":
        str = str[1:]
    while str[-1] == " ":
        str = str[:-1]
    return str
print("*",trim("   123   "),"*")
print(len(trim("   123   ")))