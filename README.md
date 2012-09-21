This transforms a JSON format issues list from JIRA into a DocBook itemizedlist
element for inclusion in release notes.

Regarding the Python scripts:

*   `./jira2xml.py jira-url` contacts JIRA and dumps an `<itemizedlist>`
    to standard out. Make sure URLs are correct and quoted with 's.
*   `./menu2xml.py` reads `queries.cfg` in the same directory
    as the script and lets you select a JIRA query URL from a list.

* * *
This work is licensed under the Creative Commons
Attribution-NonCommercial-NoDerivs 3.0 Unported License.
To view a copy of this license, visit
<http://creativecommons.org/licenses/by-nc-nd/3.0/>
or send a letter to Creative Commons, 444 Castro Street,
Suite 900, Mountain View, California, 94041, USA.

Copyright 2012 ForgeRock AS
