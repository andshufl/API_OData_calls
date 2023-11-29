import json

# Read JSON data from file
with open('data.json', 'r') as file:
    data = file.read()

# Load JSON data
json_data = json.loads(data)

# Write Id-Name pairs to a file
with open('file120.txt', 'w') as output_file:
    for entry in json_data:
        name = entry['Name'].split('"')[1]
        output_file.write(f'{name}:{entry["Id"]}\n')

print("Output file created: file120.txt")
