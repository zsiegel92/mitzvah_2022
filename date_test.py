from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import datetime
from datetime import date
from datetime import timedelta


today = datetime.datetime.today().date()

#Monday is 0, Saturday is 5, Sunday is 6
def dt_next_sat(dt):
	return dt + relativedelta(days = ((5 - dt.weekday()) % 7))

sat = dt_next_sat(today)

def week_to_datetime(wk,this_sat=sat):
	if wk is None:
		return "None"
	return this_sat + relativedelta(weeks=wk)


#0 is Monday, 1 is Tuesday
def dateOfDayAfterDate(date,day):
	return date + timedelta(days=(day-date.weekday()+7)%7)


def num_sat_in_month(wk):
	dt = week_to_datetime(wk)
	month = dt.month
	year = dt.year
	first_sat = dateOfDayAfterDate(date(year,month,1),5)
	if first_sat.day== dt.day:
		return 0
	elif (first_sat + relativedelta(days=7)).day == dt.day:
		return 1
	elif (first_sat + relativedelta(days=14)).day == dt.day:
		return 2
	elif (first_sat + relativedelta(days=21)).day == dt.day:
		return 3
	elif (first_sat + relativedelta(days=28)).day == dt.day:
		return 4
	elif (first_sat + relativedelta(days=35)).day == dt.day:
		return 5
	else:
		return 0


def dt_to_week(dt,this_sat=sat):
	return (dt-this_sat).days // 7


d = parse("May 15, 2019").date()
w = dt_to_week(d)


# d2 = dateOfDayAfterDate(d,5)
# print(d2)
print(f"dt_to_week(dt_next_sat(today)): {dt_to_week(dt_next_sat(today))}")
# print(f"dt_to_week(today: {dt_to_week(today)}")
print(num_sat_in_month(dt_to_week(dt_next_sat(today + relativedelta(days=28)))))










