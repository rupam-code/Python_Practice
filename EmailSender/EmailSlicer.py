def main():
    print("Welcome to the Email Slicer")
    print("")

    email_input=input("Input your email address::")

    (username,domain) =email_input.split("@")
    (domain,extention) = domain.split(".")

    print("UserName ::",username)
    print("Domain::",domain)
    print("Extension::",extention)

main()
