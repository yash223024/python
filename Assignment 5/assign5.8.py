my_tuple = (1, 2, 3, 4, 5, 3, 2, 3, 6, 7, 3)


repeated_items = {item: my_tuple.count(item) for item in my_tuple if my_tuple.count(item) > 1}


print("Repeated items in the tuple:", repeated_items)