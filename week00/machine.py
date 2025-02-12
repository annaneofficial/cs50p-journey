emoticon = " V.V"

def main():
    global emoticon
    say("Is anyone there!")
    emoticon = ":D"
    say("Yeah, Hello How are You")


def say(phrase):
    print(phrase + "" + emoticon)

main()
