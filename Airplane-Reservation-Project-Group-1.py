#Group 1 - Panther Programmers
#Member: Stefano Johan, Jennifer Gracia, Amera Greer
#CISPROG-1-04957
# May 21, 2019
print("Welcome to Panther Programmer Airline Ticketing System.")
print("Created by Stefano Johan, Jennifer Gracia, Amera Greer.")
admin = input("Admin login name: ") #to mention admin name when quit

#array
vip1 = [["   [Open]    "], ["   [Open]    "]]
vip2 = [["   [Open]    "], ["   [Open]    "]]
vip3 = [["   [Open]    "], ["   [Open]    "]]
vip4 = [["   [Open]    "], ["   [Open]    "]]
reg1 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg2 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg3 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg4 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg5 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg6 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg7 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg8 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg9 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]
reg10 = [["  [Open]    "], ["  [Open]    "], ["  [Open]    "],["  [Open]    "]]


def map():
    vip = ["#"], [" ===A===  "], ["   ===B===   "]
    reg = ["#"], [" ===A===  "], ["  ===B===   "], ["  ===C===   "], ["  ===D===   "]
    print(
        "==============================*First Class*=================================="
    )
    print(vip)
    print("[1]", vip1)
    print("[2]", vip2)
    print("[3]", vip3)
    print("[4]", vip4)
    print(
        "============================================================================="
    )
    print(
        "==============================*Coach Class*=================================="
    )

    print(reg)
    print("[01]", reg1)
    print("[02]", reg2)
    print("[03]", reg3)
    print("[04]", reg4)
    print("[05]", reg5)
    print("[06]", reg6)
    print("[07]", reg7)
    print("[08]", reg8)
    print("[09]", reg9)
    print("[10]", reg10)
    print(
        "============================================================================="
    )

def seatvip(): #main array formula for First Class
    name = input("Please enter the passenger's full name: ")
    while True:
        column = input("Choose your seat COLUMN (A/B): ")
        if column == "a" or column == "A":
            column = 0
        elif column == "b" or column == "B":
            column = 1
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        row = int(input("Choose your seat ROW (1-4): "))
        if row == 1:
            if vip1[column][0] != "   [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                vip1[column] = name.center(12)[:12]
        elif row == 2:
            if vip2[column][0] != "   [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                vip2[column] = name.center(12)[:12]
        elif row == 3:
            if vip3[column][0] != "   [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                vip3[column] = name.center(12)[:12]
        elif row == 4:
            if vip4[column][0] != "   [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                vip4[column] = name.center(12)[:12]
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        map()
        vip()
        return

