def getMonth(month):
  if month == 1:
	return "Nisan"
  elif month == 2:
	return "Iyyar"
  elif month == 3:
	return "Sivan"
  elif month == 4:
	return "Tammuz"
  elif month == 5:
	return "Av"
  elif month == 6:
	return "Elul"
  elif month == 7:
	return "Tishri"
  elif month == 8:
	return "Heshvan"
  elif month == 9:
	return "Kislev"
  elif month == 10:
	return "Teveth"
  elif month == 11:
	return "Shevat"
  elif month == 12:
	if date_utils.calendar_util.hebrew_leap(year):
	  return "Adar I"
	else:
	  return "Adar"

  elif month == 13:
	return "Adar II"

def getWeekday(julian):
	weekday = (int(julian) + 2) % 7
	return weekday

def getLastDayOfGregorianMonth(month, year):
	if month == 2 and date_utils.calendar_util.leap_gregorian(year):
		return 29
	else:
		month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		return month_days[month-1]

