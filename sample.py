import sys
x = 1
fo1=0
import time
intro = "You are in the Kingdom of Dragons. In front of you, you see two caves In one cave, the dragon is friendly and will share his treasure with you. The other dragon is hungry and will eat you on sight!"

print(intro)
while x==1:
    cave  = (input("\nSelect cave 1,2,3,4 and 5:"))
    if cave.isnumeric() and int(cave) in (1,2,3,4,5):
        import random
        time.sleep(1)
        print("\nYou have approach the cave...")
        time.sleep(2)
        print("A large dragon jumps out in front of you!")
        time.sleep(2)
        print("He opens his jaws and...")
        time.sleep(3)
        string = ["gobbles you down","Greats you with his treasure"]
        random.shuffle(string)
        print(string[0])
        cont=input("\nDo you want to play? (y/n):")
        if cont =="y":
            continue
        else:
            if cont =="n":
                break
        break

fo = sys.stdout
fo1 ="DragonGame.txt"
with open(fo1,"w") as file:
    sys.stdout = file
sys.stdout = fo

print(fo1)

