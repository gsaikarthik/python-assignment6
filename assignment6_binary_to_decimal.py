print("enter x for exit")
binary=input("enter a number in binary code:")
if binary=='x':
    exit()
else:
    decimal=int(binary,2)
    print(binary,"in desimal",decimal)