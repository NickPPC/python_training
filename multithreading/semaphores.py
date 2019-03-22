import threading


class Queue():
    def __init__(self, n):
        self.available_spots = threading.Semaphore(n)
        self.content = []

    def add(self, x):
        self.available_spots.acquire()
        self.content.append(x)

    def pop(self):
        x = self.content.pop(0)
        self.available_spots.release()
        return x


def production(q, base):
    for i in range (100):
        q.add('{}.{}'.format(base, i))

def consumption(q):
    for _ in range(100):
        print(q.pop())

if __name__ == '__main__':

    q = Queue(10)
    n = 5
    prod = [threading.Thread(target=production, args=(q,i)) for i in range(n)]
    conso = [threading.Thread(target=consumption, args=(q,)) for i in range(n)]

    for t in prod:
        t.start()
    for t in conso:
        t.start()

# TODO: increase conso