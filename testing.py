# import pandas as pd

# # Create a DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'London', 'Paris']
# }

# df = pd.DataFrame(data)
# print(df)

tuples = (0, 2, 4, 6, 8)
print("Original tuple:",tuples)

# Convert the tuple to a list
mylist = list(tuples)
print("Converting tuple to list:",mylist)
print("Type",type(mylist))
mylist.append(10)
print(mylist)
tup = tuple(mylist)
print(tup)
print(type(tup))