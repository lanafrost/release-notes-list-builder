This transforms a JSON format issues list from JIRA into a DocBook itemizedlist
element for inclusion in release notes.

Regarding the Python scripts:

*   `./jira2xml.py jira-url` contacts JIRA and dumps an `<itemizedlist>`
    to standard out. Make sure URLs are correct and quoted with 's.
*   `./menu2xml.py` reads `queries.cfg` in the same directory
    as the script and lets you select a JIRA query URL from a list.
    If you give this script an output file, it dumps the `<itemizedlist>`
    into the file.

An example with `./menu2xml.py` follows.

	$ ls
	jira2xml.py	menu2xml.py	queries.cfg
	$ ./menu2xml.py output.xml
	
	List of available JIRA queries
	==============================
	
		1 ) opendj 2.5.0 fixed bugs
		2 ) opendj 2.5.0 open issues
	
	Enter your selection: 2
	$ cat output.xml
	  <!-- List generated using http://bugster.forgerock.org/jira...
	  <itemizedlist>
	   <listitem><para><link xlink:href="https://bugster.forgerock.org/jira/browse...
	   ...
	  </itemizedlist>

* * *
This work is licensed under the Creative Commons
Attribution-NonCommercial-NoDerivs 3.0 Unported License.
To view a copy of this license, visit
<http://creativecommons.org/licenses/by-nc-nd/3.0/>
or send a letter to Creative Commons, 444 Castro Street,
Suite 900, Mountain View, California, 94041, USA.

Copyright 2012 ForgeRock AS
