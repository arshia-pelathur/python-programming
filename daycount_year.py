import calendar


class MyCalendar(calendar.Calendar):
    def __init__(self,year,weekday):
        super().__init__()
        self.year = year
        self.weekday = weekday

    
    def count_weekday_in_year(self):
        month_matrix = []
        for month in range(1,13):
            month_matrix.append(self.monthdays2calendar(self.year,month))
        flattened_months = [day_monthweek for month in month_matrix for week in month for day_monthweek in week]
        
        count = 0
        for day_monthweek in flattened_months:
            if (day_monthweek[0] !=0) and (day_monthweek[1] == self.weekday):
                count+=1
        return count

mycal = MyCalendar(2000,6)
count_ina_year = mycal.count_weekday_in_year()
print(count_ina_year)