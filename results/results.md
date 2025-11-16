The database script generally takes over 10 seconds to run, as shown in 'loadtime.png'. When imported this way, if a string if empty, it does not appear to be equal to null. This may make it harder to search many of the fields that may have empty values, but in the case of the circulation active month (the patron's most recent activity), if it is empty, then the year, which is a number and can be null, is also empty. Running a query on the database usually takes around a quarter of a second, and one should expect it not to take more than one second.

The entire library system has had 70,412,694 total checkouts and 33,101,214 total renewals.

There are 31 library branches in the system. The main branch has by far the most patrons, at 143,471. The one with the least is Ocean View at 3,476. Another 2,097 patrons use the Bookmobile, and another 127 have an unknown home library. The same library branch may be represented by multiple codes, but I could not find the reason.

Out of the 437,115 patrons in the database by default, there are:

271,588 adults

58,767 juveniles

40,340 teens

47,366 seniors

808 staff members

8 businesses

The rest of the patrons come from several other types that I could not find information on, and would require further clarification to understand how one would fit into those categories. Whether or not they overlap is not important, as these categories inform the user about borrowing limits rather than the actual demographic status of the patron.

Of these patrons, 369,259 of them are within San Francisco County, while the remaining 67,856 are not.

There does not seem to be any constraint or other safeguard on the 'ageRange' data. For example, I found 8 instances where a senior patron has their age range listed as '0 to 9 Years'.
In addition, I found 476 instances of a patron having 'email' listed as their preferred notification type, but did not provide an email address. This may be either an error in the database or a feature of the service used to register patrons.

The SQL queries I used to obtain this information are in the 'queries' script in this folder.