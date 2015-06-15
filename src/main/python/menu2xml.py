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
#     Copyright 2012-2014 ForgeRock AS

import argparse, datetime, ConfigParser, json, os, sys, urllib, urllib2
from xml.sax.saxutils import escape

def clearTerminal():
	os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
	return

def getSelection(queries):
	totalItems = len(queries) + 1

	clearTerminal()

	answer = 0
	while True:
		print 'List of available JIRA queries'
		print '=============================='
		print
		i = 1
		for k,v in queries:
			print '\t', i, ')' , k
			i = i+1
		print

		try:
			answer = raw_input('Enter your selection: ')
		except ValueError:
			print 'Invalid selection:', answer
			continue

		if not answer.isdigit() or not int(answer) in range(1, totalItems):
			print
			print 'You selected:', answer, '(valid range: 1 -', totalItems - 1, ')'
			print
			continue

		return int(answer)

def dumpXml(url, outfile):
	timestamp = datetime.datetime.now()
	response = urllib2.urlopen(url).read()
	jira = json.loads(response)

	if outfile == sys.stdout:
		clearTerminal()

	outfile.write('  <!-- List generated at ')
	outfile.write(timestamp.strftime('%H:%M:%S %Y%m%d'))
	outfile.write(' using ')
	outfile.write(url)
	outfile.write('-->\n')
	outfile.write('  <itemizedlist>\n')

	# This part depends on the JIRA JSON object's structure...
	count = 0
	for issue in jira["issues"]:
		id = issue["key"]
		desc = escape(issue["fields"]["summary"]).encode('utf-8')

		outfile.write('   <listitem><para><link xlink:href="https://bugster.forgerock.org/jira/browse/')
		outfile.write(id)
		outfile.write('" xlink:show="new">')
		outfile.write(id)
		outfile.write('</link>: ')
		outfile.write(desc)
		outfile.write('</para></listitem>\n')
		outfile.flush()
		count += 1

	outfile.write('  </itemizedlist>\n')
	outfile.write('  <!-- Issue count: ' + str(count) + ' -->\n')

	return

parser = argparse.ArgumentParser()
parser.add_argument('file', help='dump XML output to file', nargs='?',
							type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args()

config = ConfigParser.RawConfigParser()
config.optionxform=str
config.read('queries.cfg')
queries = config.items('Queries')

pre  = "http://bugster.forgerock.org/jira/rest/api/2/search?jql="
post = "&startAt=0&maxResults=500&fields=summary"

query = queries[getSelection(queries) - 1][1]	# Selection starts at 1.
												# List index starts at 0.
												# Tuples are (name, query).
url = pre + urllib.quote_plus(query) + post

dumpXml(url, args.file)
