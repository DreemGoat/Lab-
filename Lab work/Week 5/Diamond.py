def diamond():
    z=(int(input("Enter number: ")))
    height=2*z
    for i in range (height):
	    if(i<=z):
		    print(" " * (height-i-z), end="")
		    print("*" * (i*2-1), end="")
	    else:
		    print(" " * (i-z), end="")
		    print("*" * ((height-i)*2-1), end="")
	    print()
diamond()