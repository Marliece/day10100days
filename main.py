myBill = float(input("What was the bill?: "))
tip = int(input("What % of tip will you leave?: "))
addedTip = myBill * (tip/100)
numberOfPeople = int(input("How many people?: "))
total = myBill + addedTip
answer = total / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
