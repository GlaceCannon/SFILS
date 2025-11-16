CREATE SCHEMA sfils;
USE sfils;

CREATE TABLE patronType(
	patronTypeCode INT NOT NULL,
	patronType VARCHAR(32) NOT NULL,
	CONSTRAINT PK_PATRONTYPE PRIMARY KEY(patronTypeCode)
);

CREATE TABLE homeLibrary(
	homeLibraryCode VARCHAR(8),
	homeLibrary VARCHAR(32) NOT NULL,
	CONSTRAINT PK_HOMELIBRARY PRIMARY KEY(homeLibraryCode)
);

CREATE TABLE notificationPreference(
	notificationPreferenceCode CHAR NOT NULL,
    notificationPreference VARCHAR(32) NOT NULL,
    CONSTRAINT PK_NOTIFICATIONPREFERENCE PRIMARY KEY(notificationPreferenceCode)
);

CREATE TABLE patrons(
	patronTypeCode INT NOT NULL,
    totalCheckouts INT NOT NULL,
    totalRenewals INT NOT NULL,
    ageRange VARCHAR(32),
    homeLibraryCode VARCHAR(8),
    circulationActiveMonth VARCHAR(16),
    circulationActiveYear YEAR,
    notificationPreferenceCode CHAR NOT NULL,
    providedEmailAddress BOOL NOT NULL,
    inSanFranciscoCounty BOOL NOT NULL,
    yearRegistered YEAR NOT NULL,
    patronID INT NOT NULL AUTO_INCREMENT,
    CONSTRAINT PK_PATRONID PRIMARY KEY(PatronID),
    CONSTRAINT FK_PATRONTYPECODE FOREIGN KEY(patronTypeCode) REFERENCES patronType(PatronTypeCode),
    CONSTRAINT FK_HOMELIBRARYCODE FOREIGN KEY(homeLibraryCode) REFERENCES homeLibrary(homeLibraryCode),
    CONSTRAINT FK_NOTIFICATIONPREFERENCECODE FOREIGN KEY(notificationPreferenceCode) REFERENCES notificationPreference(notificationPreferenceCode)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/SFPL_DataSF_library-usage_Jan_2023.csv' IGNORE
INTO TABLE patronType
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(patronTypeCode, patronType);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/SFPL_DataSF_library-usage_Jan_2023.csv' IGNORE
INTO TABLE homeLibrary
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@col, @col, @col, @col, @col, @homeLibraryCode, homeLibrary)
SET
homeLibraryCode = NULLIF(@homeLibraryCode, '');

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/SFPL_DataSF_library-usage_Jan_2023.csv' IGNORE
INTO TABLE notificationPreference
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@col, @col, @col, @col, @col, @col, @col, @col, @col, notificationPreferenceCode, notificationPreference);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/SFPL_DataSF_library-usage_Jan_2023.csv'
INTO TABLE patrons
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(patronTypeCode, @col, totalCheckouts, totalRenewals, @ageRange, @homeLibraryCode, @col, @circulationActiveMonth, @circulationActiveYear, notificationPreferenceCode, @col, @providedEmailAddress, @inSanFranciscoCounty, yearRegistered)
SET
ageRange = NULLIF(@ageRange, ''),
homeLibraryCode = NULLIF(@homeLibraryCode, ''),
circulationActiveMonth = NULLIF(@circulationActiveMonth, ''),
circulationActiveYear = NULLIF(@circulationActiveYear, ''),
providedEmailAddress = (@providedEmailAddress = 'True'),
inSanFranciscoCounty = (@inSanFranciscoCounty = 'True');