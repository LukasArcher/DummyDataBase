import re


class CommandInterpreter:
    def __init__(self):
        self.VALID_REGEX = {
            'create':   {
                'regex': '\s*CREATE\s+DOCUMENT\s+(\w*)\s+\((.*)\)'
            },
            'add':      {
                'regex': '\s*ADD\s+\((.*)\)\s+TO\s+(\w*)'
            },
            'select':   {
                'regex': '\s*SELECT\s+\((.*)\)\s+FROM\s+(\w*)'
            },
            'delete': {
                'regex': '\s*DELETE\s+FROM\s+(\w*)\s+WHERE\s+(.*)=(.*)'
            },
            'export': {
                'regex': '\s*EXPORT\s+DATA\s+FROM\s+(.*)'
            },
            'import': {
                'regex': '\s*IMPORT\s+FROM\s+(.*)'
            },
            'json': {
                'regex': '\s*JSON\s+(\w*)'
            }
        }

    def interpret(self, command):
        for command_name, vr in self.VALID_REGEX.items():
            selected_command = re.findall(vr['regex'], command, re.I)
            if len(selected_command):
                if type(selected_command[0]) == tuple:
                    selected_command = selected_command[0]

                document_name = None
                columns = None
                values = None
                if command_name == "create":
                    document_name = selected_command[0]
                    columns = selected_command[1]
                elif command_name == "add":
                    values = selected_command[0]
                    document_name = selected_command[1]
                elif command_name == "select":
                    columns = selected_command[0]
                    document_name = selected_command[1]
                elif command_name == "delete":
                    document_name = selected_command[0]
                    columns = selected_command[1]
                    values = selected_command[2]
                elif command_name == "export":
                    document_name = selected_command[0]
                    document_name = document_name.replace(' ', '').split(',')
                elif command_name == "import":
                    document_name = selected_command[0]
                elif command_name == "json":
                    document_name = selected_command[0]

                if columns is not None:
                    columns = columns.replace(' ', '').split(',')

                if values is not None:
                    values = values.replace(' ', '').split(',')

                return command_name, document_name, columns, values


