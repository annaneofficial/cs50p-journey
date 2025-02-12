def replace_spaces_with_dots(msg):
    newmsg = ""
    for char in msg:
        if char == " ":
            newmsg += "..."
        else:
            newmsg += char
    return newmsg

def main():
    msg = input()
    result = replace_spaces_with_dots(msg)
    print(result)

main()

