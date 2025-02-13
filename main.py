import esimene as esimeneFail
import teine as teineFail
import kolmas as kolmasFail

userInput = input("Milline ülesanne sa tähad ülevadata")
if userInput == "1":
    esimeneFail.myFunc()
elif userInput == "2":
    teineFail.myPykkar()
else:
    print("dddddd")