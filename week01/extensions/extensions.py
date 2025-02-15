
filename = input("File name: ")
new_filename = filename.lower().strip()

if (new_filename.endswith(".jpg") | new_filename.endswith(".jpeg")):
    print("image/jpeg")
elif (new_filename.endswith(".gif")):
    print("image/gif")
elif (new_filename.endswith(".png")):
    print("image/png")
elif (new_filename.endswith("pdf")):
    print("application/pdf")
elif (new_filename.endswith("txt")):
    print("text/plain")
elif (new_filename.endswith("zip")):
    print("application/zip")
else:
    print("application/octet-stream")
