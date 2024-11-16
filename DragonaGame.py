
x = 0
fo = 0
import random

intro = ("You are in the Kingdom of Dragons.\nIn front of you, you see two caves.\nIn one cave, the dragon is friendly and\nwill share his treasure with you.\nThe other dragon is hungry and will eat you on sight!")
print(intro)
while x==0:
    import time
    cave  = input("\nEnter the cave 1,2,3,4 and 5 :")
    if cave.isnumeric() and int(cave)  in (1,2,3,4,5):
        time.sleep(1)
        a=print("you approach the cave...")
        time.sleep(1)
        b=print("A large dragon jumps out in front of you")
        time.sleep(1)
        c=print("He opens his jaws and...")
        time.sleep(2)
        more =["Gobbles you down","Greets you before share his treasure"]
        random.shuffle(more)
        print(more[0])
        cont =input("do you want to play? [y/n]:")
        if cont == "y":
            continue
        else:
            if cont =="n":
                break
            break

with open ("DragonGame.txt","w") as fo:
    fo.write(intro)
    fo.write(cave)
    fo.write(cont)
    fo.close()
