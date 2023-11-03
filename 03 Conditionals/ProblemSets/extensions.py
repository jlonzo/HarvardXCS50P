def main():
    file = input("Filename: ").strip()
    if file.rfind(".") > 0:
        #fname,ext = file.split('.')
        ext = file[file.rfind(".")+1:]
    else:
        ext=""
    eval_filetype(ext.lower())

def eval_filetype(f):
    match f:
        case "gif" | "png":
            print("image/",f,sep='')
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "txt":
            print ("text/plain")
        case "pdf" | "zip":
            print("application/",f,sep='')
        case _:
            print("application/octet-stream")

main()