from time import sleep
import os, random, string, datetime

def main():
    logwriter()
def random_hash():
    return ''.join(random.choices(string.ascii_letters + string.digits, k = 16))

def logwriter():
    filename = "files/logged.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    while(True):
        with open(filename, "a+") as log_file:
            log_file.write(str(datetime.datetime.now()) + ': ' + random_hash() + "\n")
        sleep(5)

if __name__ == "__main__":
    main()
