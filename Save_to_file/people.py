people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Tyler", "age": 34}]

def save_data(filename, dic):
    with open(filename, 'w') as data:
        for dics in dic:
            for key, value in dics.items():
                data.write(f"{key}, {value}\n")


save_data('people.txt', people)

# Need to make a function to load data back into the dictionary
