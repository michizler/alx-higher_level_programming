def uppercase(str):
    for char in str:
        if (ord(char) in range(65, 91)) or (ord(char) not in range(97, 123)):
            print(f"{char}", end="")
        else:
            char_low = chr((ord(char) - 32))
            print(f"{char_low}", end="")
    print("")
