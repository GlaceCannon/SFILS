db = connect("mongodb://localhost:27017/sfils");

patronTypeColl = db.patronsUnsorted.aggregate([
	{$group:{_id:"$patronTypeCode", patronTypeDefinition:{$addToSet:"$patronTypeDefinition"}}},
	{$unwind:"$patronTypeDefinition"}]);
	
db.patronType.insertMany(patronTypeColl.toArray());

homeLibraryColl = db.patronsUnsorted.aggregate([
	{$group:{_id:"$homeLibraryCode", homeLibraryDefinition:{$addToSet:"$homeLibraryDefinition"}}},
	{$unwind:"$homeLibraryDefinition"}]);

db.homeLibrary.insertMany(homeLibraryColl.toArray());

notificationPreferenceColl = db.patronsUnsorted.aggregate([
	{$group:{_id:"$notificationPreferenceCode", notificationPreferenceDefinition:{$addToSet:"$notificationPreferenceDefinition"}}},
	{$unwind:"$notificationPreferenceDefinition"}]);

db.notificationPreference.insertMany(notificationPreferenceColl.toArray());

patronsSorted = db.patronsUnsorted.aggregate([
	{$project:{"_id":0,"patronTypeDefinition":0,"homeLibraryDefinition":0,"notificationPreferenceDefinition":0}}]);

db.patrons.insertMany(patronsSorted.toArray());

db.patronsUnsorted.drop();