from pathlib import Path

people = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Tyler", "age": 34}]

def save_data(filename, dic):
    with open(filename, 'w') as data:
       for item in dic:
        values = ", ".join(str(value) for value in item.values())
        data.write(f"{values}\n")


save_data('people.txt', people)

# Need to make a function to load data back into the dictionary
def load_data(filename):
    file_path = Path(filename)
    if not file_path.exists():
        print(f"Error: The file '{filename}' does not exist.")
    
    people = []
    with open(filename, 'r') as data:
        for line in data:
            name, age = line.strip().split(", ")
            people.append({"name": name, "age": age })
    return people


#print(load_data('humans.txt'))


