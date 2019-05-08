import random 
import time 
#Print some super fancy looking ASCII art on the Console
print("""
    _____                                    _  _____            
    |  __ \                                  | |/ ____|           
    | |__) |_ _ ___ _____      _____  _ __ __| | |  __  ___ _ __  
    |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` | | |_ |/ _ \ '_ \ 
    | |  | (_| \__ \__ \\ V  V / (_) | | | (_| | |__| |  __/ | | |
    |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|\_____|\___|_| |_|
    """)

#get Input from user in a function so callable as often as wanted later on
def getInput():
    #define desiredStrength as global variable to be accessed by value check 
    #later on 
    global desStrength
    #get actual input from user
    desStrength = input("""

Enter your desired password strength 

[1] chain
[2] vault
[3] fortress

> """)

#Call function once 
getInput()


#Only if user input is a number, repeat
if desStrength.isnumeric()==True:
    
    #Give user some infos about their password strength
    print('Desired strenth is '+desStrength+'/3')
    #Some 'UX'
    time.sleep(0.25)
    #As input is a number, transform desStrength to int without getting error
    desStrength = int(desStrength)
    if desStrength==1:
        print('PasswordGen will generate a strong 16-digit password...')
    elif desStrength ==2:
        print('PasswordGen will generate a strong 32-digit password...')
    elif desStrength ==3:
        print('PasswordGen will generate a strong 64-digit password...')
#If input wasn't a number, repeat process      
else:
    print('Please enter a number')
    getInput()
    
#Charset with 92 entries to pick random numbers from 
charset = '#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

#Empty list for later password
password=[]

#picking a random number from the charset
#What do i need to do? 
#Get 16 random numbers out of the charset
#Get 32 random numbers out of the charset
#Get 64 random numbers out of the charset 
#With each iteration choosing new
if desStrength==1:
    #Do the loop 16 times 
    for i in range(0,16):
        #Take a random choice out of the charset and append to empty pw list
        password.append(random.choice(charset))

if desStrength==2:
    #Do the loop 32 times 
    for i in range(0,32):
        #Take a random choice out of the charset and append to empty pw list
        password.append(random.choice(charset))
        
if desStrength==3:
    #Do the loop 64 times 
    for i in range(0,64):
        #Take a random choice out of the charset and append to empty pw list
        password.append(random.choice(charset))

#transform list elements to str, take empty string and join with list elementss
strPassword = ''.join(password)

#Some 'UX'
time.sleep(2)
#Return the password to user
print('Here is your desired strong password :\n'+strPassword)


