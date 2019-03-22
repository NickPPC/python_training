import sys
import random

def generate_list(size, max):
    generated_list = []

    for i in range(size):
        generated_list.append(random.randint(0, max))

    return generated_list

def list_overlap(list1, list2):
    #TODO
    pass

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
        # TODO


    