import csv

with open("movie_data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = [row for row in reader]

def partition(data, low, high, index):
    pivot = data[high][index]
    i = low - 1

    for j in range(low, high):
        if data[j][index] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i+1], data[high] = data[high], data[i+1]
    return i + 1

def quick_sort(data, low, high, index):
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()

        if low < high:
            partition_index = partition(data, low, high, index)

            stack.append((low, partition_index - 1))
            stack.append((partition_index + 1, high))

vote_count = headers.index("vote_count")
quick_sort(data, 0, len(data) - 1, vote_count)

with open("sorted_movie_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for row in data:
        writer.writerow(row)

