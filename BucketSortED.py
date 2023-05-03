import pandas as pd

df = pd.read_csv("movie_data.csv")

num_buckets = 10

min_vote_count = df["vote_count"].min()
max_vote_count = df["vote_count"].max()

bucket_range = (max_vote_count - min_vote_count + 1) / num_buckets

buckets = []
for i in range(num_buckets):
    buckets.append([])

for index, row in df.iterrows():
    vote_count = row["vote_count"]
    bucket_index = int((vote_count - min_vote_count) // bucket_range)
    buckets[bucket_index].append(row)

for bucket in buckets:
    bucket.sort(key=lambda x: x["vote_count"])

sorted_df = pd.concat([pd.DataFrame(bucket) for bucket in buckets])

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

sorted_df