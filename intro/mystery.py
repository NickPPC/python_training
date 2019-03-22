import sys
import random
def fait_un_truc(a, b):
    x = []
    for i in range(a):
        x.append(random.randint(0, b))
    return x
def fait_autre_chose(a, b):
    c = []
    for x in a:
        if x in b:
            c.append(x)
    return c
if __name__ == '__main__':
    if len(sys.argv) == 5:
        random.seed(int(sys.argv[1]))
        a = fait_un_truc(int(sys.argv[3]), int(sys.argv[2]))
        b = fait_un_truc(int(sys.argv[4]), int(sys.argv[2]))
        print(a)
        print(b)
        voila = fait_autre_chose(a, b)
        print(voila)


