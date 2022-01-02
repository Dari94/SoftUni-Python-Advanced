def get_text(file_path):
    with open(file_path, 'r') as file:
        counter = 0
        list_lines = []
        for line in file:
            if counter % 2 == 0:
                list_lines.append(line)
            counter += 1
        return list_lines
        # for idx,line in enumerate(file):
        #   if idx % 2 == 0:
        #       print(line)


def replace_symbols(text):
    for line in (get_text(file_path)):
        for el in "-,.!?":
            line = line.replace(el, '@')
        words = line[:-1].split(' ')[::-1]
        print(' '.join(words))


file_path = "text.txt"
(replace_symbols(get_text(file_path)))
