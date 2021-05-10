import random

class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

def generate_six_random_numbers(guess_list):
    num_list = []
    for _ in range(5):
        num = random.randint(1, 71)
        num_list.append(num)
    num_list.sort()
    mega_num = random.randint(1, 26)
    num_list.append(mega_num)

    print(colors.underline + "Lottery result:\n" + colors.reset + "White: " + str(num_list[0:5]) + "\nMega: " + str(mega_num))
    print()
    print(colors.underline + "Your result:\n" + colors.reset + "White: " + str(guess_list[0:5]) + "\nMega: " + str(guess_list[-1]))

    num_match_count = 0
    for i in range(len(num_list) - 1):
        for j in range(len(guess_list) - 1):
            if num_list[i] == guess_list[j]:
                num_match_count += 1

    if num_list[-1] == guess_list[-1]:
        num_match_count += 1

    print(colors.fg.lightblue + "Found " + str(num_match_count) + " match(es)!" + colors.reset)

def run_input(my_guess):
    count = 1
    while count <= 6:
        isDuplicateIncluded = False
        try:
            if count <= 5:
                numinput = int(input(colors.fg.pink + str(count) + "." + colors.reset + " Enter a number between 1-70: "))

                if numinput <= 0 or numinput > 70:
                    print(colors.fg.lightred + "Number must be between 1-70!" + colors.reset)
                else:
                    if count == 1:
                        my_guess.append(numinput)
                        count += 1
                    else:
                        for i in range(len(my_guess)):
                            if numinput == my_guess[i]:
                                isDuplicateIncluded = True

                        if isDuplicateIncluded:
                            print(colors.fg.lightred + "Cannot assign that has a same number!" + colors.reset)
                        else:
                            my_guess.append(numinput)
                            count += 1

            else:
                my_guess.sort()
                numinput = int(input("Enter a mega number between 1-25: "))
                if numinput <= 0 or numinput > 25:
                    print(colors.fg.lightred + "Number must be between 1-25!" + colors.reset)
                else:
                    my_guess.append(numinput)
                    count += 1
        except ValueError:
            print(colors.fg.lightred + "Integer value is only allowed." + colors.reset)

    return my_guess

my_guess = []

print(colors.bold + "=======================|" + colors.reset)
print("Lottery Simulator")
print("By RueLee")
print(colors.bold + "=======================|" + colors.reset)
print("This code was inspired by ticket lottery (ex: mega million, power ball, etc.)")
print(colors.bold + "==================================================================================|" + colors.reset)
run_input(my_guess)
generate_six_random_numbers(my_guess)