import csv
import math
import matplotlib.pyplot as plt

with open('WFC_Ortec_MatchDate_2018_Datathon.csv', 'rb') as f:
	reader = csv.reader(f)
	data = []
	cornerList =[]
	appendRow =[]
	xLocl = 0
	yLocl = 0
	xLocr =0
	yLocr=0
	xVl =[]
	yVl =[]
	xVr=[]
	yVr=[]
	xVgl =[]
	yVgl =[]
	xVgr=[]
	yVgr=[]
	distance = 0

	# the team of choice
	print('\n\nEnter the team you would like to analyze. You may choose from the following:\n')
	team = raw_input(' Portland Timbers\n Minnesota United\n Chicago Fire\n Columbus Crew\n LA Galaxy\n FC Dallas\n Real Salt Lake\n Toronto FC\n Colorado Rapids\n New England Revolution\n Sporting Kansas City\n DC United\n Seattle Sounders FC\n Houston Dynamo\n San Jose Earthquakes\n Montreal Impact\n New York City FC\n Orlando City SC\n Atlanta United\n New York Red Bulls\n Philadelphia Union\n Vancouver Whitecaps FC\n\n')

	# will contain a dict with the following
		# the entire row (ID =1, Match =2, time=5, player =8, team=11, action=12, atr =13, x = 14, y=15 
		# append angle 
		# append distance
		# append whether interception
		# append whether goal or not

	# grab csv info and place into 'data' list
	for row in reader:
		data.append(row)

# For each row in data, check if it was a corner and import the line
for i in range(0, len(data)):					
	row = data[i]
	# for right hand corners ball moves right from kickers perspective
	if row[12] == "corner" and team == row[6] and row[15] == '100':
		appendRow = row

		# find out the angle and distance of the corner by looking at the next event and append to corner
		nextRow = data[i + 1]

		# if the corner was intercepted, convert the x location
		if nextRow[11] != row[11]:
			xLocr = 100 - float(nextRow[14])
			yLocr = 100 - float(nextRow[15])
			
		else:
			xLocr = float(nextRow[14])
			yLocr = float(nextRow[15])

		# calculate distance
		distance = math.sqrt((float(row[14]) - xLocr)**2 + (float(row[15]) - yLocr)**2)	
		
		# append items to row
		appendRow.append(xLocr)
		appendRow.append(yLocr)		
		xVr.append(xLocr)
		yVr.append(yLocr)
		appendRow.append(distance)			
		
		# check the next 5 events, see if there is a goal
		for j in range(5):
			row = data[i + j]
			if row[16] == "Goal":
				appendRow.append("Y")
				xVgr.append(xLocr)
				yVgr.append(yLocr)
		# append row
		cornerList.append(appendRow)
	
	# for left hand corners ball moves left from kickers perspective
	if row[12] == "corner" and team == row[6] and row[15] == '0':
		appendRow = row

		# find out the angle and distance of the corner by looking at the next event and append to corner
		nextRow = data[i + 1]

		# if the corner was intercepted, convert the x location
		if nextRow[11] != row[11]:
			xLocl = 100 - float(nextRow[14])
			yLocl = 100 - float(nextRow[15])
			
		else:
			xLocl = float(nextRow[14])
			yLocl = float(nextRow[15])

		# calculate distance
		distance = math.sqrt((float(row[14]) - xLocl)**2 + (float(row[15]) - yLocl)**2)	
		
		# append items to row
		appendRow.append(xLocl)
		appendRow.append(yLocl)		
		xVl.append(xLocl)
		yVl.append(yLocl)
		appendRow.append(distance)			
		
		# check the next 5 events, see if there is a goal
		for j in range(30):
			row = data[i + j]
			if row[16] == "Goal":
				appendRow.append("Y")
				xVgl.append(xLocl)
				yVgl.append(yLocl)
		# append row
		cornerList.append(appendRow)

img = plt.imread("field.png")
fig, ax = plt.subplots()
axes = plt.gca()
axes.set_xlim([0,100])
axes.set_ylim([50,100])
plt.title('Corner kick attempts/goals by ' + team + ' (right)')
ax.imshow(img, extent=[0,100,50,100])
ax.plot(yVr, xVr, 'bo', yVgr, xVgr, 'ro')


img = plt.imread("field.png")
fig, ax = plt.subplots()
axes = plt.gca()
axes.set_xlim([0,100])
axes.set_ylim([50,100])
plt.title('Corner kick attempts/goals by ' + team + ' (left)')
ax.imshow(img, extent=[0,100,50,100])
ax.plot(yVl, xVl, 'bo', yVgl, xVgl, 'ro')

plt.show()
