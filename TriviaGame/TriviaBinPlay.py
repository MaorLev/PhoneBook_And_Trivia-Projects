# TriviaBinPlay
import pickle
import random


def GameBinData():
    #  פתיחת  קובץ
    F = None
    for k in range(3):
        try:
            fname = input('Enter FileName of Game : ')
            F = open(fname, 'rb')
        except:
            print(" Open or FileName  Error ")
        else:
            break
        finally:
            if F == None:
                print("Fatal Error ")
                exit()

    List = pickle.load(F)
    print(List)
    F.close()
    return List


def GameBinPlay(List):
    listRnd = list()
    wins = 0
    again = True
    while again:
        rnd = str(random.randint(0,len(List)-1))
        if rnd not in listRnd:
            answers = List[int(rnd)][1:len(List[int(rnd)])-1]
            trueAns = int(List[int(rnd)][len(List[int(rnd)])-1])
            ques = List[int(rnd)][0]
        elif len(listRnd) == len(List):
            again = False
            print("\nThe questions are over.\nThank you for play!")
            break
        else:
            continue
        print("Answer the question : " + ques)
        for k in range(len(answers)):
            print( str(k+1) + " :" + "  " + answers[k] + "\n")
        try:
            userAns = int(input("choose and enter number of your answer from above options : "))
            if userAns > 4 or userAns < 0:
                raise  ValueError
        except ValueError:
            print("\nEnter only above number!!\n")
            continue
        if userAns == trueAns:
            wins += 1
            print("\ncongralations you right")
        else:
            print("\nWrong answer\n")
        print("RIGHT ANSWERS : " + str(wins)+"\n")
        again = input("For continue to next question enter 'y',\nfor exit enter any key :") == "y"
        listRnd.append(rnd)

def main():
    List = GameBinData()
    if len(List) > 0:
        GameBinPlay(List)
    print(" Bye ")


main()
#C:\Users\97250\Desktop\Newfolder\triviaAdmin.dat
# טיפולים נדרשים : טיפול חריגה של בחירת התשובה לשאלה
#טיפול בכתב וברווח