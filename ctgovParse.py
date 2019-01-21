import xml.etree.ElementTree as ET
import glob
import numpy as np
import csv



#Extract title
def extractTitle(root):
	title = ''
	for offTitle in root.iter('official_title'):
		title = offTitle.text

	#If there is no official title
	if title == '':
		for briefTitle in root.iter('brief_title'):
			title = briefTitle.text
	
	return title


#Extract status
def extractStatus(root):
	status = ''
	for stat in root.iter('overall_status'):
		status = stat.text

	return status

#Extract condition
def extractCondition(root):
	condition = ''
	for cond in root.iter('condition'):
		condition = cond.text

	return condition

#Extract detailed description
def extractDescription(root):
	description = ''
	for descrip in root.iter('detailed_description'):
		description = descrip[0].text

	return description



#Extract NCTID
def extractNct(root):
	nct = ''
	for id in root.iter('nct_id'):
		nct = id.text

	return nct

#Extract year
def extractYear(root):
	date = ''
	for dt in root.iter('start_date'):
		date = dt.text
	date = date[-4:]

	return date


#Parse file
def main():

	path = input('Please specify the complete path to where the files of ctgov2016_2017 dataset are present: ')
	fileList = glob.glob(path + '/*.xml')
	count = 0

	row = ['ID', 'Title', 'Status', 'Year', 'Condition', 'Description']
	with open('./ctgovTest.csv','w') as f:
		writer = csv.writer(f)
		writer.writerow(row)

		for file in fileList:
	
			title = ''
			status = ''
			condition = ''
			description = ''
			nctID = ''
			year = ''

			tree = ET.parse(file)
			root = tree.getroot()
	
			title = extractTitle(root)
			status = extractStatus(root)
			condition = extractCondition(root)
			description = extractDescription(root)
			nctID = extractNct(root)
			year = extractYear(root)

			#print('nctID: ',nctID)

			row = [nctID, title, status, year, condition, description]
			writer.writerow(row)
			count += 1
			
			if (count % 100) == 0:
				print('\nNumber of files parsed: ', count)
if __name__ == '__main__':
	main()
