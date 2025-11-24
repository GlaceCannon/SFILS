This repository contains information required to set up a database of patrons of the San Francisco Public Library in MongoDB. It also contains a program that performs very basic read, add, and delete operations on the database. The 'results' folder contains some comparisons to the MySQL setup.

Creating the database:

If you have MongoDB Compass installed, use the same .csv file from the original program. Open a shell in your local connection by right-clicking it in the 'Connections' menu and selecting 'Open MongoDB shell' and enter the following to set up the database:

> use sfils

> db.createCollection("patronsUnsorted")

Navigate to this collection and click 'Add Data', then 'Import JSON or CSV file'. Select the .csv file in the 'scripts' folder, then select 'Import' in the bottom-right when it is done reading the data. You do not have to modify any of the settings before importing. Once this is done, run 'sfils.js' in a separate installation of mongosh (the shell in Compass does not support running scripts) by opening the shell and entering your connection string (You can get this by right-clicking your connection and selecting 'Copy connection string'), then typing:

> load("[TYPE THE PATH TO SFILS.JS HERE]")

This will assume that your local installation is on the default port. If it is not, you can modify the number '27017' in the script, or perform the next steps instead.

If you do not have a separate installation of mongosh, you can run the following commands in the Compass shell (You can copy-paste them):

> db.patronsUnsorted.aggregate([{$group:{_id:"$patronTypeCode",patronTypeDefinition:{$addToSet:"$patronTypeDefinition"}}},{$unwind:"$patronTypeDefinition"},{$out:"patronTypes"}])

> db.patronsUnsorted.aggregate([{$group:{_id:"$homeLibraryCode",homeLibraryDefinition:{$addToSet:"$homeLibraryDefinition"}}},{$unwind:"$homeLibraryDefinition"},{$out:"homeLibrary"}])

> db.patronsUnsorted.aggregate([{$group:{_id:"$notificationPreferenceCode",notificationPreferenceDefinition:{$addToSet:"$notificationPreferenceDefinition"}}},{$unwind:"$notificationPreferenceDefinition"},{$out:"notificationPreference"}])

> db.patronsUnsorted.aggregate([{$project:{"patronTypeDefinition":0,"homeLibraryDefinition":0,"notificationPreferenceDefinition":0}},{$out:"patrons"}])

> db.patronsUnsorted.drop()

This will create a database with a similar structure to the MySQL version.

Using the app:

The program also uses a Python app, so make sure Python is installed. Like last time, it requires an external library called pymongo, which can be installed like the MySQL connector:

> pip install pymongo

or whichever method was required to make it work. To run the program, type:

> py sfilsmongo.py

The program will ask you for a connection string. You can find this string in Compass by right-clicking the connection in the 'Connections' menu and selecting 'Copy connection string'. Simply paste this string into the input.

Because of the radically different structure of the database, much of the functionality had to be gutted. The program can perform three actions:

	It can read data from the first patron that was entered into the database. This will not be the same between different imports.
	
	It can create a new patron document with a numeric ID based on the number of patrons in the database.
	
	It can delete one of the patrons you have added with the above action.