# Release Notes List Builder

This transforms a JSON format issues list from JIRA
into a DocBook <itemizedlist> block element for inclusion in release notes.

To prepare your queries, edit them in JIRA's advanced mode,
and then copy them to `src/main/python/queries.cfg`.

Use the Python scripts under `src/main/python`:

*   `./menu2xml.py` reads `queries.cfg` in the same directory as the script
    and lets you select a JIRA query from a list.
    If you pass a file name argument, it dumps the list into the file.
*   `./menu2wiki.py` is like `./menu2xml.py`,
    but outputs a list in the format used in JIRA and Confluence.
*   `./jira2xml.py jira-url` dumps an `<itemizedlist>` to standard out.
    Make sure URLs are correct and quoted with 's.
    Also make sure URLs work as an anonymous user.
    (Any documentation you publish should contain
    only those issues viewable by any anonymous user.)

An example with `./menu2xml.py` follows.

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

Copyright 2012-2014 ForgeRock AS
