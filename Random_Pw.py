import random
import string
import time
import os

alphabet = set(string.ascii_lowercase + string.ascii_uppercase)
digits = set(string.digits)
rand_pw = ""
print("Welcome to auto password creator...\n")

def func():
    leng = int(input("How many characters do you need for this password? "))
    return leng
leng = func()


while True:    
    if leng < 6:
        print("With " + str(leng) +" characters password will be too weak, please increase the length of the password.")
        #func()
        leng = func()
    else:
        break
    

site_name = input("\nPlease type the site/system name: ")

pw_date = input("\nPlease type the date ('yyyy-mm-dd'): ")

for i in range(0,leng):
    
    if i == 1 or i == 4:
        rand_c = random.sample(digits, 1)
    else:
        rand_c = random.sample(alphabet, 1)
    rand_c = str(rand_c[0])
    rand_pw = rand_pw + rand_c
  
path = os.path.expanduser("~/Desktop\\Rand_Pw.txt")
  
with open(path, mode ="a") as f:
        f.write(f"{site_name}  |  {pw_date}  |  {rand_pw}")
        f.write("\n")
        
print(f"Your random password has been created for {site_name}. You may find your password at the output file.")
time.sleep(5)
        

