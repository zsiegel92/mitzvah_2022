import sys
import csv
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
import datetime
from datetime import date, timedelta
from convertdate import hebrew


heads = ['timestamp','email','childname','dob','pre_sunset','hschool','school','pref_main','pref_family','pref_torah','over200','holiday_dates','nondate1','nondate2','nondate3','nondate4','sameday_party','twin','accommodations','more_info']
nondatekeys=['nondate1','nondate2','nondate3','nondate4']



infile = "Google_Submissions/Sinai Temple 2022 B'nai Mitzvah Venue Selection Form (Responses) - Form Responses 1.csv"

filein = open(infile,'r')
reader = csv.reader(filein)
headers = next(reader,None)
users = [{headers[i] : row[i] for i in range(len(headers)) if ((row[i] is not None) and (row[i] is not ''))} for row in reader]

filein.seek(0)
next(reader, None)
xheads=['xx','holiday1','holiday2','holiday3','holiday4','holiday5','holiday6','holiday7']
cleanusers = [{heads[i] : row[i] for i in range(len(heads)) if heads[i] not in xheads} for row in reader]


def users_same(u,o):
	return (u['email']==o['email']) and ((u['childname'].lower() in o['childname'].lower()) or ((o['childname'].lower() in u['childname'].lower())))


to_remove=[]
for i,user in enumerate(cleanusers):
	for other in cleanusers:
		if users_same(user,other):
			if (parse(user['timestamp']) < parse(other['timestamp'])):
				to_remove.append(i)
				print(f"REMOVING DUPLICATE USER '{user['childname']}' at INDEX {i}")
to_remove=list(set(to_remove))
cleanusers = [v for i,v in enumerate(cleanusers) if i not in to_remove]







# for user in cleanusers:
# 	print("\n"*2)
# 	print("-"*10)
# 	for k,v in user.items():
# 		print(f"{k}:{v}")
# 	print("-"*10)

print("\n"*10)
for user in cleanusers:
	print(f"'{user.get('childname')}': {{}},")



print("NON-TRIVIAL REQUESTS:\n\n")
nontrivial_needs = 0
for user in cleanusers:
	has_more_info = (user['more_info'] is not None) and(user['more_info'] != '') and (user['more_info'].lower() not in [s.lower for s in ('none','no','nothing','Not that we can think of.','no ',' no','no. ', ' no.',' no. ')])
	has_accommodations = (user['accommodations'] is not None) and (user['accommodations'] != '') and ('none' not in user['accommodations'].lower())
	if has_accommodations or has_more_info:
		nontrivial_needs += 1
		print("\n"*2)
		print("-"*20)
		print(user['childname'])
		if has_more_info:
			print("INFO:")
			print(user['more_info'])
		if has_accommodations:
			print("ACCOMMODATIONS:")
			print(user['accommodations'])

		print("-"*20)
		print("\n"*2)

print(f"\n\n{nontrivial_needs} non-trivial requests.\n\n")
# to_remove=[]
# for i,user in enumerate(cleanusers):
# 	for other in cleanusers:
# 		if users_same(user,other):
# 			if (parse(user['timestamp']) < parse(other['timestamp'])):
# 				to_remove.append(i)
# to_remove=list(set(to_remove))
# cleanusers = [v for i,v in enumerate(cleanusers) if i not in to_remove]

