#Jesus Gomez Martinez 
#Telephone Number Word Generator
#22561 Prog & Prob Solv 2
"""This is a program that will generate every possible word from
letters that correspond to their telephone number."""

def main():
    numbers_To_Letters = [["A", "B", "C"],
                         ["D", "E", "F"],
                         ["G", "H", "I"],
                         ["J", "K", "L"],
                         ["M", "N", "O"],
                         ["P", "R", "S"],
                         ["T", "U", "V"],
                         ["W", "X", "Y"]]
    telephone_Number = get_Telephone_Number()
    words_From_Number = get_Words(telephone_Number, numbers_To_Letters)
    print_information(words_From_Number)


def get_Telephone_Number():
    i = 0
    while i == 0:
        try:
            number = str(input("Please enter your phone number using only 7 digits: "))
            if not number.isdigit():
                raise TypeError
            while len(number) != 7:
                  number = str(input("Please make sure to enter 7 digits: "))
            i += 1
        except:
            print("Please enter a 7 digit number with no symbols or letters.")
    return int(number)


def get_Words(telephone_Number, numbers_To_Letters):
    list_Of_Digits = [int(i) for i in str(telephone_Number)]
    possible_Words = []
    i = 0
    for digit in numbers_To_Letters[list_Of_Digits[i] - 2]:
        for digit2 in numbers_To_Letters[list_Of_Digits[i+1] - 2]:
            for digit3 in numbers_To_Letters[list_Of_Digits[i+2] - 2]:
                for digit4 in numbers_To_Letters[list_Of_Digits[i+3] - 2]:
                    for digit5 in numbers_To_Letters[list_Of_Digits[i+4] - 2]:
                        for digit6 in numbers_To_Letters[list_Of_Digits[i+5] - 2]:
                            for digit7 in numbers_To_Letters[list_Of_Digits[i+6] - 2]:
                                possible_Words.append(digit+digit2+digit3+digit4+digit5+digit6+digit7)
    return possible_Words


def print_information(words_From_Numbers):
    print(f'Total number of words is {len(words_From_Numbers)}.')
    print(words_From_Numbers)

main()