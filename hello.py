def main():
	#input
	print ("Whats your name?")
	name = input()
	print (f"Hello, {name}")

	#set
	s = set()
	s.add(1)
	s.add(3)
	s.add(5)
	#s.add(3)
	print (s)

	#dictionary
	ages = {"Bob":20, "Alice":30}
	ages["Charlie"] = 45
	ages["Alice"] +=1
	print(ages)
	
	for i in range(20):
		print(f"{i} squared is {square(i)}")

	#function
def square(x):
	return x*x

if __name__ == "__main__":
	main()
