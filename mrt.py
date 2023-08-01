import pickle

def main():
    try:
        mp_num_dict = pickle.load(open('mp_num_dict.pickle', 'rb'))      
    except:
        mp_num_dict = {}

    print(mp_num_dict)

    try:
        current_record = mp_num_dict[max(mp_num_dict.keys())]
    except:
        current_record = 0
    #print(current_record)

    current_number = current_record + 1
    #print(current_number)

    while(True):
        
        multiplicative_persistence = test_number(current_number)
        #print(current_number)
        
        if multiplicative_persistence > current_record:
            #print(str(current_number) + " " + str(multiplicative_persistence))
            mp_num_dict[multiplicative_persistence] = current_number
            print(mp_num_dict)
            pickle.dump(mp_num_dict, open('mp_num_dict.pickle', 'wb'))
            current_record = multiplicative_persistence
        
        current_number += 1

def test_number(number):
    if number < 10:
        return 0
    elif number % 10 == 0:
        return 1

    digit_list = list(map(int, str(number)))
    
    if 0 in digit_list:
        return 1
    elif 5 in digit_list and (2 in digit_list or 4 in digit_list or 6 in digit_list or 8 in digit_list):
        return 2
    else:
        done = False
        current_iteration = 1
        while done == False:
            current_product = 1
            for element in digit_list:
                current_product *= element
            if current_product < 10:
                return current_iteration
            else:
                digit_list = list(map(int, str(current_product)))
                current_iteration += 1
    
    
    #current_iteration = 1
    
    #while(one_digit_reached = False)
    

if __name__ == "__main__":
    main()


