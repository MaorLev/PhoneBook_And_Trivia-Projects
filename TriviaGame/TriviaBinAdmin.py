# TriviaBinAdmun
import pickle


def main():
    for k in range(3):
        mode = input('To New game press 0, to Add Asks press 1 : ')
        if mode < '0' or mode > '1':
            print("Input Error")
        else:
            AddAsk(mode)
            break
    print(" Bye ")

def AddAsk(mode):
    #  פתיחת  קובץ
    F = None
    for k in range(3):
        try:
            fname = input('Enter FileName of Game : ')
            F = open(fname, 'ab+')
        except:
            print(" Open or FileName  Error ")
        else:
            break
    if F == None:
        print("Fatal Error ")
        exit()

    # הכנה לקליטת שאלות
    if mode == '1':
        F.seek(0, 0)
        List = pickle.load(F)
        print(List)  # תצוגה לאחר קריאה מקובץ - לבדיקה בלבד
        F.close()
        F = open(fname, 'wb+')
    else:
        List = []

    # קליטת  שאלות
    flag = '1'
    while flag == '1':
        temp = []
        temp.append(input('Enter Ask : '))
        for k in range(1, 5):
            temp.append(input('Enter Answer %d : ' % (k)))
        while 1:
            ans = input('Enter number of True Answer (1,2,3,4) : ')
            if ans > '0' and ans < '5':
                break
        temp.append(ans)
        List.append(temp)
        print('To continue press 1 and ENTER other press ENTER : ')
        flag = input()

    #  שמירה  בקובץ
    pickle.dump(List, F)
    F.close()


main()
