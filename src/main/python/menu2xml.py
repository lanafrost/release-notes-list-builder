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

import argparse, ConfigParser, json, os, sys, urllib2

def clearTerminal():
	os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
	return

def getSelection(queries):
	config = ConfigParser.RawConfigParser()
	totalItems = len(queries) + 1
	
	clearTerminal()

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
			answer = int(raw_input('Enter your selection: '))
		except ValueError:
			print 'Invalid selection:', answer
			continue
	
		if not answer in range(1, totalItems):
			print
			print 'You selected:', answer, '(valid range: 1 -', totalItems, ')'
			print
			continue
	
		return answer

def dumpXml(url, outfile):
	response = urllib2.urlopen(url).read()
	jira = json.loads(response)

	if outfile == sys.stdout:
		clearTerminal()
	
	outfile.write('  <!-- List generated using ')
	outfile.write(url)
	outfile.write('-->\n')
	outfile.write('  <itemizedlist>\n')
	
	# This part depends on the JIRA JSON object's structure...
	for issue in jira["issues"]:
		id = issue["key"]
		desc = issue["fields"]["summary"]

		outfile.write('   <listitem><para><link xlink:href="https://bugster.forgerock.org/jira/browse/')
		outfile.write(id)
		outfile.write('" xlink:show="new">')
		outfile.write(id)
		outfile.write('</link>: ')
		outfile.write(desc)
		outfile.write('</para></listitem>\n')
		outfile.flush()
	
	outfile.write('  </itemizedlist>\n')
	
	return

parser = argparse.ArgumentParser()
parser.add_argument('file', help='dump XML output to file', nargs='?',
							type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args()

config = ConfigParser.RawConfigParser()
config.read('queries.cfg')	
queries = config.items('Queries')

url = queries[getSelection(queries) - 1][1]		# Selection starts at 1.
												# List index starts at 0.
												# Tuples are (name, url).
dumpXml(url, args.file)
