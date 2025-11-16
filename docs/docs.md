This repository contains the means to create a database of patrons of the San Francisco Public Library in MySQL. It also contains a simple program that is able to read, create, and delete data for individual patrons. In addition, the 'results' folder contains some interesting finds about the database.

Creating the database:

In order to create the database, unzip the file in the 'scripts' folder and place the .csv file into the default import folder for MySQL. On Windows, this is:

C:/ProgramData/MySQL/MySQL Server 8.0/Uploads

ProgramData is a hidden folder. You may have to enable the option to show hidden folders by selecting the drop-down 'View' menu in File Explorer, hovering over 'Show' and selecting 'Hidden items' (See 'hiddenitems.png'). Once the file is in the correct folder, simply run the 'sfils.sql' script, also in the 'scripts' folder, on your server. As long as your current account has the correct permissions, it will create a 'sfils' schema with a 'patrons' table, as well as three other tables that contain additional information.

Using the app:

You will have to install Python in order to run the program in the 'app' folder in the repository. The program also requires the mysql connector package, which can be installed with PIP (which should come installed with Python) by running the following command in a command prompt:

	> pip install mysql-connector-python
	
If that doesn't work, you may need to add the path to PIP to your environment variables, or you may need to run it using your base Python path, like this:

	> python3 pip install mysql-connector-python
	
After that, you should be able to run the program in the command prompt as you would any Python program:

	> python3 sfils.py
	
The program will ask you to log in to your server. Remember to make sure the server is running, and to use an account that has the proper permissions for editing. The program can perform three simple operations on the database:

	It can print the information about a given patron based on the ID assigned by the database.
	
	It can add a new patron to the database, allowing the user to input some of its values.
	
	It can delete a patron from the database using their ID.
	
When prompted to give a numeric response, enter only numeric values. In its current state, the program will crash if a non-numeric value is entered at these prompts. This restriction does not apply to non-numeric responses.

Acknowledgements:

W3schools has a comprehensive MySQL tutorial on their website:

	https://www.w3schools.com/mysql/default.asp
	
Documentation about the MySQL connector can be found on their website:


	https://dev.mysql.com/doc/refman/8.4/en/connector-python-info.html
