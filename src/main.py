from csv_dao import CsvDao
from command_line_interface import CommandLineInterface
from group_manager import GroupManager


def main():
    print('initializing application')

    dao = CsvDao()
    group_manager = GroupManager(dao)
    ui = CommandLineInterface(group_manager)

    ui.cmdloop()


if __name__ == '__main__':
    main()
