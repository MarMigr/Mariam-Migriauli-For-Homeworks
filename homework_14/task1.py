temp_for_week = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))

def avg_temp_for_day(tuples):
    return [sum(t) / len(t) for t in temp_for_week]

def max_temp_for_day(tuples):
    return [max(t) for t in temp_for_week]

def min_temp_for_day(tuples):
    return [min(t) for t in temp_for_week]

def avg_for_week(temp_for_week):
    avg_for_day = avg_temp_for_day(temp_for_week)
    return sum(avg_for_day) / len(avg_for_day)

if __name__=='__main__':
    print(f"avarage temperatures for each week-{avg_temp_for_day(temp_for_week)}")
    print(f"maximum temperatures for each week-{max_temp_for_day(temp_for_week)}")
    print(f"minimum temperatures for each week-{min_temp_for_day(temp_for_week)}")
    print(f"avarage temperature for the week -{avg_for_week(temp_for_week)}")
