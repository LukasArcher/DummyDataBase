def select_spaces_columns(file_name):
    with open(file_name, 'r') as f:
        num_spaces = 0
        num_columns = 0
        for line in f:
            num_columns = len(line.split(','))
            for v in line.split(','):
                if num_spaces < len(v):
                    num_spaces = len(v) + 1
        return num_spaces, num_columns
