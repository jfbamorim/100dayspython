import csv
import pandas

panda_data = pandas.read_csv("weather_data.csv")
print(panda_data['temp'])

# with open("./weather_data.csv") as weather_data:
#    data = csv.reader(weather_data)
#    temperatures = []
#    print(data)
#    for row in data:
#        print(row)
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)
    # weather_list = weather_data.readlines()
    # print(weather_list)

data_dict = panda_data.to_dict()
print(data_dict)

temp_list = panda_data['temp'].to_list()
print(temp_list)


average = sum(temp_list) / len(temp_list)
print(f"A média dos valores {average}")
# Average calculations could be:
average_mean = panda_data["temp"].mean()
print(average_mean)

# Max value
max_value = panda_data["temp"].max()
print(max_value)

# Get data in row
day_row = panda_data[panda_data.day == "Monday"]
print(day_row)

# Get row of data where temperature was at maximum
row_on_max_temp = panda_data[panda_data.temp == panda_data.temp.max()]
# row_on_max_temp = panda_data[panda_data.temp == max_value]
print(row_on_max_temp)

# Get monday temperature in Fahrenheit
monday = panda_data[panda_data.day == "Monday"]
temp_c = int(monday.temp)
temp_f = temp_c * 9/5 + 32
print(temp_f)

# Create a dataframe from scratch
student_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 88, 55]
}
data = pandas.DataFrame(student_dict)
data.to_csv("new_data.csv")
