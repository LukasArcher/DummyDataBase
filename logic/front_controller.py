from user_interface.user_interface import UserInterface
from logic.commands_interpreter import CommandInterpreter
from logic.create_logic import CreateLogic


class FrontController:
    def __init__(self):
        self.ui = UserInterface()
        self.ci = CommandInterpreter()
        self.cl = CreateLogic()

        self.ui.say_hello()

    def run(self):
        while True:
            command = self.ui.user_input()
            command_name, document_name, columns, values = self.ci.interpret(command)
            if command_name == 'create':
                self.cl.create(document_name, columns)
            elif command_name == 'add':
                self.cl.add_values(values, document_name)
            elif command_name == 'select':
                self.cl.select_column(columns, document_name)
            elif command_name == 'delete':
                self.cl.delete(document_name, columns, values)
            elif command_name == 'export':
                self.cl.export(document_name)
            elif command_name == 'import':
                self.cl.import_from_path(document_name)
            elif command_name == 'json':
                self.cl.json_creator(document_name)


