# Open the input file for reading
with open('input_file.txt', 'r') as input_file:
    # Read the contents of the file
    contents = input_file.read()

# Replace multiple spaces with a single space
contents = ' '.join(contents.split())

# Open the output file for writing
with open('output_file.txt', 'w') as output_file:
    # Write the modified contents to the output file
    output_file.write(contents)
