
def filter_out_multiple(numbers_list, x):
    maxi = max(numbers_list)
    for i in range(maxi // x + 1):
        try:
            numbers_list.remove(i * x)
        except:
            pass
    return numbers_list
    


def filter_out_multiple_copy(numbers_list, x):
    filtered_list = [n for n in numbers_list if n % x != 0]
    return filtered_list



if  __name__ == '__main__':
    n = 50

    print('No copy\n\n')
    full_list = [i for i in range(n)]
    print(full_list)
    list_no_3s = filter_out_multiple(full_list, 3)
    print(list_no_3s)
    list_no_9s = filter_out_multiple(full_list, 9)
    print(list_no_9s)

    print('\n\nCopy\n\n')
    full_list = [i for i in range(n)]
    print(full_list)
    list_no_3s = filter_out_multiple_copy(full_list, 3)
    print(list_no_3s)
    list_no_9s = filter_out_multiple_copy(full_list, 9)
    print(list_no_9s)
