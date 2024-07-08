flight_info = [('Finnair', 650.0, '10:45', '21:30')\
            , ('Cathay Pacific', 650.0, '11:30', '23:55')\
            , ('British Airways', 850.0, '08:00', '19:50')\
            , ('ANA', 1025.0, '12:00', '23:25')\
            , ('Japan Airlines', 1025.0, '06:15', '17:45')]

def flight_duration(departure_time,arrival_time):
    dep_hour,dep_mins = map(int,departure_time.split(':'))
    arr_hour,arr_mins = map(int,arrival_time.split(':'))
    
    dep_total_time = dep_hour*60 + dep_mins
    arr_total_time = arr_hour*60 + arr_mins

    if arr_total_time >= dep_total_time:
        return arr_total_time - dep_total_time
    else:
        return 24*60 + arr_total_time - dep_total_time
    
sorted_flights = sorted(flight_info,key = lambda info: (info[1],flight_duration(info[2],info[3])))


print(sorted_flights)