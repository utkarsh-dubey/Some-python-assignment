# Name : Utkarsh Dubey
# Roll No : 2019213
# Group : 6

import datetime
import urllib.request

def getLatestRates():

	""" Returns: a JSON string that is a response to a latest rates query.
	The Json string will have the attributes: rates, base and date (yyyy-mm-dd).
	"""
	temp=urllib.request.urlopen("https://api.exchangeratesapi.io/latest")
	tempLatestData=temp.read()												#data in bytes
	LatestData=tempLatestData.decode(encoding='utf-8',errors='strict')		#decoding the data in order to convert it from bytes to string
	return LatestData



def getvalue(data,cur,index=0):			#helper function

	"""returns the conversion value"""
	ending=data.find("}",index)
	a=data.find(cur,index,ending)
	if(a==-1  ):
		return -1
	end=data.index(',',(a+1))
	start=data.index(':',(a+1))
	
	if(ending<end ):		#for the last currency
		value=float(data[(start+1):(ending)])
	else:
		value=float(data[(start+1):(end)])

	return value

def getbase(data,index=0):			#helper function

	"""returns the base """

	a=data.find("base",index)
	base=data[a+7:a+10]
	return base

def getcurrency(data,index):	#helper function

	"""returns the currency based on the provided index """

	return data[(index-4):(index-1)]

def getdate(data,index):	#helper function

	"""returns the date present in the data in the divided form of (year,month,day)"""
	year=(data[index-12:index-8])
	month=(data[index-7:index-5])
	day=(data[index-4:index-2])
	return year,month,day




def changeBase(amount, currency, desiredCurrency, date):

	""" Outputs: a float value finalvalue.
	Requirements-date should not be before 1999-01-04 as no data of those dates is available
	"""

	temp=urllib.request.urlopen("https://api.exchangeratesapi.io/"+date)
	tempdata=temp.read()
	data=tempdata.decode(encoding='utf-8',errors='strict')

	base=getbase(data)
	if(getvalue(data,currency)==-1 or getvalue(data,desiredCurrency)==-1):
		return "Either entered currency is not available on the provided date or entered currency is invalid"
	if(currency!=base and desiredCurrency!=base):
		tempvalue=amount/getvalue(data,currency)
		finalvalue=tempvalue*getvalue(data,desiredCurrency)
	elif(currency==base and desiredCurrency!=base):
		finalvalue=amount*getvalue(data,desiredCurrency)
	elif(desiredCurrency==base and currency!=base):
		finalvalue=amount/getvalue(data,currency)
	else:
		finalvalue=amount

	return finalvalue






def printAscending(json):
	""" Output: the sorted order of the Rates
		You don't have to return anything.

	Parameter:
	json: a json string to parse

	"""
	listofrates=[]				#stores the exchange rates of all currencies 
	testlist=[]					#stores all the present currency
	data=json
	index=data.find(":")
	while True:
		
		index=data.index(':',index+1)
		currency=getcurrency(data,index)
		testlist.append(currency)
		if(data.find(':',index+1)>data.find("}")):
			break
		
		
	for x in testlist:

		listofrates.append(getvalue(data,x))

		
	for i in range(len(listofrates)-1,0,-1):		#bubblesort to arrange the exchange rates

		for j in range(i):

			if listofrates[j]>listofrates[j+1]:
			    temp = listofrates[j]
			    temp2=testlist[j]					#for mapping currency name with its exchange price
			    listofrates[j] = listofrates[j+1]
			    testlist[j]=testlist[j+1]
			    listofrates[j+1] = temp
			    testlist[j+1]=temp2


	base=getbase(data)				#stores the base of the data

	for x in range(len(listofrates)):

		print ("1",base,"=",listofrates[x],testlist[x])

	return None





