import csv

def searchByDescription():
	name=input("Enter Description: ")
	csv_file=csv.reader(open("survey2018.csv","r"))

	for row in csv_file:
		if name==row[0]:
			print(row)

def searchByIndustry():
	name=input("Enter Industry Name: ")
	csv_file=csv.reader(open("survey2018.csv","r"))

	for row in csv_file:
		if name in row[1]:
			print(row)

def searchByLevel():
	level=input("Enter Level Number: ")
	csv_file=csv.reader(open("survey2018.csv","r"))

	for row in csv_file:
		if level in row[2]:
			print(row)
		
def searchBySize():
	size=input("Enter Size: ")
	csv_file=csv.reader(open("survey2018.csv","r"))

	for row in csv_file:
		if size in row[3]:
			print(row)

def searchByLine_code():
	code=input("Enter Line_code: ")
	csv_file=csv.reader(open("survey2018.csv","r"))

	for row in csv_file:
		if code in row[4]:
			print(row)

def searchByValue():
	value=input("Enter Value: ")
	csv_file=csv.reader(open("survey2018.csv","r"))

	for row in csv_file:
		if value in row[5]:
			print(row)

print("Enter 1 Search By Description: ")
print("Enter 2 Search By Industry: ")
print("Enter 3 Search By Level: ")
print("Enter 4 Search By Size: ")
print("Enter 5 Search By Line_code: ")
print("Enter 6 Search By value: ")

src=int(input("Enter Your Chosen Number: "))

if src==1:
	searchByDescription()
elif src==2:
	searchByIndustry()
elif src==3:
	searchByLevel()	
elif src==4:
	searchBySize()
elif src==5:
	searchByLine_code()	
elif src==6:
	searchByValue()			
else:
	print("Enter Invalid Number")
	        