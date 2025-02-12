def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

def main():
    msg = input()
    res = convert(msg)
    print(res)

main()

