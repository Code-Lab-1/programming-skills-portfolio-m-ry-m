#Get a key with minimun value in a dictionary
dict = {
    'Math': 82,
    'Physics': 65,
    'Chemistry': 75
}
print(min(dict, key=dict.get))
