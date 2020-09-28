from threading import *

def OddNumbersThread():
    for i in range(1,101):
    	if i%2 == 0:
    		print(i)
    
def EvenNumbersThread():
    for i in range(1,101):
    	if i%2 != 0:
    		print(i)

def MainThread():
    for i in range(1,101):
    	print(i)

t1 = Thread(target=OddNumbersThread)
t2 = Thread(target=EvenNumbersThread)
t3 = Thread(target=MainThread)
t1.start()
t2.start()
t3.start()
