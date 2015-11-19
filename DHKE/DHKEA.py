class DHKE:
    g = input("What is your shared base prime? ")
    p = input("What is your shared second prime? ")
    a = input("What is your secret prime? ")
    A = g ** a % p
    print(A)
