#################################################################################

• Install Django on your system command for Linux:
		sudo apt-get update
		sudo apt-get install python-django
• Download the project from the given link of Github.
• Go to the main directory ProofReader(which contains the file manage.py).
• Open the terminal and run the command:
		python3 manage.py runserver
-This will start the server and host our website on the local host.
• Signup if newuser or Login if existing

• Upon login you will see a contenteditable <div> inside which you can enter your query then on 
clicking the submit button you will see the suggestion of the corrected text which can be replaced in 
following ways:
	-Suggestion from API.
	-Manual input from user.
Example-
	Query: this is a exapmle.
	Returns: Errors is the given statement along with its type ,possible replacements.
	Final:	Corrected text obtained by replacing the errors with replacement selected by user.
		(This is an example.)


#################################################################################