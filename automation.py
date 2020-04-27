from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time

link_addaccount = "https://accounts.google.com/ServiceLogin/identifier?continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&csig=AF-SEnZg0gjrAEALE5xG%3A1587964981&service=accountsettings&flowName=GlifWebSignIn&flowEntry=AddSession"
link_signout = "https://accounts.google.com/Logout"

#put csv file into a 2D list format
creds = list(csv.reader(open("students.csv")))

#open and erase pass and fail files for read+write and erase their contents
#delete their contents if they have any
passfile = open("pass.csv","w+")
passfile.truncate(0)
failfile = open("fail.csv","w+")
failfile.truncate(0)

#open a new window for Firefox
driver = webdriver.Firefox()

#initialize global variables
email = ""
pswd = ""
user = ""

#go to a fresh instance of the Google Sign-In link
driver.get(link_addaccount)

#wait for page to load completely
time.sleep(2)

#for each student in the .csv file
for elem in creds:
	try:
		#pull the email and passwords from the .csv file
		email = elem[0]
		user = elem[1]
		pswd = elem[2]

		#click on the input box for email and type in email
		fill = driver.find_element_by_xpath("//*[@id=\"identifierId\"]")
		fill.click()
		fill.send_keys(email)

		#click the "Next" button
		fill = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span")
		fill.click()

		#wait for the next section to load
		time.sleep(1)

		#click on the input box for password and type in email
		fill = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
		fill.click()
		fill.send_keys(pswd)

		#click the "Next" button
		fill = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/span")
		fill.click()

		#wait for the next section to load
		time.sleep(2)

		#click the "Agree button"
		fill = driver.find_element_by_xpath("//*[@id=\"accept\"]")
		fill.click()

		#wait for the next section to load
		time.sleep(2)

		#open sidebar to look at email address
		fill = driver.find_element_by_xpath("/html/body/div[2]/header/div[2]/div[3]/div[1]/div[2]/div/a/span")
		fill.click()

		#wait for the next section to load
		time.sleep(1)

		#assert that the email is the same as the account being currently tested
		fill = driver.find_element_by_xpath("/html/body/div[2]/header/div[2]/div[4]/div[2]/div[2]/div[2]")
		fill.click()
		assert(email == fill.text)

		#add account to the list of passed accounts
		passfile.write(email+","+user+","+pswd+"\n")

		#sign out
		driver.get(link_signout)

		#wait for the next section to load
		time.sleep(2)
		
		#print to console
		print(" successful login with user: "+user)

		#set up for next account
		fill = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[3]/div")
		fill.click()
		time.sleep(1)
		fill = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div[1]/ul/li[1]/div/div[2]")
		fill.click()
		time.sleep(1)
		fill = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div[3]/div[1]/span/span")
		fill.click()

		#wait for the next section to load
		time.sleep(2)

	except:
		#print to console
		print("noncritical error with user: "+user)

		#add account to the list of failed accounts
		failfile.write(email+","+user+","+pswd+"\n")

		#restart window to reset driver
		driver.close()
		driver = webdriver.Firefox()
		driver.get(link_addaccount)

#print to console
print("finished execution")

#wrap up program
driver.close()
passfile.close()
failfile.close()
