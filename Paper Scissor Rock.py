import random

lst = ["p", "s", "r"]
c_points = 0
p_points = 0
name = input("Enter Your Name:")
print("The Match is Between",name,"VS Computer!!")
rounds = int(input("Enter How Many Times you want to play:"))

i = 1
while(i <= rounds):
    print("\'p\' stands for paper, \'s\' stands for scissor and \'r\' stand for rock")
    p_choice = input("Enter Your Choice:")
    c_choice = random.choice(lst)
    print("Computer choose:", c_choice)
    if c_choice == p_choice:
        print("Round is Drawn!!\n")
    elif c_choice == "p" and p_choice == "r":
        print("Computer Win This Round!!")
        c_points += 1
    elif c_choice == "r" and p_choice == "p":
        print(name, "Win This Round!!\n")
        p_points += 1
    elif c_choice == "s" and p_choice == "p":
        print("Computer Win This Round!!\n")
        c_points += 1
    elif c_choice == "p" and p_choice == "s":
        print(name, "Win This Round!!\n")
        p_points += 1
    elif c_choice == "r" and p_choice == "s":
        print("Computer Win This Round!!\n")
        c_points += 1
    elif c_choice == "s" and p_choice == "r":
        print(name, "Win This Round!!\n")
        p_points += 1
    else:
        print("Wrong input!!")
    i = i + 1

if c_points == p_points:
    print("THE SCORE OF COMPUTER IS", c_points)
    print("THE SCORE OF", name, "is", p_points)
    print("***THE MATCH IS TIED***")
elif c_points > p_points:
    print("THE SCORE OF COMPUTER IS", c_points)
    print("THE SCORE OF", name, "IS", p_points)
    print("***COMPUTER WIN THE SERIES OF ALL ROUND***")
elif c_points < p_points:
    print("THE SCORE OF COMPUTER IS", c_points)
    print("THE SCORE OF", name, "IS", p_points)
    print("***", name, "WIN THE SERIES OF ALL ROUNDS***")
