#The calendar master :-)
import Hlokza_Handy_Functions as mf


#this list contains all dates in multiple formats

allDates = []

yearDays = 365.25
allMonths = {"January":31,"February":28,
			"March":31,"Aprill":30,"May":31,
			"Jun":30,"Jully":31,"August":31,
			"September":30,"October":31,
			"November":30,"December":31}

weekDays = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
weekDaysInv = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
weekType = {"weekend":(6,7),"weekDay":(1,2,3,4,5)}

# Get the full calendar from excel to compare
#calFull = mf.readCsv("Cal.txt","rt","|")
#print(calFull)


#This function returns a dictionary of years and weekdays i.e {1900: 'Monday'}
#doomsDay1List(year) this is the maximum year
def doomsDay1List(year):
	y1 = 1901
	y2 = 1902
	wd1 = "Tuesday"
	leap = "false"
	weekCount = 2
	dmdList = {}
	


	if year > y1:
		#initialize the list
		dmdList[y1] = wd1
		#loop through years
		for i in range(y2,year+1):
			# if year is divisable by 4, then it is roughly a leap year			
		#	print(str(i%4))
		#	print("The year is "+str(i))

			if (i-1)%400==0 and (i-1)%100==0 and (i-1)%4==0:		#is divisible by 4
				leap = "true"
		#		print("leap is true")
				if weekCount == 7:
					weekCount = 2
				elif weekCount <= 5:
					weekCount += 2
				elif weekCount == 6:
					weekCount = 1
			elif (i-1)%400>0 and (i-1)%100==0 and (i-1)%4==0: #Not a leap year
				leap = "false"
				if weekCount <=6:
					weekCount += 1
				else:
					weekCount = 1					
			elif (i-1)%4==0:
				leap = "true"
		#		print("leap is true")
				if weekCount == 7:
					weekCount = 2
				elif weekCount <= 5:
					weekCount += 2
				elif weekCount == 6:
					weekCount = 1
			else:	
				leap = "false"
				if weekCount <=6:
					weekCount += 1
				else:
					weekCount = 1	

			dmdList[i] = weekDays[weekCount]

	return dmdList


#ti = doomsDay1List(2323)

#print(ti)

#Delete from here---------------------------------------------------------------------------------------------------
#ti is a dictionary {2093:"Thursday"}
#calFull is list in list [["2320","Thursday","leap"]]
#calFulldic {2223:"Wednesday"}
# ti is limmited
#check_i = ["Row","RealCalendar","MyCalendar","Status"]

#create dictionary from full calendar
#calFulldic = {}
#for i in calFull:
#	calFulldic[int(i[0])] = i[1]
#print(calFulldic)
#check using the limitations of ti
#rr = 1
#for ix in ti:
#	st =""
#	if calFulldic[ix] == ti[ix]:
#		st = "Good"
#	elif calFulldic[ix] != ti[ix]:
#		st = "Broken"	
#	e =(rr,ix,calFulldic[ix],ti[ix],st)
#	check_i.append(e)
#	rr += 1
#for i in check_i:
#	print(i)
#print(check_i)

#Delete till here---------------------------------------------------------------------------------------------------



#This function takes the weekday(dic key) and returns "weekDay" or "weekEnd"
def whatWeek(weekDayKey):
	for j in weekDays:
		if j in weekType["weekend"]:
			#print(str(j)+" Weekend")
			if j == weekDayKey:
				return "weekEnd"
		elif j in weekType["weekDay"]:
			#print(str(j)+" working day")
			if j == weekDayKey:
				return "weekDay"

#uu =whatWeek(6)	
#print(uu)		

#This function creates all the months taking the leap year into concideration
def createMonths(cyear):
	cMonths = {"January":31,"February":28,
			"March":31,"Aprill":30,"May":31,
			"Jun":30,"Jully":31,"August":31,
			"September":30,"October":31,
			"November":30,"December":31}

	if cyear%400==0 and cyear%100==0 and cyear%4==0: #is divisible by 4
		leap = "true"
		cMonths["February"]= 29
	#	print(str(cyear)+" is a leap year")
	#	print("the diff is: "+str(diff))		
	elif cyear%400>0 and cyear%100==0 and cyear%4==0: #Not a leap year
		leap = "false"
		cMonths["February"]= 28
	#	print(str(cyear)+" is not a leap year")		
	elif cyear%4==0: # is a leap year
		leap = "true"
		cMonths["February"]= 29
	#	print(str(cyear)+" is a leap year")
	#	print("the diff is: "+str(diff))		
	else: #is false
		leap = "false"
		cMonths["February"]= 28
	#	print(str(cyear)+" is not a leap year")
	return cMonths	

