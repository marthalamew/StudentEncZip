#All the imports
import random
import hashlib
import subprocess
import string
from functools import partial
#Opens the files and is able to read each line individually
lines = open('rockyou.txt', encoding = "ISO-8859-1").read().splitlines()
student = open('student.txt', encoding = "ISO-8859-1").read().splitlines()
#For each Student iin the student list
for name in student:
	#Creates the name for the student file
	x=name+".txt"
	#Creates the password for the encrypted zip file
	zippass=''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
	#Writes the string to the current student .txt file
	with open(x,"a") as stu:
		stu.write(name+" This is a list of hashes you need to crack, I will talk more about this in class on Wed" '\n')
	#Writes the current student name to the master list
	with open("master.txt","a") as mast:
		mast.write(name+" :\n")
	#For each random password from rockyou.txt file
	for j in range(10):
		#Grabs a random line(password) from the rockyou.txt file
		myline=random.choice(lines)
		###print(myline)
		#m is equal to the random password
		m=myline
		#Writes the random password to the masterfile
		with open("master.txt","a") as mast:
			mast.write(m+"\n")
		#hashs the password 10 times
		for i in range(10):
			m=hashlib.md5(m.encode("utf")).hexdigest()
		###print(m)
		#Hashes the 10 md5 hashes with 10 sha1
		for i in range(10):
			m=hashlib.sha1(m.encode("utf")).hexdigest()
		###print(m)
		#Hashes the 10 md5 hashes with 10 sha512
		for i in range(10):
			m=hashlib.sha512(m.encode("utf")).hexdigest()
		#writes the final hash to the master file
		with open("master.txt","a") as mast:
			mast.write(str(j+1) + ': '+ m + '\n')
		#Prints the hash to the screen
		###print(m)
		#Writes the number of the hash (1 through 10) and then the hash to the current student's .txt file
		with open(x,"a") as stu:
			stu.write(str(j+1) + ': '+ m + '\n')
	#After all the 10 hashes have been written to the master.txt file then the zip password is added
	with open("master.txt","a") as mast:
		mast.write('+++++++++++\n'+zippass+'\n+++++++++++\n\n\n\n')
	#prepares for the system call
	password = "-P"+zippass
	zipper = name+".zip"
	#Command that creates the encrypted hash
	subprocess.call(["zip", "-e", password, zipper, x])