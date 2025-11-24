import datetime

import pymongo
from pymongo import MongoClient

print("Welcome to this (very simple) MongoDB Interface Program!")
uri = "mongodb://localhost:27017/"#input("Please enter your connection string: ")
client = MongoClient(uri)

database = client.get_database("sfils")
patronCollection = database.get_collection("patrons")
patronTypeCollection = database.get_collection("patronTypes")
homeLibraryCollection = database.get_collection("homeLibrary")
notPreferenceCollection = database.get_collection("notificationPreference")
print("Connection successful!")
print("This is a collection of library usage statistics for the San Francisco Public Library.")
print("Most identifying information has been removed to protect the identity of the patrons.")
count = patronCollection.count_documents({})
print(f"There are {count} patrons in the database.")
consoleInput = -1
while not consoleInput == 0:
    print("What would you like to do?")
    print("0 - Exit the program.")
    print("1 - Retrieve a document from the first added patron")
    print("2 - Add a new patron with a numeric ID.")
    print("3 - Delete a previously-added patron.")
    consoleInput = int(input(": "))
    match(consoleInput):
        case 1:
            patron = patronCollection.find_one({})
            patronType = patronTypeCollection.find_one({"_id":patron["patronTypeCode"]})
            homeLibrary = homeLibraryCollection.find_one({"_id":patron["homeLibraryCode"]})
            notPreference = notPreferenceCollection.find_one({"_id":patron["notificationPreferenceCode"]})
            print(f"Information for patron {patron["_id"]}")
            print(f"Type: {patronType["patronTypeDefinition"]}")
            print(f"Total Checkouts: {patron["totalCheckouts"]}")
            print(f"Total Renewals: {patron["totalRenewals"]}")
            print(f"Age Range: {patron["ageRange"]}")
            print(f"Home library: {homeLibrary["homeLibraryDefinition"]}")
            if patron["circulationActiveMonth"] == " ":
                print("This patron has no circulation history")
            else:
                print(f"This patron's most recent activity was in {patron["circulationActiveMonth"]} {patron["circulationActiveYear"]}")
            print(f"Notification Preference: {notPreference["notificationPreferenceDefinition"]}")
            if patron["providedEmailAddress"] is True:
                print("This patron has provided an Email address")
            else:
                print("This patron has not provided an Email address")
            if patron["withinSanFranciscoCounty"] is True:
                print("This patron is within San Francisco County")
            else:
                print("This patron is not within San Francisco County")
            print(f"Year Registered: {patron["yearPatronRegistered"]}")
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
            patronCollection.insert_one({"_id":str(count + 1),"patronTypeCode":str(patronInput),"totalCheckouts":0,"totalRenewals":0,"homeLibraryCode":"x","notificationPreferenceCode":str(notInput),"providedEmailAddress":bool(emailInput),"withinSanFranciscoCounty":bool(SFCountyInput),"yearPatronRegistered":currentYear})
            count = patronCollection.count_documents({})
            print(f"There are now {count} patrons in the database.")
        case 3:
            print("Which patron would you like to delete? Currently this only works with patron you have added.")
            IDInput = input(": ")
            if int(IDInput) < 437116 or int(IDInput) > count:
                print("Cannot access that patron.")
            else:
                patronCollection.delete_one({"_id":IDInput})
                count = patronCollection.count_documents({})
                print(f"There are now {count} patrons in the database.")
print("Closing connection and exiting program...")
client.close()
print("Goodbye...")