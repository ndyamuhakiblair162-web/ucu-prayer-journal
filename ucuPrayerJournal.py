"""
The project is a Prayer Journal Application for UCU.

"""

#Placeholder information for login.
name = "John Doe"
accessnumber = "A00000"
registrationnumber = "S26B1/000"
sex = "M"
age = 18
password = 1234
studentinformation = list((name, accessnumber, registrationnumber, sex, age, password))

#Assigning variables
trials = 2
attempts = 3
#Pre-assigning varibles to be assigned later.
mood = 0 
good_feeling = 0
bad_feeling = 0
random_number = vars
random_verse = vars

print(" ") #This is just to nicely space the code in the Terminal.
#Start of the programme.
print(f"🛐Welcome, to the UCU PRAYER JOURNAL🛐")

#Demonstration of while and for loop
print(" ")
print("Would you like to:\n1.Login \n2.Create a new account")
login_status = input()

#Match is like a stronger version of nested ifs.
match login_status:
    case "1":
        print(" ")
        while trials <= 3:
            entered_password = int(input("Enter your password:"))
            if entered_password == password:
                break
            elif trials > 0 and entered_password != password:
                trials -= 1
                attempts -= 1
                print(f"Incorrect password! You have {attempts} more attempt(s).")
            elif trials <= 3 and entered_password != password:
                print("It seems you are having troubles logging in. Please create an account.")
                continue          

    case "2":
        print(" ")
        print("Please enter...")

        #Variables and Input

        print("Your Name:")
        name = input()
        print("Your Acess Number:")
        accessnumber = input()
        print("Your Registration Number:")
        registrationnumber = input()
        print("Your Age:")
        age = int(input())
        print("Your sex:")
        sex = input() #Only M or F
        print("Create a password:")
        password = input()
        studentinformation = list((name, accessnumber, registrationnumber, sex, age, password))
    case _:
        print(" ")
        print("It seems you are having troubles logging in. Please create an account.")
        print("Please enter...")
        
        #Variables and Input fo the case neither 1 or 2 is the input

        print("Your Name:")
        name = input()
        print("Your Acess Number:")
        accessnumber = input()
        print("Your Registration Number:")
        registrationnumber = input()
        print("Your Age:")
        age = int(input())
        print("Your sex:")
        sex = input() #Only M or F
        print("Create a password:")
        password = input()
        studentinformation = list((name, accessnumber, registrationnumber, sex, age, password))

#Miscellaneous || Imports information from your system
from datetime import date
today = date.today()

import random

#Lists
prayer_request_contacts = ["01234567", "07654321"]

encouragement = ["You're chosen.", "You're not alone.", "He died for you."]

joyful_bible_verses = ["1Peter 1:8(Be joyful in hope, patient in affliction, faithful in prayer.)", "1Thessalonians 5:16(For the kingdom of God is not a matter of eating and drinking,but of righteousness, peace and joy in the Holy Spirit.)"]
peaceful_bible_verses = ["John 14:26(Peace I leave with you, my peace I give unto you: not as the world giveth, give I unto you. Let not your heart be troubled...)", "Matthew 11:28(But the fruits of the Spirit is love, joy, peace longsuffering, gentleness, goodness, faith, meekness, temperance...)"]
depression_bible_verses = ["Pslams 34:18(The LORD  is near to the brokenhearted and saves the crushed in spirit.)", "Psalms 43:5(Why are you cast down, O my soul, and why are you in turmoil within me? Hope in God; for I shall again praise Him, my salvation and my God.)"]
anxious_bible_verses = ["Psalms 23 (The LORD is my shepherd, I shall not want...Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me...)", "Daniel 3:17(...God whom we serve is able to deliver us from the burning fiery furnace...)"]

#Functions
def relevant_scripture():
    match mood:
        case "1":
            if good_feeling == 1:
                return random.choice(joyful_bible_verses)
            elif good_feeling == 2:
                return random.choice(peaceful_bible_verses)
        
        case "2":
            if bad_feeling == 1:
                return random.choice(depression_bible_verses)
            elif bad_feeling == 2:
                return random.choice(anxious_bible_verses)

def enocouraging_words():
    return random.choice(encouragement)

print(" ")
#Now we get input to compose the Journal.
print(f"{name}, how are you doing today? \n1.Good Mood \n2.Bad Mood")
mood = input()

match mood:
    case "1":
        print("Glad to hear! How are you feeling? \n1.Joyful \n2.Peaceful")
        good_feeling = int(input())
    case "2":
        print(f"Sorry to hear that, {name}... How are you feeling? \n1.Depressed \n2.Anxious")
        bad_feeling = int(input())
    case _:
        print("INVALID INPUT")

print(" ")
#Demonstration of nested ifs.
print("Would you like to share what happened? \n1.yes \n2.no")
share = int(input())

if share == 1:
    print("Type down what happened. Press 'Enter' when you're done.")
    journal_entry = str(input())

elif share == 2:
    journal_entry = "NIL"
    print("I understand.")

else:
    if share < 1 or share > 2 or share != int:
        print("INVALID INPUT")


print(" ")
print("Would you like someone to pray for you? \n1.yes \n2.no")
prayer_request = int(input())

if prayer_request == 1:
    print("Here are some numbers you can call:")
    print(prayer_request_contacts)

elif prayer_request == 2:
    print("I understand. Don't be scared to put in a prayer request when you need it, though.")

else:
    if prayer_request < 1 or prayer_request > 2 or prayer_request != int:
        print("INVALID INPUT")


#Actual Journal Entry based on information gathered.

print(" ")
print(" ")
print(" ")

print("✝️   ✝️   ✝️")
print(today.strftime("%B %d, %Y"))
print("Dear God...")
if mood == "1":
    print("Today, I was in a good mood.")
    if good_feeling == 1:
        print("I'm joyful because...")

    elif good_feeling == 2:
        print("I'm at peace because...")


elif mood == "2":
   print("Today, could have gone better...")
   if bad_feeling == 1:
        print("I'm feeling depressed because...")
   
   elif bad_feeling == 2:
        print("I'm anxious because...")

    
print(journal_entry)

print("The Bible says:")
print(relevant_scripture()) #Bring back the verse accoriding to mood and feeling. This is randomised.


print("✝️   ✝️   ✝️")
print(" ")
print(enocouraging_words()) #Function for random generation of encouraging words.

