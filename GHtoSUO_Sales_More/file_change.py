# Specify the input and output file names
input_file_name = 'file120.txt'
output_file_name = 'file120.txt'

# Open the input file for reading
with open(input_file_name, 'r') as input_file:
    # Read lines from the input file
    lines = input_file.readlines()

# Open the output file for writing
with open(output_file_name, 'w') as output_file:
    # Process each line and write to the output file
    for line in lines:
        key, value = line.strip().split(':')
        output_file.write(f'{key};I:{value}\n')

print(f"Output file created: {output_file_name}")
