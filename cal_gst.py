ppb=499.00
plb=855.00
dsb=645.00
del_price=250.00
a=int(input("Enter no of python_Programming_Books you want:"))
b=int(input("Enter no of python_Libraries_Books you want:"))
c=int(input("Enter no of data_Science_Books you want:"))
tot=(ppb*a)+(plb*b)+(dsb*c)
gst=(tot/100)*12
net_price=tot+gst+del_price
print(net_price)
