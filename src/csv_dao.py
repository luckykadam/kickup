from models import User, Group
from utils import csv_to_dict, csv_to_relationship


class CsvDao:
    def __init__(self, data_dir='../data'):
        self._data_dir = data_dir
        # entities
        self.users = None
        self.groups = None
        # relationships
        self.user_to_groups = None
        self.group_to_users = None

        # load data from csv files
        self.load_data()

    def load_data(self):
        # entities
        self.users = csv_to_dict(self._data_dir + '/users.csv', User)
        self.groups = csv_to_dict(self._data_dir + '/groups.csv', Group)
        # relationships
        self.user_to_groups, self.group_to_users = csv_to_relationship(self._data_dir + '/user_group.csv', self.users, self.groups)

    def add_relation(self, a_to_b, b_to_a, a, b):
        a_to_b[a].add(b)
        b_to_a[b].add(a)

    def remove_relation(self, a_to_b, b_to_a, a, b):
        a_to_b[a].remove(b)
        b_to_a[b].remove(a)
