import datetime
currentDate = datetime.datetime.now()

deadline= input ('Tulis tanggal lahir (mm/dd/yyyy) ')
deadlineDate= datetime.datetime.strptime(deadline,'%m/%d/%Y')
print (deadlineDate)
daysLeft = deadlineDate - currentDate
print(daysLeft)

years = ((daysLeft.total_seconds())/(365.242*24*3600))
yearsInt=int(years)

months=(years-yearsInt)*12
monthsInt=int(months)

days=(months-monthsInt)*(365.242/12)
daysInt=int(days)

print('Kamu berumur {0:d} tahun, {1:d}  bulan, {2:d}  hari, {3:d}  hours, {4:d} \
 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt))