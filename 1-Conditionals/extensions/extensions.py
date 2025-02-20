extension = input("file name: ")

name, filetype = extension.split(".")
match filetype:
    case "gif" | "jpeg" | "jpg" | "png":
        print (f"image/{filetype}")
    case "pdf" | "txt" | "zip":
        print (f"application/{filetype}")
    case _:
        print ("application/octet-stream")
