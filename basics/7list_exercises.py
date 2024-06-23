matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)
print(matrix2)
print(matrix2[2])

a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)
print(a)
print(a[3][3])

countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
countries2 = [country for sublist in countries for country in sublist if len(country) < 4]
print(countries2)



countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
# This is a nested list (2D list) where each sublist contains country names.

countries2 = [country for sublist in countries for country in sublist if len(country) < 4]
# This can be understood step by step:

# Step 1: for sublist in countries

# This iterates over each sublist in the countries list.
# For the first iteration, sublist will be ['Egypt', 'USA', 'India'].
# For the second iteration, sublist will be ['Dubai', 'America', 'Spain'].
# For the third iteration, sublist will be ['London', 'England', 'France'].
# Step 2: for country in sublist

# For each sublist, this inner loop iterates over each country in that sublist.
# For the first sublist ['Egypt', 'USA', 'India'], the inner loop will iterate over Egypt, USA, and India.
# For the second sublist ['Dubai', 'America', 'Spain'], it will iterate over Dubai, America, and Spain.
# For the third sublist ['London', 'England', 'France'], it will iterate over London, England, and France.
# Step 3: if len(country) < 4

# This is a conditional check that includes a country in the result list only if its length is less than 4 characters.
# For example, Egypt (length 5) will not be included, but USA (length 3) will be included.
# Step 4: country

# This is the item that will be included in the resulting list if it passes the conditional check.
# country will be added to countries2 if its length is less than 4 characters.
print(countries2)

matrix = [[j for j in range(4)] for i in range(4)] 
print(matrix)

# Outer Loop: for i in range(4) creates 4 sublists (one for each iteration of i from 0 to 3).
# Inner Loop: for j in range(4) generates a list of numbers from 0 to 3 for each iteration of i.
# Result: The list comprehension combines these sublists into a 4x4 matrix where each sublist contains [0, 1, 2, 3]