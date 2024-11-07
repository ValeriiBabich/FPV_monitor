# Open the original binary file in read-binary mode
with open('damp_5802d_ant_a.BIN', 'rb') as f:
    binary_content = f.read()

# List of frequency values as bytes
frequencies = [
    b'5865M', b'5845M', b'5825M', b'5805M', b'5785M', b'5765M', b'5745M', b'5725M', 
    b'5733M', b'5752M', b'5771M', b'5790M', b'5809M', b'5828M', b'5847M', b'5866M',
    b'5705M', b'5685M', b'5665M', b'5645M', b'5885M', b'5905M', b'5925M', b'5945M',
    b'5740M', b'5760M', b'5780M', b'5800M', b'5820M', b'5840M', b'5860M', b'5880M',
    b'5658M', b'5695M', b'5732M', b'5769M', b'5806M', b'5843M', b'5880M', b'5917M',
    b'5653M', b'5693M', b'5733M', b'5773M', b'5813M', b'5853M', b'5893M', b'5933M',
    b'5333M', b'5373M', b'5413M', b'5453M', b'5493M', b'5533M', b'5573M', b'5613M',
    b'5325M', b'5348M', b'5366M', b'5384M', b'5402M', b'5420M', b'5438M', b'5456M',
    b'5474M', b'5492M', b'5510M', b'5528M', b'5546M', b'5564M', b'5582M', b'5600M',
    b'4990M', b'5020M', b'5050M', b'5080M', b'5110M', b'5140M', b'5170M', b'5200M'
]

# Function to add a null byte separator (\x00) after each frequency
def add_separators(frequencies):
    with_separators = []
    for freq in frequencies:
        with_separators.append(freq + b'\x00')  # Add \x00 to each frequency
    return with_separators

# Apply the separator addition function to all frequencies
frequencies_with_separators = add_separators(frequencies)

# Define the starting position for the new data block in the binary file
new_block_start = 0x0001F000

# Join all the frequency values with separators into a single bytes object
new_block_content = b''.join(frequencies_with_separators)

# Create a new binary content by inserting the new block at the specified position
new_binary_content = (
    binary_content[:new_block_start] +          # Keep original content up to new block start
    new_block_content +                         # Insert new frequency block
    binary_content[new_block_start + len(new_block_content):]  # Append remaining original content
)

# Define the path for the modified file
new_file_path = 'damp_5802d_ant_a_modified.BIN'

# Write the modified binary content to the new file
with open(new_file_path, 'wb') as f:
    f.write(new_binary_content)

# Output a message indicating that the modified file was saved successfully
print(f"Modified file saved as {new_file_path}")
