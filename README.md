G Suite Account Activation Automation through Terms and Conditions
Backbone of Selenium for Firefox

This script automates the process to activate multiple G Suite accounts created through web scraping. The script begins by reading in the account information from the students.csv file put into the following format:

username@domain.ext,username,password

The program then uses the account information to go to accounts.google.com, log into the account using the provided username and password, accept the terms and conditions, confirm that the program reached the log-in page, and then log out. 

The program will repeat until all lines in the file have been tried. All lines that were completed will be written to the file pass.csv, and all files that had an error while attempting log-in or accepting the terms and conditions will be stored into fail.csv. 

To run the program, you must have the following programs given below:
Python 3: https://www.python.org/downloads/
Mozilla Firefox: https://www.mozilla.org/en-US/firefox/new/
Gecko Driver (must include in PATH environment variable: https://selenium-python.readthedocs.io/installation.html
Note: There is no need for a Selenium server. Just the geckodriver for Firefox will work. 

Steps to run:
1. Download and unzip the folder in the desired location
2. Enter the folder in your desired command prompt and run the following commands
pip install -U -r requirements.txt
3. Put a .csv file of the format specified above into the folder and name it students.csv
4. Run the following command
python3 automation.py

INPUT: students.csv
OUTPUT: students.csv(unchanged), pass.csv, fail.csv