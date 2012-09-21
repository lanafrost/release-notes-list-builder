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

def dumpXml(url):
	response = urllib2.urlopen(url).read()
	jira = json.loads(response)

	clearTerminal()
	
	print '  <!-- List generated using ', url, '-->'
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
	
	return

# TODO use output file
#parser = argparse.ArgumentParser()
#parser.add_argument('file', help='Dump XML output to this file')
#args = parser.parse_args()

config = ConfigParser.RawConfigParser()
config.read('queries.cfg')	
queries = config.items('Queries')

url = queries[getSelection(queries) - 1][1]		# Selection starts at 1.
												# List index starts at 0.
												# Tuples are (name, url).
dumpXml(url)
