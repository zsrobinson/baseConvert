types = ["int", "bin", "hex", "oct"]

while True:
	print("------------------------------\n")
	print(f"Data types: {', '.join(types)} \n")

	a = input("From  : ").lower()
	b = input("To    : ").lower()
	num = input("Num   : ").lower()

	# input to binary
	if a == "int":
		temp = bin(int(num))
	elif a == "bin":
		temp = bin(int(num, 2))
	elif a == "hex":
		temp = bin(int(num, 16))
	elif a == "oct":
		temp = bin(int(num, 8))
	else:
		print("\nERROR: 'To' value not recognized")
	
	if b == "int":
		output = str( int(temp, 2))
	elif b == "bin":
		output = str( temp.replace("0b", ""))
	elif b == "hex":
		output = str( hex(int(temp, 2)).replace("0x", ""))
	elif b == "oct":
		output = str( oct(int(temp, 2)).replace("0o", ""))
	else:
		print("\nERROR: 'From' value not recognized")
	
	print(f"\nResult: {output}\n")