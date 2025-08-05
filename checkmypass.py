"""
Author: Kyle Allendorf

Overview:
This script was created to check passwords against the infamous haveibeenpwned password database and
notify the user if the password that has been entered is secure or not.

This script was created as part of the ZTM Python3 Developer course, with minor modifications.

There will be a version which I modified to accept input from the command line to make
it more repeatable.
In the future I may create a version which accepts a hashed text file containing passwords to enhance
the security of the script.
"""

import requests
import hashlib
import os
from sys import argv, exit

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')
    return res

def get_password_leak_count(hashes, hash_to_check):
    # Split response into hash : num of occurrences
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    # return 0 if hash is not found
    return 0

def pwned_api_check(password):
    # Check password to see if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # API only accepts first 5 characters of hash, save the rest for comparison later
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leak_count(response, tail)

def read_file(file):
    file_path = file
    passwords = []

    try:
        with open(file_path, 'r') as password_file:
            for line in password_file:
                passwords.append(line.strip())
    except FileNotFoundError:
        print(f"The File '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return passwords


def main(file_path):
    password_list = read_file(file_path)
    directory_path = os.path.dirname(file_path)
    badpasswordfile = 'badpasswords.txt'
    goodpasswordfile = 'goodpasswords.txt'

    for password in password_list:
        count = pwned_api_check(password)

        if count:
            with open(os.path.join(directory_path, badpasswordfile), 'a') as bad_file:
                bad_file.write(f'{password} was found {count} times... consider a different password!\n')
        else:
            with open(os.path.join(directory_path, goodpasswordfile), 'a') as good_file:
                good_file.write(f'{password} was not found!\n')

    print(f'Finished! Checked: {len(password_list)} password(s)')

    return print(f'Results can be found at {directory_path}')

if __name__ == '__main__':
    exit(main(argv[1]))