#for k in range(1900,2070):
#	gv =createMonths(k)
#	print(k)
#	print(gv)

#for i in allDays:
#	print(allDays[i])			

#for i in allMonths:
#	print(i+" "+str(allMonths[i]))

#Create calendar function
#inputs:
#start and end dates
#outputs:
#[rowid,year,month,day]

# Start is the start year i.e 2008
# genCalendar(2008,2010)
#This function returns [rowid,year,month,day]
def genCalendar(start,end):
	row = 1
	leap = "false"
	currYear = start
	counterDay = 0
	diff = 0
	weekDayCount = 1
	yearDayList = doomsDay1List(2293) #{2229:"Thursday"}
#	print(yearDayList)
	if start < end:
		counterYear = 1
		diff = end - start+1
	elif start > end:
		counterYear = -1
		diff = start - end+1
	elif start == end:
		print("start is equal to end")	
		diff = 1

	#loop through the years
	for i in range(0,diff):
		#yearDayList	#{2229:"Thursday"}
		#weekDays = {1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
		#weekDaysInv = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
		# if year is divisable by 4, then it is roughly a leap year	
		weekDayCount = weekDaysInv[yearDayList[currYear]]
		#print(str(currYear)+" "+weekDays[weekDayCount])

		alMnths = createMonths(currYear)
		#loop through months
		for k in alMnths: #allMonths = {"January":31,"February":28,
			#print(k)
			#print(str(currYear)+" "+k)

			#loop through days
			for dy in range(1,alMnths[k]+1):
				#[rowid,year,month,day]
				#loop through weeks
			#	print(str(row)+"| "+ str(currYear)+" |"+k+" |"+str(dy))
				ww = whatWeek(weekDayCount)
				fullDateData =(row,currYear,k,dy,weekDays[weekDayCount],ww) #(rowNumber INT,Year INT,Month STR,Day INT,WeekDay STR,WeekType STR)
				allDates.append(fullDateData)
				row +=1
				if weekDayCount == 7:
					weekDayCount = 1
				else:	
					weekDayCount += 1

		currYear += counterYear

	return allDates



#tt = genCalendar(2008,2009)

#delete after use================================================Start
#for k in tt:
#	print(k)

#delete after use================================================End






#This function extends the business month by n days
#inputs [externsion number,start year, end year,List of exeptions(dates)]
#allMonths = {"January":31,"February":28,

def businessCalendar(exN,startYear,EndYear,CalendarType,ExpDates):
	bc = []
	#genCalendar(X,Y) (rowNumber INT,Year INT,Month STR,Day INT,WeekDay STR,WeekType STR) 
	generalCal = genCalendar(startYear,EndYear)
	#loop through generalCal,
	#add business month next to calendar month
	#at the end of the cal month count exN
	#while exn is not max business month is prev month
	rj = 0
	exNCount = 1
	exNCountReset = 0
	weekendCount = 0
	bm = ""

	#weekDaysInv = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
	#weekType = {"weekend":(6,7),"weekDay":(1,2,3,4,5)}

	for i in generalCal:
		#loop through exN to extend business month
		#start with "if its a weekend"
		theMonths = createMonths(i[1])
		if exNCount == 1:
			exNCount = exN + theMonths[i[2]] + exNCountReset + weekendCount
			bm = i[2]
			newCal = (i[0],i[1],i[2],bm,i[3],i[4],i[5])
			#print(i[2]+" : "+str(theMonths[i[2]])) # Not taking leap years into concideration
			#print("count=1 The exNCount is: "+str(exNCount)+" "+str(i[1])+" "+i[2]+" "+str(i[3])+" bm is "+bm+" and the resert is: "+str(exNCountReset))
			exNCountReset = 0
			weekendCount = 0
		elif exNCount > 1:	 
			newCal = (i[0],i[1],i[2],bm,i[3],i[4],i[5])
			exNCount -= 1
			if i[2] !=bm:
				exNCountReset -= 1
			#	if i[5] == "weekEnd":
			#		weekendCount += 1
			#print("count>1 The exNCount is: "+str(exNCount)+" "+str(i[1])+" "+i[2]+" "+str(i[3])+" bm is "+bm)
		bc.append(newCal)	
		rj +=1
		#print(bc)
	for k in bc:
		print(k)	


businessCalendar(3,2008,2009,"typeOfCalendar","None")