def read_and_modify_file(input_file_path, output_file_path):
    try:
        # Open the input file for reading
        with open(input_file_path, 'r') as infile:
            content = infile.read()

        # Modify the content (example: convert text to uppercase)
        modified_content = content.upper()  # You can change this modification as needed

        # Open the output file for writing the modified content
        with open(output_file_path, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File modified successfully. The new file is saved as {output_file_path}")

    except FileNotFoundError:
        print(f"The file {input_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'input.txt'  # Change this to your input file
output_file = 'output.txt'  # Change this to your output file
read_and_modify_file(input_file, output_file)
