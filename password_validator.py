import sys
from colorama import Fore
import argparse

def password_check(passwd):
    """
     A program to validate password strength with the following requirements:
     password strength with the following requirements:
     Length – minimum of 10 characters.
     Contain both alphabet and number.
     Include both the small and capital case letters.
     The output will be green if it passed the validation and red if it didn’t.
     The program return exit code 0 if it passed the validation and exit code 1 if it didn’t.
    """
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

    if password_check(passwd) == 0:
        print(f"{Fore.GREEN}Password is valid")
    else:
        print(f"{Fore.RED}Invalid Password !!")
    print(Fore.WHITE)

# Driver Code
if __name__ == '__main__':
    main()
