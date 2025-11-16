SELECT patronType.patronType, COUNT(*) AS numPatrons FROM patrons 
JOIN patronType ON patronType.patronTypeCode = patrons.patronTypeCode
GROUP BY patrons.patronTypeCode;

SELECT homeLibrary.homeLibrary, COUNT(*) AS numPatrons FROM patrons
JOIN homeLibrary ON homeLibrary.homeLibraryCode = patrons.homeLibraryCode
GROUP BY homeLibrary.homeLibrary
ORDER BY numPatrons DESC;

SELECT SUM(totalCheckouts) AS numCheckouts, SUM(totalRenewals) AS numRenewals FROM patrons;

SELECT inSanFranciscoCounty, COUNT(*) AS numInSFCounty FROM patrons GROUP BY inSanFranciscoCounty;

SELECT COUNT(*) AS numWrongAgeSeniors FROM patrons WHERE patronTypeCode = 3 AND ageRange = '0 to 9 Years';

SELECT COUNT(*) AS numNoEmailProvided FROM patrons WHERE notificationPreferenceCode = 'z'
AND providedEmailAddress IS FALSE;