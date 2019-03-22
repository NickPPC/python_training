import sys
import random

def generate_list(size, max):
    generated_list = []

    for i in range(size):
        generated_list.append(random.randint(0, max))

    return generated_list

def list_overlap(list1, list2):
    overlapping_elements = []
    for x in list1:
        if x in list2:
            overlapping_elements.append(x)
    return overlapping_elements


def make_unique_flawed(repeated_list):

    for i in range(len(repeated_list)):
        for j in range(i + 1, len(repeated_list)):
            if repeated_list[i] == repeated_list[j]:
                repeated_list.remove(repeated_list[i])
    

if __name__ == '__main__':

    if len(sys.argv) < 5:
        print('Missing arguments, need 4')
    else:
        seed = int(sys.argv[1])
        max_value = int(sys.argv[2])
        size1 = int(sys.argv[3])
        size2 = int(sys.argv[4])

        random.seed(seed)

        list1 = generate_list(size1, max_value)
        list2 = generate_list(size2, max_value)

        print(list1)
        print(list2)
        overlapping = list_overlap(list1, list2)
        print(overlapping)

        print(make_unique_flawed(overlapping))

# python3 list_overlap.py 0 50 20 10
# [24, 48, 26, 2, 16, 32, 31, 25, 50, 19, 30, 22, 37, 13, 32, 8, 18, 8, 48, 6]
# [39, 16, 34, 45, 38, 9, 19, 6, 46, 4]
# [16, 19, 6]

# python3 list_overlap.py 1 50 20 10
# [8, 36, 48, 4, 16, 7, 31, 48, 28, 30, 41, 24, 50, 13, 6, 31, 1, 24, 27, 38]
# [48, 49, 0, 44, 28, 17, 46, 14, 37, 6]
# [48, 48, 28, 6]

# python3 list_overlap.py 0 20 20 20
# [12, 13, 1, 8, 16, 15, 12, 9, 15, 11, 18, 6, 16, 4, 9, 4, 3, 19, 8, 17]
# [19, 4, 9, 3, 2, 10, 15, 17, 3, 11, 13, 10, 19, 20, 6, 17, 15, 14, 16, 8]
# [13, 8, 16, 15, 9, 15, 11, 6, 16, 4, 9, 4, 3, 19, 8, 17]
