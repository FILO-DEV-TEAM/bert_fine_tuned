import re

def remove_special_symbols(file_path, result_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = re.sub(r'[^\w\s가-힣]', '', content)

    #cleaned_content = re.sub(r'[\n+]', '', cleaned_content)
    cleaned_content = re.sub(r'[1234567890]', '', cleaned_content)

    #cleaned_content = re.sub(r'[\n{2,}]', '\n', cleaned_content)
    cleaned_content = re.sub(r'①', '', cleaned_content)
    cleaned_content = re.sub(r'②', '', cleaned_content)
    cleaned_content = re.sub(r'③', '', cleaned_content)
    cleaned_content = re.sub(r'④', '', cleaned_content)


    with open(result_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

def remove_blank_lines(file_path, result_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    cleaned_lines = [line for line in lines if line.strip()]

    with open(result_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)



# Example usage
file_path = './Moe files/56.txt'
result_path = './3_processed/56_out.txt'
remove_special_symbols(file_path, result_path)
remove_blank_lines(result_path, result_path)
