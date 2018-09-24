import random

#define a main method
def main():
    input("Press Enter to generate your password.")
    #number of numbers in the password
    nums = 0
    #number of letters (upper and lower case) in the password
    let_up = 0
    let_lo = 0
    #number of symbols in the password
    sym = 0
    #special character
    special = 0
    while nums*let_up*let_lo*sym == 0:
        #the length of the password
        length = random.randint(6,16)
        code = ""
        for i in range(length):
            char_type = random.randint(0,3)
            if char_type == 0:
                code+=chr(random.randint(48,57))
                nums += 1
            elif char_type == 1:
                symbol_range = random.randint(0,3)
                if symbol_range == 0:
                    code+=chr(random.randint(33,47))
                elif symbol_range == 1:
                    code+=chr(random.randint(58,64))
                elif symbol_range == 2:
                    code+=chr(random.randint(91,96))
                else:
                    code+=chr(random.randint(123,126))
                sym += 1
            elif char_type == 2:
                case = random.randint(0,1)
                if case == 0:
                    code+=chr(random.randint(65,90))
                    let_up += 1
                else:
                    code+=chr(random.randint(97,122))
                    let_lo += 1
            else:
                if special <= 2:
                    code+=chr(random.randint(130,10000))
                    special += 1
                else:
                    code+=chr(random.randint(58,64))
                    sym += 1
    print(code)

while __name__ == '__main__':
    main()
