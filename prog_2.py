def prog_2(l):
    len_list = len(numeric_array)
    if len_list == 0:
        return 0
    sum_of_el = 0
    number_of_positive_el = 0
    for el in numeric_array:
        sum_of_el += el
        if el>0:
            number_of_positive_el += 1
    numeric_array.insert(0, sum_of_el)
    numeric_array.insert(1, number_of_positive_el)
    return numeric_array

if __name__ == '__main__':
    num_l = input('Enter data:').split()
    if len(num_l) == 0:
        print("No data.")
    else:
        try:
            numeric_array = list(map(float, num_l))
        except:
            print("Invalid data.")
        else: print(prog_2(num_l))
    input()