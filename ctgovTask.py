import csv
import matplotlib.pyplot as plt
import numpy as np


idDict = {}
yearDict = {}
conditionDict = {}
years = []
year_frequency = []

#Plot the graph for year frequency of the trials
def plot_bar_x(years, year_frequency):
	print(years)
	# this is for plotting purpose
	index = np.arange(len(years))
	plt.bar(index, year_frequency)
	plt.xlabel('Year', fontsize=5)
	plt.ylabel('No of Studies', fontsize=5)
	plt.xticks(index, years, fontsize=5, rotation=30)
	plt.yticks(year_frequency, fontsize=5, rotation=30)
	
	plt.title('Number of Studies for years 1957-2020')
	plt.show()

def plot_year_condition(years):
	inp_cond = input("Enter the conditon: ")

	condition_frequency = []
	for yr in years:
		count = 0
		for elem in yearDict[yr]:
			if elem['Condition']==inp_cond:
				count += 1
		condition_frequency.append(count)



    # this is for plotting purpose
	index = np.arange(len(years))
	plt.bar(index, condition_frequency)
	plt.xlabel('Year', fontsize=5)
	plt.ylabel('No of Studies', fontsize=5)
	plt.xticks(index, years, fontsize=5, rotation=30)
	plt.yticks(condition_frequency, fontsize=5, rotation=30)
	plt.title('Number of Studies for years 1957-2020 for ' + str(inp_cond))
	plt.show()









#Add entry to idDict
def addID(id, title, status, year, condition, description):
	if id not in idDict.keys():
		idDict[id] = [{'Title': title, 'Status': status, 'Year': year, 'Condition': condition, 'Description': description}]
	
	else:
		idDict[id].append({'Title': title, 'Status': status, 'Year': year, 'Condition': condition, 'Description': description})


#Add entry to yearDict
def addYear(id, title, status, year, condition, description):
	if year not in yearDict.keys():
		yearDict[year] = [{'NCTID': id, 'Title': title, 'Status': status, 'Condition': condition, 'Description': description}]

	else:
		yearDict[year].append({'NCTID': id, 'Title': title, 'Status': status, 'Condition': condition, 'Description': description})


#Add entry to conditionDict
def addCondition(id, title, status, year, condition, description):
	if condition not in conditionDict.keys():
		conditionDict[condition] = [{'NCTID': id, 'Title': title, 'Status': status, 'Year': year, 'Description': description}]

	else:
		conditionDict[condition].append({'NCTID': id, 'Title': title, 'Status': status, 'Year': year, 'Description': description})


#Search for a trial based on NCTID
def searchById():
	id = input("Please enter the NCT ID: ")

	if id not in idDict.keys():
		print("No record exists for NCT ID: ", id)
	
	else:
		print("Here is the trial with NCTID: ", id)
		for trial in idDict[id]:
			print("*", trial['Title'])
			print("\n")

#Search for a trial based on year
def searchByYear():
	year = input("Please enter the year: ")

	if year not in yearDict.keys():
		print("No trial exists in year: ", year)

	else:
		print("Here is the list of trials started in the year: ", year)
		for trial in yearDict[year]:
			print("*", trial['Title'])
			print("\n")

#Search for a trial based on condition
def searchByCondition():
	condition = input("Please enter the condtion: ")

	if condition not in conditionDict.keys():
		print("No related trial found for the condition: ", condition)

	else:
		print("Here is the list of trials related to the condition: ", condition)
		for trial in conditionDict[condition]:
			print("*", trial['Title'])
			print("\n")
# Parse the csv file
def parseCsv():
	count = 0
	
	with open('ctgovTest.csv',newline='') as f:
		reader = csv.reader(f)
		header = next(reader)
		for row in reader:
			id = row[0]
			title = row[1]
			status = row[2]
			year = row[3]
			condition = row[4]
			description = row[5]


			addID(id,title,status,year,condition,description)
			addYear(id,title,status,year,condition,description)
			addCondition(id,title,status,year,condition,description)
			
			count +=1
			if (count%100 == 0):
				print("\n Number of trials processed: ", count)

	global years
	years  = [y for y in yearDict.keys()]
	print(years)
	input()
	years.sort()
	for y in years:
	    year_frequency.append(len(yearDict[y]))

# Main application
def main():
	
	parseCsv()
	print(years)
	input()
	while(True):
		print("Enter your choice from the following list of options")
		print("\n 1 Search for a trial based on NCT ID" + 
			"\n 2 Search for a trial based on start year" +
			"\n 3 Search for trials related to a condition" +
			"\n 4 View the number of trials started over different years" +
			"\n 5 View the number of trials related to a condition started over different years" +
			#"\n 6 View the number of trials according to their status" +
			"\n 7 Exit the application")

		choice = input()
		
		#if choice not in range(1,8):
		#	print("Invalid option, Please choose from the displayed list of options")

		if choice == "1":
			searchById()
		
		elif choice == "2":
			searchByYear()

		elif choice == "3":
			searchByCondition()

		elif choice == "4":
			plot_bar_x(years, year_frequency)

		elif choice == "5":
			plot_year_condition(years)

		elif choice == "7":
			break

if __name__ == "__main__":
	main()
