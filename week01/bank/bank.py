text = input("Greeting: ")
new_text = text.lower().strip()

if "hello" in new_text:
    print("$0")
elif "h" in new_text[0]:
    print("$20")
else:
    print("$100")
