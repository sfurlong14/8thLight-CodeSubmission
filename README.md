# 8thLight-CodeSubmission

Introduction


This application utilizes Python and the Google book API in order to perform tasks that were required of the assessment. This app was intended to be simple and 	user friendly. For this reason, the only thing that needs to be installed to run the application with be python 3.9.

The follwoing libraries will be used for the the progam to function

	import requests     # essential for http request for the Google Book API
	import json         # essential to convert the users reading list into a txt file


Running the App and Testing


Once Python has been installed on the machine, clone this repository to the local machine and launch in a terminal utilizing the following command:
	
	python3 BookAPI.py
	
the app will launch immediately and bring the user to the main menu with in the console. This menu will give the user four options which will be activated by pressing a number 1 - 4.

       Create A Reading List
    ____________________________________________________


          press 1: ONLY BROWSE
          press 2: BROWSE and SAVE TO READING LIST
          Press 3: VIEW READING LIST
          Press 4: EXIT

    ____________________________________________________
    
OPTION 1 = will allow the user to to view by key word. The user will only be able to browse the result before being sent back to menu

OPTION 2 = will allw the user to browse the option and save one of those 5 choices to the reading list

OPTION 3 = will allow the user to view the reading list create during the session

OPTION 4 = will convert the reading list to a .txt file and exit the application


Testing was done through test drivent development with importing the python library Unittest
	
		python3 Testing.py
