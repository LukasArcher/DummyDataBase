import re
import os
import pickle
import gzip
import json
from files_handler.select_spaces_and_columns import select_spaces_columns


class FilesHandler:
    @staticmethod
    def create_file_and_write(file_name, content):
        with open(file_name, 'w') as f:
            f.write(f'{content}\n')

    @staticmethod
    def add_to_file(file_name, content):
        with open(file_name, 'r') as f:
            head_line = f.readline()
            file_num_of_columns = len(head_line.split(','))
            content_num_of_columns = len(content.split(','))

        with open(file_name, 'a') as f:
            if file_num_of_columns == content_num_of_columns:
                f.write(f"{content}\n")
            else:
                print('Error!')


    @staticmethod
    def select_from_file(file_name, content):
        num_spaces, num_columns = select_spaces_columns(file_name)

        with open(file_name, 'r') as f:
            head_line = f.readline()

            if content != '*':
                selected = re.search(content, head_line, re.I)
                head_line_list = head_line.split(',')
                index = [i for i in range(len(head_line_list))
                         if head_line_list[i].replace('\n', '') == selected.group()][0]
                print(selected.group())
                print('-----------')

                for line in f:
                    print(line.split(',')[index].replace('\n', ''))
            else:
                head_line_list = head_line.split(',')

                for i in range(len(head_line_list)):
                    print(head_line_list[i].replace('\n', '').ljust(num_spaces), end='|')

                print('\n' + '-'*(num_spaces*num_columns+(num_columns - 1)), end='|\n')

                for line in f:
                    for val in line.split(','):
                        print(val.replace('\n', '').ljust(num_spaces), end='|')
                    print()

    @staticmethod
    def delete_from_file(file_name, column, value):
        column = column[0]
        value = value[0]
        match_count = 0
        index = None
        with open(file_name, 'r') as f:

            content = f.readline()
            head_line = content.split(',')
            for i in range(len(head_line)):
                if re.fullmatch(column, head_line[i].replace('\n', '')):
                    index = i
                    break
            for line in f:
                if re.fullmatch(value, line.split(',')[index].replace('\n', '')):
                    match_count += 1
                    continue

                content += line
        if match_count != 0:
            with open(file_name, 'w') as f:
                print(match_count)
                f.writelines(content)
        else:
            print("There is no such a value in that column!")

    def export_files(self, file_names):
        for file in file_names:
            if os.path.exists(f'{file}.ddo'):
                with open(f'{file}.ddo', 'r') as f:
                    content = f.readlines()
                    with gzip.open(f'{file}.pkl.gz', 'wb') as zip_f:
                        pickle.dump(content, zip_f)
                        print(os.path.abspath(f'{file}.pkl.gz'))
            else:
                print(f'{file}.ddo does not exist!')

    def import_files(self, file_path):
        zipped_file_name = file_path.split('\\')[-1]
        unzipped_file_name = f"{zipped_file_name.split('.')[0]}.ddo"
        if os.path.exists(zipped_file_name):
            if os.path.abspath(zipped_file_name) == file_path:
                with gzip.open(zipped_file_name, 'rb') as zip_f:
                    content = pickle.load(zip_f)
                    with open(unzipped_file_name, 'w') as f:
                        f.writelines(content)
                        print(os.path.abspath(unzipped_file_name))
            else:
                print('Wrong path!')

        else:
            print('The file does not exist!')

    def json_converter(self, file_name):
        ddo_file = f'{file_name}.ddo'
        json_file = f'{file_name}.json'
        if os.path.exists(ddo_file):
            with open(ddo_file, 'r') as f:
                head_line = f.readline()
                lines = ''
                for line in f:
                    lines += line
            head_line_columns = head_line.replace('\n', '').split(',')
            single_lines = lines.split('\n')
            for line in single_lines:
                values = line.split(',')
                # for values
    #
    #       Trochę się zakręciłem z tym jsonem i nie wiem czy w ogóle w dobrym kierunku idę xD
    #
            # with open(json_file, 'w') as f:
            #     f.write(json.dumps(content, indent=4))
            # with open(json_file, 'r') as f:
            #     print(f.readlines())

        else:
            print("The file does not exist!")
