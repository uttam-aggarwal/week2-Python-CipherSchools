# in keyword and iterations in dictionary
user_info={
    'name':'uttam',
    'age': 18,
    'fav_movies': ['dark'],
    'fav_tunes': ['perfect','shape of you'],
}

# check if key exist in dictionary
#if 'names' in user_info:
#    print('present')
#else:
#   print('not present')

# check if value exist in dictionary
# if 'uttam' in user_info.values():
#  print('present')
# else:
# print('not present')
# loop in dictionaries
# for i in user_info.values():
#    print(i)
#values method
# user_info_values= user_info.values()
# print(user_info_values)
# print(type(user_info_values))

# items method
# user_items= user_info.items()
# print(user_items)
# print(type(user_items))
for i, j in user_info.items():
    print(f"key is {i} and value is{j}")
