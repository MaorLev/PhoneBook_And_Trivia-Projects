#MaorLevy

phonebook = dict()
#1
def addContact():
    name = input("enter name : ")
    phone = input("enter phone : ")
    phonebook[name] = phone

#2
def showbook ():
    for key, value in phonebook.items():
        print(key,value)

#3
def newPhoneBook():
    y = "y"
    phonebook.clear()
    while y == "y":
        addContact()
        y = input("if you want to add one more contact enter 'y', otherwise enter any char")
    showbook()
#6
def searchByName():
    name = input("enter name so you want to find")
    for key, value in phonebook.items():
        if key == name:
            print(key,value)
#7
def searchByPhone():
    phone = input("enter phone so you want to find")
    for key, value in phonebook.items():
        if value == phone:
            print(key,value)

#8
def updatePhone():
    name = input("enter name to find contact and update")
    print(phonebook[name])
    phone = input("enter phone to update")
    ques = input("are you sure? enter: yes/no")
    if ques == "yes" :
        phonebook[name] = phone
#9
def removeContact():
    name = input("enter contact name so you want to remove")
    for key, value in phonebook.items():
        if key == name:
            print(key,value)
    ques = input("are you sure? enter: yes/no")
    if ques == "yes" :
        del phonebook[name]
#10
def cleanPhonebook():
    ques = input("are you sure? enter: yes/no")
    if ques == "yes":
        phonebook.clear()

#4
def main():
    act = int(input("enter your action from this menu\n,"
                    "0. show menu \n"
                    "1. create new phonebook\n"
                    "2. show all contact from phonebook\n"
                    "3. add new contact\n"
                    "4. search into the phonebook by name\n"
                    "5. search into the phonebook by phone\n"
                    "6. update phone from the phonebook\n"
                    "7. remove specific contact\n"
                    "8. remove this phonebook\n"
                    "9. finish this program\n"))
    while act != 9:
        if act == 0 :
            print("enter your action from this menu\n,"
                    "0. show menu \n"
                    "1. create new phonebook\n"
                    "2. show all contact from phonebook\n"
                    "3. add new contact\n"
                    "4. search into the phonebook by name\n"
                    "5. search into the phonebook by phone\n"
                    "6. update phone from the phonebook\n"
                    "7. remove specific contact\n"
                    "8. remove this phonebook\n"
                    "9. finish this program\n")
        elif act == 1 :
            newPhoneBook()
        elif act == 2 :
            showbook()
        elif act == 3 :
            addContact()
        elif act == 4 :
            searchByName()
        elif act == 5 :
            searchByPhone()
        elif act == 6 :
            updatePhone()
        elif act == 7 :
            removeContact()
        elif act == 8 :
            cleanPhonebook()
        act = int(input("choose action, press '0' for menu"))

main()










