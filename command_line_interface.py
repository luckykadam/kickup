from cmd import Cmd

from utils import print_entities


class CommandLineInterface(Cmd):
    prompt = 'app> '
    intro = 'welcome to application'

    def __init__(self, group_manager):
        Cmd.__init__(self)
        self.group_manager = group_manager

    def do_users(self, args):
        """print all users"""
        users = self.group_manager.all_users()
        print_entities(users)

    def do_groups(self, args):
        """print all groups"""
        groups = self.group_manager.all_groups()
        print_entities(groups)

    def do_check(self, args):
        """check if user exist in a group"""
        user_id, group_id = args.split()
        if self.group_manager.check_user_in_group(user_id, group_id):
            print('YES! user({}) is in group({})'.format(user_id, group_id))
        else:
            print('NO! user({}) is not in group({})'.format(user_id, group_id))

    def do_assign(self, args):
        """assign user to a group"""
        user_id, group_id = args.split()
        self.group_manager.add_user_to_group(user_id, group_id)
        print('successfully assigned user({}) to group({})'.format(user_id, group_id))

    def do_remove(self, args):
        """remove user from group"""
        user_id, group_id = args.split()
        self.group_manager.remove_user_from_group(user_id, group_id)
        print('successfully removed user({}) from group({})'.format(user_id, group_id))

    def do_exit(self, args):
        """exit the application"""
        print('bye')
        return True
