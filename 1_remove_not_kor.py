def remove_ascii_codes(file_path, file_out, ascii_codes):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = ''.join(char for char in content if ord(char) not in ascii_codes or (55203 >= ord(char) and ord(char) >= 44032))

    with open(file_out, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

# Example usage
file_path = './MoE files/12.txt'
file_out = 'output.txt'
ascii_codes_to_remove = [\
    65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91,\
        97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122,\
            48, 49, 50, 51, 52, 53, 54, 55, 56, 57]  # ASCII codes for 'A', 'a', '0'

remove_ascii_codes(file_path, file_out, ascii_codes_to_remove)