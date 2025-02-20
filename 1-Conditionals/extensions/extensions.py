extension = input("file name: ")

name, filetype = extension.split(".")
filetype = filetype.lower()
match filetype:
    case "gif" | "jpeg" | "jpg" | "png":
        print (f"image/{filetype}")
    case "pdf" | "txt" | "zip":
        print (f"application/{filetype}")
    case _:
        print ("application/octet-stream")
