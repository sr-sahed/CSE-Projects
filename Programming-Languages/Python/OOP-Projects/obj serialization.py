import pickle

data = {"name": "Alice", "age": 25}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)  # Save to file

with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)  # Load from file

print(loaded_data)  # Output: {'name': 'Alice', 'age': 25}
