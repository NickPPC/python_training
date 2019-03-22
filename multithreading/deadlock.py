import threading
import time

class BankAccount():
    def __init__(self, name):
        self.amount = 0
        self.name = name
        self.lock = threading.Lock()

    def withdraw(self):
        self.lock.acquire()
        if self.amount >= 100:
            print('Withdrawing 100 from {}'.format(self.name))
            self.amount -= 100
        self.lock.release()
    
    def credit(self):
        self.lock.acquire()

        if self.amount < 0:
            print('Negative amount !!!!!')
        print('Creditting 100 to {}'.format(self.name))
        self.amount += 100
        self.lock.release()

    def transfer(self, other_account):
        self.lock.acquire()
        if self.amount >= 100:
            print('We can transfer 100 from {} to  {}'.format(self.name, other_account.name))
            self.amount -= 100
            other_account.lock.acquire()
            other_account.amount += 100
            print('100 transfered')
            other_account.release()
        self.lock.release()

def withdrawing(account):
    start = time.time()
    while time.time() - start < 4:
        account.withdraw()
        print('Money {}: {}'.format(account.name, account.amount))

    print('Withdrawing done')

def creditting(account):
    start = time.time()
    while time.time() - start < 4:
        account.credit()
        print('Money {}: {}'.format(account.name, account.amount))

    print('Creditting done')

def transfering(account_from, account_to):
    start = time.time()
    while time.time() - start < 4:
        account_from.transfer(account_to)
        print('Money {}: {}'.format(account_from.name, account_to.amount))

    print('Transfering from {} to {} done'.format(account_from.name, account_to.name))

if __name__ == '__main__':

    account_me = BankAccount('Me')
    account_you = BankAccount('You')
    
    transfer_threads = [threading.Thread(target=transfering, args=(account_me, account_you))]

    
    accounts = [account_me, account_you]
    for j in range(2):
        withdrawing_threads = [threading.Thread(target=withdrawing, args =(accounts[j],), daemon=True) for i in range(5)]
        creditting_threads = [threading.Thread(target=creditting, args = (accounts[j],), daemon=True) for i in range(2)]
        transfer_threads = [threading.Thread(target=transfering, args=(accounts[j], accounts[j % 2])) for i in range(2)]

        for t in creditting_threads:
            t.start()
        for t in withdrawing_threads:
            t.start()
        for t in transfer_threads:
            t.start()

    time.sleep(5)