def extremeFridays(startDate, endDate, currency):
	""" Output: on which friday was currency the strongest and on which was it the weakest.
		You don't have to return anything.

	Parameters:
	stardDate and endDate: strings of the form yyyy-mm-dd
	currency: a string representing the currency those extremes you have to determine
	Requirements- endDate should not be before 1999-01-04 as no data of those dates is available, currency should not 
	be equal to the base (which in this case is EUR)
	"""
	
	temp=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
	tempdata=temp.read()
	data=tempdata.decode(encoding='utf-8',errors='strict')

	minimum=100000000
	mindate=0
	maximum=0
	maxdate=0
	test=0
	index=data.index("{",1)

	while True:
		index=data.find("{",index+1)
		
		if(index==-1):
			print("No data to calculate extreme fridays")
			return None

		(year,month,day)=(getdate(data,index))
		date=datetime.datetime(int(year),int(month),int(day))
		if(date.weekday()==4):
			test=1
			if(getvalue(data,currency,index,)==-1):
				pass
			else:

				if(getvalue(data,currency,index)>maximum):
					maximum=getvalue(data,currency,index)
					maxdate=(year)+"-"+(month)+"-"+(day)
				if(getvalue(data,currency,index)<minimum):
					minimum=getvalue(data,currency,index)
					mindate=(year)+"-"+(month)+"-"+(day)
		if(data.find("{",index+1)==-1):
			break
	
	if(test==0):
		print("No friday was found in the given span of dates")
		return None
	else:
		print(currency+" was strongest on "+(mindate)+". "+"1 Euro was equal to "+str(minimum)+" "+currency)
		print(currency+" was weakest on "+maxdate+". "+"1 Euro was equal to "+str(maximum)+" "+currency)

	return None
		



	



def findMissingDates(startDate, endDate):
	""" Output: the dates that are not present when you do a json query from startDate to endDate
		You don't have to return anything.

		Parameters: startDate and endDate: strings of the form yyyy-mm-dd

		Requirements- endDate should not be before 1999-01-04 as no data of those dates is available
	"""
	temp=urllib.request.urlopen("https://api.exchangeratesapi.io/history?start_at="+startDate+"&end_at="+endDate)
	tempdata=temp.read()
	data=tempdata.decode(encoding='utf-8',errors='strict')

	dates=[]
	index=data.index("{",1)
	while True:
		index=data.find("{",index+1)
		(year,month,day)=(getdate(data,index))
		dates.append((year)+(month)+(day))
		if(data.find("{",index+1)==-1):
			break

	startyear=int(startDate[0:4])-1
	startmonth=int(startDate[5:7])-1
	startday=int(startDate[8:])
	endyear=int(endDate[0:4])
	endmonth=int(endDate[5:7])
	endday=int(endDate[8:])

	print("The following dates were not present:")
	
	while(startyear!=endyear):
		while( startmonth<12):
			while((startday<=31 and (((startmonth+1)%2!=0 and (startmonth+1)<8) or ((startmonth+1)%2==0 and (startmonth+1)>=8))) or (startday<=30 and (((startmonth+1)%2!=0 and (startmonth+1)>8 ) or ((startmonth+1)%2==0 and (startmonth+1)<8) and (startmonth+1)!=2)) or (startday<=29 and (startmonth+1)==2 and ((startyear+1)%4==0 or ((startyear+1)%100==0) and (startyear+1)%400==0)) or (startday<=28 and (startmonth+1)==2))  :
				
				if((startmonth+1)<10):
					if str(startyear+1)+"0"+str(startmonth+1)+str(startday) not in dates:
						print(str(startyear+1)+"-"+"0"+str(startmonth+1)+"-"+str(startday))
				else:
					if str(startyear+1)+str(startmonth+1)+str(startday) not in dates:
						print(str(startyear+1)+"-"+str(startmonth+1)+"-"+str(startday))
				if(startyear+1==endyear and startmonth+1==endmonth and startday==endday):
					break
				startday+=1
			if(startyear+1==endyear and startmonth+1==endmonth and startday==endday):
				break
			startmonth+=1
			startday=1
		startyear+=1
		startmonth=0

	return None	

extremeFridays("2019-10-25","2019-10-25","TRY")