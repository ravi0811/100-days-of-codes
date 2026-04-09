import pandas

data= pandas.read_csv(r"data\french_words.csv")

to_learn= data.to_dict(orient="records")
print(to_learn)
