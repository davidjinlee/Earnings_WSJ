# Earnings_WSJ
Scrap Earnings from Wall Street Journal

import time
import urllib
from bs4 import BeautifulSoup

ofInterest = []

try:
	for eachStock in ofInterest:
		url = urllib.urlopen('http://quotes.wsj.com/'+eachStock+'/financials/annual/income-statement').read()

		soup = BeautifulSoup(url,'html.parser')

		fulldata = []
		PageTable = []
		PageHeader = []

		table = soup.find('table')				#finds all tables
		table_rows = soup.find_all('tr')		#finds rows in table
		table_headers = soup.find_all('th')
		

		for tr in table_rows:
			td = tr.find_all('td')				#finds data in each row
			row = PageTable.append([i.text for i in td])

		for metrics in PageTable:
			if 'Sales/Revenue' in metrics:
				print eachStock
				for data in metrics:
					if len(data) > 0:
			 			print data

			if 'Net Income' in metrics:
				for data in metrics:
					if len(data) > 0:
			 			print data

		print '--------------------------'

	time.sleep(1)
		
except Exception,e:
	print 'failed in the main loop',str(e)
