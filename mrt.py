import pickle

def main():
    try:
        current_record = pickle.
    
    current_number = 0
    current_record = 0
    while(True):
        multiplicative_resistance = test_number(current_number)
        if multiplicative_resistance > current_record:
            print(str(current_number) + " " + str(multiplicative_resistance))
            current_list.write(str(current_number) + " " + str(multiplicative_resistance) + "\n")
            current_record = multiplicative_resistance
        current_number += 1

def test_number(number):
    if number < 10:
        return 0
    elif number % 10 == 0:
        return 1

    string_number = str(number)
    digit_list = list(string_number)
    
    if "0" in digit_list:
        return 1
    elif "5" in digit_list and "2" in digit_list:
        return 2
    else:
        done = False
        current_iteration = 1
        while done == False:
            current_product = 1
            for element in digit_list:
                current_product *= int(element)
            if len(str(current_product)) == 1:
                return current_iteration
            else:
                digit_list = list(str(current_product))
                current_iteration += 1
    
    
    #current_iteration = 1
    
    #while(one_digit_reached = False)
    

if __name__ == "__main__":
    main()


