# python-password-checker
Checks passwords against the HaveIBeenPwned password database.
Source code can be found in the source branch.


# Usage
This is a very simple script. You must run checkmypass.exe in a command line interface and pass an argument containing the path of a text file containing a list of passwords.
The script will take that list and check it against the HaveIBeenPwned password database.
Passwords that are found in the database are deemed 'bad', while passwords that are not found are deemed 'good'.
Good and bad passwords will be separated.

To maintain privacy and security, the HaveIBeenPwned database API only accepts obfuscated hashed passwords.
The script will obfuscate and hash passwords before making a request with the API.

Command:
`<path_to_checkmypass.exe> <path_to_list_file>`

An example command with executable path:
`C:\Users\User\Downloads\password_checker\dist\checkmypass.exe C:\Users\User\Desktop\passwords.txt`

Add chechmypass.exe to OS PATH and run (not recommended)
`checkmypass <path_to_list_file>`

An example command with OS PATH Variable:
`checkmypass.exe C:\Users\User\Desktop\passwords.txt`


# Outputs
The script will generate two text files in the same directory as the text file you pass to it.
One file (goodpasswords.txt) will contain all of your acceptable passwords.
A different file (badpasswords.txt) will contain all of your compromised passwords.

The script is currently configured to create and then append these files.
If you run the program again it will not check for duplicates and it will continue to append to that file.
The script does not perform any cleanup, files will need to be handled by the user after execution.
