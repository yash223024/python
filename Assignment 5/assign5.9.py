tuples_list = [(1, 2, 3), (-1, 4, 5), (0, -2, 3), (7, 8, 9), (-5, -6, -7)]


positive_tuples = [tup for tup in tuples_list if all(x > 0 for x in tup)]


print("Tuples with all positive elements:", positive_tuples)