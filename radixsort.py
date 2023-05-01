import pandas as pd

df = pd.read_csv("movie_data.csv", index_col=0)
df = df.to_dict('records')

def counting_sort(data, digit):
    size = len(data)

    output = [0] * size
    count = [0] * 10

    for i in range(size):
        index = data[i]["vote_count"] // digit
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    
    for i in range(size - 1, -1, -1):
        index = data[i]["vote_count"] // digit
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1

    for i in range(size):
        data[i] = output[i]

def radix_sort(data):
    MAX = max(data, key=lambda x: x["vote_count"])["vote_count"]

    digit = 1
    while MAX // digit > 0:
        counting_sort(data, digit)
        digit *= 10

radix_sort(df)
df = pd.DataFrame(df)
df.to_csv("RADIX_movie_data.csv")