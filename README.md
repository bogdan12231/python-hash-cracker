# python-hash-cracker
A simple Python script the performs a dictionary attack to crack hashes. It compares generated hashes with a target hash to find the password
How to use:
1. Generate a Hash
If you want to create a hash to test the cracker, run the generator script:
  python hasher.py
2. Crack a Hash
To perform a dictionary attack, ensure you have a wordlist (e.g., passwords.txt) and run:
  python cracker.py

Project Structure

-hasher.py: Simple utility to convert strings into various hash formats.

-cracker.py: The main logic containing the Wordlist and Cracker classes.

-wordlist.txt: (Optional) Your list of potential passwords for testing.
