import datetime

import mysql.connector
from mysql.connector import errorcode

print("Welcome to this (very simple) MySQL interface program!")
userInput = input("Please enter your username: ")
passwordInput = input("Please enter your password: ")

try:
    cnx = mysql.connector.connect(user = userInput, password =  passwordInput, database = 'sfils')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Unable to access that database. Does it exist?")
    else:
        print(err)
else:
    cursor = cnx.cursor()
    print("Connection successful!")
    print("This is a table of library usage statistics for the San Francisco Public Library.")
    print("Most identifying information has been removed to protect the privacy of the patrons.")
    query = "SELECT COUNT(*) AS numPatrons FROM patrons;"
    cursor.execute(query)
    row = cursor.fetchone()
    numPatrons = row[0]
    print(f"There are {numPatrons} patrons in the database.")
    consoleInput = -1
    while not consoleInput == 0:
        print("What would you like to do?")
        print("0 - Exit this program.")
        print("1 - Retrieve information on a patron by ID.")
        print("2 - Add a patron by ID.")
        print("3 - Delete a patron by ID.")
        consoleInput = int(input(": "))
        match consoleInput:
            case 1:
                print("Enter the ID of the patron")
                IDInput = input(": ")
                if int(IDInput) < 1 or int(IDInput) > numPatrons:
                    print("That patron does not exist.")
                else:
                    query = "SELECT PatronID, patronType.patronType, totalCheckouts, totalRenewals, ageRange, homeLibrary.homeLibrary, circulationActiveMonth, circulationActiveYear, notificationPreference.notificationPreference, providedEmailAddress, inSanFranciscoCounty, yearRegistered FROM patrons JOIN patronType ON patrons.patronTypeCode = patronType.patronTypeCode JOIN homeLibrary ON patrons.homeLibraryCode = homeLibrary.homeLibraryCode JOIN notificationPreference ON patrons.notificationPreferenceCode = notificationPreference.notificationPreferenceCode WHERE patronID = %s;"
                    cursor.execute(query, (IDInput,))
                    row = cursor.fetchone()
                    print(f"Information for patron {IDInput}:")
                    print(f"Type: {row[1]}")
                    print(f"Total Checkouts: {row[2]}")
                    print(f"Total Renewals: {row[3]}")
                    print(f"Age Range: {row[4]}")
                    print(f"Home Library: {row[5]}")
                    if row[7] is None:
                        print("This patron has no circulation history")
                    else:
                        print(f"This patron's most recent activity was in {row[6]} {row[7]}")
                    print(f"Notification Preference: {row[8]}")
                    if row[9] == 0:
                        print("This patron has not provided an Email address")
                    else:
                        print("This patron has provided an Email address")
                    if row[10] == 0:
                        print("This patron is not in San Francisco County")
                    else:
                        print("This patron is in San Francisco County")
                    print(f"Year Registered: {row[11]}")
            case 2:
                patronInput = -1
                while int(patronInput) < 0 or int(patronInput) > 3:
                    print("What type of patron is this?")
                    print("0 - Adult")
                    print("1 - Juvenile")
                    print("2 - Teen")
                    print("3 - Senior")
                    patronInput = input(": ")
                notInput = '\0'
                while not notInput == '-' and not notInput == 'a' and not notInput == 'p' and not notInput == 'z':
                    print("How does this patron wish to be notified?")
                    print("- - No contact provided")
                    print("a - Print")
                    print("p - Phone")
                    print("z - Email")
                    notInput = input(": ")
                emailInput = -1
                while not int(emailInput) == 0 and not int(emailInput) == 1:
                    print("Has this person provided an Email address?")
                    print("0 - No")
                    print("1 - Yes")
                    emailInput = input(": ")
                SFCountyInput = -1
                while not int(SFCountyInput) == 0 and not int(SFCountyInput) == 1:
                    print("Is this person in San Francisco County?")
                    print("0 - No")
                    print("1 - Yes")
                    SFCountyInput = input(": ")
                currentYear = datetime.datetime.today().year
                query = "INSERT INTO patrons (patronID, patronTypeCode, totalCheckouts, totalRenewals, homeLibraryCode, notificationPreferenceCode, providedEmailAddress, inSanFranciscoCounty, yearRegistered) VALUES (%s, %s, 0, 0, 'x', 'a', %s, %s, %s);"
                cursor.execute(query, (int(numPatrons) + 1, int(patronInput), int(emailInput), int(SFCountyInput), currentYear))
                cnx.commit()
                query = "SELECT COUNT(*) AS numPatrons FROM patrons;"
                cursor.execute(query)
                row = cursor.fetchone()
                numPatrons = row[0]
                print(f"There are now {numPatrons} patrons in the database.")
            case 3:
                print("Which patron would you like to delete?")
                IDInput = input(": ")
                if int(IDInput) < 1 or int(IDInput) > numPatrons:
                    print("That patron does not exist.")
                else:
                    query = "DELETE FROM patrons WHERE patronID = %s;"
                    cursor.execute(query, (IDInput,))
                    cnx.commit()
                    query = "SELECT COUNT(*) AS numPatrons FROM patrons;"
                    cursor.execute(query)
                    row = cursor.fetchone()
                    numPatrons = row[0]
                    print(f"There are now {numPatrons} patrons in the database.")
    print("Closing the connection and exiting the program...")
    cnx.close()
    print("Goodbye...")
