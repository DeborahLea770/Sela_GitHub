import sys
from colorama import Fore
import argparse

def password_check(passwd):
    val = 0

    if len(passwd) < 10:
        print('length should be at least 10')
        val = 1

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = 1

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = 1

    if not any(char.islower() for char in passwd):
        print(f'{Fore.WHITE}Password should have at least one lowercase letter')
        val = 1

    return val

# Main method
def main():
    passwd = sys.argv[1]
    parser = argparse.ArgumentParser()

    if len(sys.argv) == 3:
        parser.add_argument('-f', required=True)
        args = parser.parse_args()
        txt = args.f
        f = open("." + txt, 'r')
        passwd = f.readline()
        f.close()

    if password_check(passwd) == 0:
        print(f"{Fore.GREEN}Password is valid")
    else:
        print(f"{Fore.RED}Invalid Password !!")
    print(Fore.WHITE)

# Driver Code
if __name__ == '__main__':
    main()
