# Goal: Create a csv with a header: Fur color and Count based on 2018_Central_Park_Squirrel_Census.csv
import pandas

# First read the csv file to a dataframe panda
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Get the counts
count_grey_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
count_black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
count_cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

# Build a dictionary so it is possible to build a csv file
data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Color": [count_grey_squirrels, count_black_squirrels, count_cinnamon_squirrels]
}

# DataFrame from dictionary to CSV
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

