#This is a Zip-file password cracker script 
#import module zipfile in order to access the zip file 
#import module tqdm to create a progress bar
import zipfile
from tqdm import tqdm
import os
#ask user to imput the exact location of the zip file 
user_file_input=input("Enter the full path of your zip file: ")
user_dict_input=input("Enter the full path of your dictionary file: ")
valid_file=os.path.exists(user_file_input)
valid_file2=os.path.exists(user_dict_input) 
try:
  valid_file==True
  valid_file2==True
  zfile=zipfile.ZipFile(user_file_input)
#Create a string call password and assign the dictionary to this string 
  password=(user_dict_input) # 'rb')
#create a new string call n_password to get the number of passwords in the dictionary file 
#Need to open the file to count the passwords
  n_password=len(list(open(password,'rb')))
  print(f'The total number of password to crack is: {n_password}')
#Read the password file in a binary format 
#for each_word in the password file otain the password itself and its position)
  with open(password,'rb') as password:
    for word in tqdm(password,total=n_password, unit="word"):
    #exception handling, strip any space from the passoword 
      try:
        zfile.extractall(pwd=word.strip())
    #if there is any error, continue 
      except:
        continue
    #if there is no error, print the password 
      else:
        print("Password Found")
      #the password is in a binary format hence it needs to be decoded and strip any spaces 
        print("The password is:", word.decode().strip())
except FileNotFoundError:
  print("No such file or directory")
except Exception as e:
  print(e)




#for word in password.readlines():
  #try:
    #zfile.extractall(pwd=word.strip())
  #except:
    #continue
  #else:
    #print(f"[+] Password Found")]

 # Print(f'The correct password is: {word})
  
  #Exception as e:
     #print(e)
   #print (password)
#must use b before the password strings for encoding 
#use the below exception handling for bad password 

