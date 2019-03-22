import threading
import time

class BankAccount():
    def __init__(self):
        self.amount = 0
        self.lock = threading.Lock()

    def withdraw(self):
        self.lock.acquire()
        if self.amount >= 100:
            print('Withdrawing 100')
            self.amount -= 100
        self.lock.release()
    
    def credit(self):
        self.lock.acquire()
        if self.amount < 0:
            print('Negative amount !!!!!')
        print('Creditting 100')
        self.amount += 100
        self.lock.release()

def withdrawing(account):
    start = time.time()
    while time.time() - start < 0.5:
        account.withdraw()
        print('Money : {}'.format(account.amount))

    print('Withdrawing done')

def creditting(account):
    start = time.time()
    while time.time() - start < 0.5:
        account.credit()
        print('Money : {}'.format(account.amount))

    print('Creditting done')


if __name__ == '__main__':

    account = BankAccount()
    withdrawing_threads = [threading.Thread(target=withdrawing, args =(account,), daemon=True) for i in range(5)]
    creditting_threads = [threading.Thread(target=creditting, args = (account,), daemon=True) for i in range(2)]
    for t in creditting_threads:
        t.start()
    for t in withdrawing_threads:
        t.start()
    time.sleep(1)