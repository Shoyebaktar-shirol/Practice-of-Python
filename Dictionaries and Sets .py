dict = {
    "Name": "Shoyebaktar",
    "sgpa": 8.92,
    "Country": "India",
    "Subjects": {
        "Cyber": 99,
        "Python": 98,
        "Multimedia Animation": 92,
        "Daa": 98,
        "R Programming": 95
    }
}

# Printing all the keys in dictionary
print(dict.keys())

# Printing all the values in dictionary
print(dict.values())

# Printing key-value pairs of dictionary all
print(dict.items())

# Adding new Key
dict.update({"Age": 17, "City": "Delhi"})
print(dict)
