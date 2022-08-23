#!/usr/bin/python3
for n in range(0, 100):
    if n < 10:
        print(f"0{n}, ", end="")
    else:
         if n == (100-1):
            print(f"{n}")
        else:
            print(f"{n}, ", end=", ")
