import datetime

def parseDatetime(result):

	date = datetime.datetime.now()

	if result == 'today' :
		result = date.today().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
		print result
	elif result == 'yestoday':
		result = date.today().replace(hour = 0, minute = 0, second = 0, microsecond = 0) - datetime.timedelta(days = 1)
		print result
	else:
		result = datetime.datetime.strptime(result, "%Y-%m-%d")
	
	return result

