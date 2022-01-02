def get_text(file_path):
    with open(file_path, 'r') as file:
        counter = 0
        list_lines = []
        for line in file:
            list_lines.append(line)
        return list_lines


def count_symbols(text):
    count = 0
    result = ""
    for line in (get_text(file_path)):
        count += 1
        symbol_line = [el for el in line if el in "-,.!?'"]
        letter_line = [el for el in line if el not in "-,.!?' \n"]

        result += f"Line {count}: {line[0:-1]} ({len(letter_line)})({len(symbol_line)})\n"
    return result


def write_file(writen_file):
    with open(writen_file, 'w') as w_file:
        w_file.write(str(count_symbols(get_text(file_path))))


file_path = "text.txt"
writen_file = "output.txt"
print(count_symbols(get_text(file_path)))
write_file(writen_file)


