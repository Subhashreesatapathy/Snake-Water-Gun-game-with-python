import random
def game(comp,you):
    if comp==you:#tie
      return None
    elif comp=="s":
        if you=="w":
           return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
         return False
        elif you =="w":
            return True
print("computer  turn : snake(s) water(w) or gun(g) ?")#comp choice
randno=random.randint(1,3)#random module it generate random number its range is 1 to 3
#print(randno) you can know which num is generated
if randno==1:
    comp="s"
elif randno==2:
    comp="w"
elif randno==3:
    comp="g"

you = input("Your turn : snake(s) water(w) or gun(g) ?")#user choice
a=game(comp,you)
print(f"comp chose:{comp}")
print(f"you chose:{you}")

if a==None:
    print(" IT'S A TIE !!")
elif a :
    print("YOU WIN !!")
else:
    print("YOU LOSE!")
