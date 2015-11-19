class DHKE:
    B = input("What did you get from your contact? ")
    p = input("What is your shared second prime? ")
    a = input("What is your secret prime? ")
    s = B ** a % p
    print("Share this with your contact: " + str(s))