def seatvip_b(): #First Class change seat phase 1 (remove name from array)
    name = input("Enter the passenger's full name \n"
                 "(NAME WILL BE REMOVED. CASE SENSITIVE): ")

    while True:
        column = input("Choose your OLD seat COLUMN (A/B): ")
        if column == "a" or column == "A":
            column = 0
        elif column == "b" or column == "B":
            column = 1
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        row = int(input("Choose your OLD seat ROW (1-4): "))
        if row == 1:
            if vip1[column] == ["   [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                vip1[column] = ["   [Open]    "]
                seatvip_c()
                break
        elif row == 2:
            if vip2[column] == ["   [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                vip2[column] = ["   [Open]    "]
                seatvip_c()
                break
        if row == 3:
            if vip3[column] == ["   [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                vip3[column] = ["   [Open]    "]
                seatvip_c()
                break
        if row == 4:
            if vip4[column] == ["   [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                vip4[column] = ["   [Open]    "]
                seatvip_c()
                break
        else:
            print("Not a valid choice. Please try again. Try again.")
            print()
            continue
        return

def seatvip_c(): #First Class change seat phase 2 (add/move name to diff. array)
    name = input("Please enter the passenger's full name (CONFIRMATION): ")
    while True:
        column = input("Choose your NEW seat COLUMN (A/B): ")
        if column == "a" or column == "A":
            column = 0
        elif column == "b" or column == "B":
            column = 1
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        row = int(input("Choose your NEW seat ROW (1-4): "))
        if row == 1:
            if vip1[column][0] != "   [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                vip1[column] = name.center(12)[:12]
        elif row == 2:
            if vip2[column][0] != "   [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                vip2[column] = name.center(12)[:12]
        elif row == 3:
            if vip3[column][0] != "   [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                vip3[column] = name.center(12)[:12]
        elif row == 4:
            if vip4[column][0] != "   [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                vip4[column] = name.center(12)[:12]
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        print("Reservation change confirmed.")
        map()
        return

def seatreg(): #main array formula for Coach Class
    name = input("Enter the passenger's full name: ")
    while True:
        column = input("Choose your seat COLUMN (A/B/C/D): ")
        if column == "a" or column == "A":
            column = 0
        elif column == "b" or column == "B":
            column = 1
        elif column == "c" or column == "C":
            column = 2
        elif column == "d" or column == "D":
            column = 3
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        row = int(input("Choose your seat ROW (1-10): "))
        if row == 1:
            if reg1[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg1[column] = name.center(12)[:12]
        elif row == 2:
            if reg2[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg2[column] = name.center(12)[:12]
        elif row == 3:
            if reg3[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg3[column] = name.center(12)[:12]
        elif row == 4:
            if reg4[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg4[column] = name.center(12)[:12]
        elif row == 5:
            if reg5[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg5[column] = name.center(12)[:12]
        elif row == 6:
            if reg6[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg6[column] = name.center(12)[:12]
        elif row == 7:
            if reg7[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg7[column] = name.center(12)[:12]
        elif row == 8:
            if reg8[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg8[column] = name.center(12)[:12]
        elif row == 9:
            if reg9[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg9[column] = name.center(12)[:12]
        elif row == 10:
            if reg10[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg10[column] = name.center(12)[:12]
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        map()
        reg()
        return

def seatreg_b(): #Coach Class change seat phase 1 (remove name from array)
    name = input("Please enter the passenger's full name \n"
                 "(NAME WILL BE REMOVED. CASE SENSITIVE): ")
    while True:
        column = input("Choose your OLD seat COLUMN (A/B/C/D): ")
        if column == "a" or column == "A":
            column = 0
        elif column == "b" or column == "B":
            column = 1
        elif column == "c" or column == "C":
            column = 2
        elif column == "d" or column == "D":
            column = 3
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        row = int(input("Choose your OLD seat ROW (1-10): "))
        if row == 1:
            if reg1[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg1[column] = ["  [Open]    "]
                seatreg_c()
                break
        elif row == 2:
            if reg2[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg2[column] = ["  [Open]    "]
                seatreg_c()
                break
        elif row == 3:
            if reg3[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg3[column] = ["  [Open]    "]
                seatreg_c()
                break
        elif row == 4:
            if reg4[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg4[column] = ["  [Open]    "]
                seatreg_c()
                break
        elif row == 5:
            if reg5[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg5[column] = ["  [Open]    "]
                seatreg_c()
                break
        elif row == 6:
            if reg6[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg6[column] = ["  [Open]    "]
                seatreg_c()
                break
        elif row == 7:
            if reg7[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg7[column] = ["  [Open]    "]
                seatreg_c()
                break
        elif row == 8:
            if reg8[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg8[column] = ["  [Open]    "]
                seatreg_c()
                break
        elif row == 9:
            if reg9[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg9[column] = ["   [Open]    "]
                seatreg_c()
                break
        elif row == 10:
            if reg10[column] == ["  [Open]    "]:
                print("Not the passenger's seat. Try again.")
                continue
            else:
                reg10[column] = ["  [Open]    "]
                seatreg_c()
                break
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        return

def seatreg_c(): #Coach Class change seat phase 2 (add/move name to diff. array)
    name = input("Enter the passenger's full name (CONFIRMATION): ")
    while True:
        column = input("Choose your NEW seat COLUMN (A/B/C/D): ")
        if column == "a" or column == "A":
            column = 0
        elif column == "b" or column == "B":
            column = 1
        elif column == "c" or column == "C":
            column = 2
        elif column == "d" or column == "D":
            column = 3
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        row = int(input("Choose your OLD seat ROW (1-10): "))
        if row == 1:
            if reg1[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg1[column] = name.center(12)[:12]
        elif row == 2:
            if reg2[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg2[column] = name.center(12)[:12]
        elif row == 3:
            if reg3[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg3[column] = name.center(12)[:12]
        elif row == 4:
            if reg4[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg4[column] = name.center(12)[:12]
        elif row == 5:
            if reg5[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg5[column] = name.center(12)[:12]
        elif row == 6:
            if reg6[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg6[column] = name.center(12)[:12]
        elif row == 7:
            if reg7[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg7[column] = name.center(12)[:12]
        elif row == 8:
            if reg8[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg8[column] = name.center(12)[:12]
        elif row == 9:
            if reg9[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg9[column] = name.center(12)[:12]
        elif row == 10:
            if reg10[column][0] != "  [Open]    ":
                print("Sorry, seat taken.")
                continue
            else:
                reg10[column] = name.center(12)[:12]
        else:
            print("Not a valid choice. Please try again.")
            print()
            continue
        map()
        return

def vip(): #First Class reservation main formula
    cost1 = 500
    print("The cost is $", cost1)
    print()
    while True:
        try:
            a = int(input(
                "Children under 7 and senior that are 65 years old or older "
                "are automatically discounted for 20% \n How old is the passenger? "))
        except:
            print('You have entered an invalid value. Please try again.')
            continue
        break
    if a <= 7 or a >= 65:
        cost2 = cost1 - (cost1 * 0.2)
        print("20% discount applied. Your cost now is: $", round(cost2, 2))
        totalcost = cost2 + (cost2 * 0.09)
        print(cost2, "+", round(cost2 * 0.09, 2), "\nYour total cost after 9% tax is $", round(totalcost, 2))
    else:
        print("No discount applied. Your cost now is:", cost1)
        totalcost = cost1 + (cost1 * 0.09)
        print(cost1, "+", round(cost1 * 0.09, 2), "\nYour total cost after 9% tax is $", round(totalcost, 2))
    while True:
        try:
            pay = float(input("How much you want to pay? $ "))
            change = pay - totalcost
            if change < 0:
                print("Sorry but your payment is not enough.")
                continue
            else:
                print("your change is $", round(change, 2))
                change_machine(change)
        except:
            print('You have entered an invalid value. Please try again.')
            continue
        break
    print()


def reg(): #Coach Class reservation main formula
    cost1 = 199
    print("Your total cost is $", cost1)
    print()
    while True:
        try:
            a = int(input(
                "Children under 7 and senior that are 65 years old or older are automatically discounted for 20% \n How old is the passenger? "))
        except:
            print('You have entered an invalid value. Please try again.')
            continue
        break
    if a <= 7 or a >= 65:
        cost2 = cost1 - (cost1 * 0.2)
        print("20% discount applied. Your cost now is: $", round(cost2, 2))
        totalcost = cost2 + (cost2 * 0.09)
        print(cost2, "+", round(cost2 * 0.09, 2), "\nYour total cost after 9% tax is $", round(totalcost, 2))
    else:
        print("No discount applied. Your cost now is:", cost1)
        totalcost = cost1 + (cost1 * 0.09)
        print(cost1, "+", round(cost1 * 0.09, 2), "\nYour total cost after 9% tax is $", round(totalcost, 2))
    while True:
        try:
            pay = float(input("How much you want to pay? $ "))
            change = pay - totalcost
            if change < 0:
                print("Sorry but your payment is not enough.")
                continue
            else:
                print("your change is $", round(change, 2))
                change_machine(change)
        except:
            print('You have entered an invalid value. Please try again.')
            continue
        break
    print()

def change_machine(change): #self explanatory
    print("")
    print("Change Machine Program initiated: ")
    print("$100:", int(change // 100))
    change = change % 100
    print("$20:", int(change // 20))
    change = change % 20
    print("$10:", int(change // 10))
    change = change % 10
    print("$5:", int(change // 5))
    change = change % 5
    print("$1:", int(change // 1))
    change = change % 1
    print("Quarter (25 c):", int(change // .25))
    change = change % .25
    print("Dime(10 c):", int(change // .1))
    change = change % .1
    print("Nickel(5 c):", int(change // .05))
    change = change % .05
    print("Penny (1 c):", int(change // .01))
    change = change % .01


while True: #main program loop
    print("What do you want to do? ")
    print("Enter 1 to choose First Class seat ($500).")
    print("Enter 2 to choose Coach Class seat ($199).")
    print("Enter 3 to change existing reservation.")
    print("Enter 4 to display seat map.")
    print("Enter 0 to quit")
    print()
    main = input("please make your selection:\n")
    if main == "1":
        print("\n You have selected First Class seat.")
        seatvip()
    elif main == "2":
        print("\n You have selected Coach seat.")
        seatreg()
    elif main == "3":
        edit = int(input("\n Press 1 for First Class\n Press 2 for Coach \n "))
        if edit == 1:
            seatvip_b()
        elif edit == 2:
            seatreg_b()
        else:
            print("\n Not a valid choice. Please try again.")
            print()
    elif main == "4":
        print("\n Displaying current seat map....")
        map()
    elif main == "0":
        print ("\n Thank you,", admin, "and have a good day!")
        break
    else:
        print("\n Not a valid choice. Please try again.")
        print()
