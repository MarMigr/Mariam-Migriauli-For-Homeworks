
input_date = input("Enter the date: ")

date_part, time_part = input_date.split("T")
year, month, day = date_part.split("-")


time_and_zone = time_part.split("+") if "+" in time_part else time_part.split("-")
time = time_and_zone[0]  


if len(time_and_zone) > 1:
    timezone = "+" + time_and_zone[1] 
else:
    timezone = "-" + time_and_zone[1]  


output_date = f"{day}-{month}-{year} {time} {timezone[0]}{timezone[1:]}" 


print(output_date)
