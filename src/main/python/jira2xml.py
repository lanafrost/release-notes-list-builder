#!/usr/bin/python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# If applicable, add the following below this MPL 2.0 HEADER, replacing
# the fields enclosed by brackets "[]" replaced with your own identifying
# information:
#     Portions Copyright [yyyy] [name of copyright owner]
#
#     Copyright 2012 ForgeRock AS

import argparse, json, sys, textwrap, urllib2

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
								description='Build DocBook itemizedlist from JIRA query',
								epilog=textwrap.dedent('''
									Quote the URLs using 's.
									
									Fixed bugs in OpenDJ 2.5.0:
									    'http://bugster.forgerock.org/jira/rest/api/2/search?jql=project+%3D+OPENDJ+AND+fixVersion+%3D+%222.5.0%22+AND+component+%21%3D+documentation+AND+type+%3D+Bug+and+resolution+%3D+Fixed+and+priority+%21%3D+Trivial&startAt=0&maxResults=200&fields=summary'
									
									Open issues in OpenDJ 2.5.0:
										'http://bugster.forgerock.org/jira/rest/api/2/search?jql=project+%3D+OpenDJ+and+affectedVersion+%3D+%222.5.0%22+and+(resolution+%3D+Unresolved+or+(resolution+%3D+fixed+and+fixVersion+!%3D+%222.5.0%22))+and+component+!%3D+documentation+and+type+%3D+Bug&startAt=0&maxResults=200&fields=summary'
								'''))
parser.add_argument('url', help='JIRA search URL returning JSON that contains issues.')
args = parser.parse_args()


response = urllib2.urlopen(args.url).read()
jira = json.loads(response)

print '  <!-- List generated using ', args.url, '-->'
print '  <itemizedlist>'

for issue in jira["issues"]:
	id = issue["key"]
	desc = issue["fields"]["summary"]
	sys.stdout.write('   <listitem><para><link xlink:href="https://bugster.forgerock.org/jira/browse/')
	sys.stdout.write(id)
	sys.stdout.write('" xlink:show="new">')
	sys.stdout.write(id)
	sys.stdout.write('</link>: ')
	sys.stdout.write(desc)
	sys.stdout.write('</para></listitem>\n')
	sys.stdout.flush()

print '  </itemizedlist>'
