import random
import string
import datetime
from time import sleep

def main():
    logger()

def logger():
    while(True):
        sleep(5)
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k = 16))
        print(str(datetime.datetime.now()) + ': ' + random_string)
if __name__ == "__main__":
    main()
