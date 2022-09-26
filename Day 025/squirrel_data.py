import pandas

data = pandas.read_csv("data/squirrel_data.csv")
new_df = pandas.DataFrame(data["Primary Fur Color"].value_counts())
new_df.to_csv("data/squirrel_count.csv")
