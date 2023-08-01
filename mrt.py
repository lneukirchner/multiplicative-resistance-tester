def main():
    current_number = 0
    while(True):
        multiplicative_resistance = test_number(current_number)
        print(str(current_number) + " -> " + str(multiplicative_resistance))
        current_number += 1

def test_number(number):
    string_number = str(number)
    split_list = string_number.split()
    current_total_product = 1
    for element in split_list:
        current_total_product *= int(element)
    return current_total_product

if __name__ == "__main__":
    main()


