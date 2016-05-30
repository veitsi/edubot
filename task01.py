# this program is not absolutelly proper and calculates hours
# when all months has 30 days. real months have different days number
# but it is not so important in our case
print ("my name is Sergio Feldman")
print ("I have a crazy dream to teach programming all people in Ukraine")
hours_per_workingday = 3
hours_per_weekendday = 5
total_per_week = 5*hours_per_workingday + 2*hours_per_weekendday
total_per_month = 4.2 * total_per_week
total_per_year = 12 * total_per_month
print("every week I spent "+str(total_per_week)+" hours to study and code python")
print("every year I spent "+str(int(total_per_year))+" hours to study and code python")
