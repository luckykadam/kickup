from exceptions import UnknownUser, UnknownGroup, UserNotInGroup, UserAlreadyInGroup


class GroupManager:
    def __init__(self, dao):
        self.dao = dao

    def all_users(self):
        return self.dao.users

    def all_groups(self):
        return self.dao.groups

    def check_user_in_group(self, user_id, group_id):
        return group_id in self.dao.user_to_groups[user_id] and user_id in self.dao.group_to_users[group_id]

    def add_user_to_group(self, user_id, group_id):
        # validation
        if user_id not in self.dao.users:
            raise UnknownUser
        if group_id not in self.dao.groups:
            raise UnknownGroup
        if group_id in self.dao.user_to_groups[user_id] and user_id in self.dao.group_to_users[group_id]:
            raise UserAlreadyInGroup

        self.dao.add_relation(self.dao.user_to_groups, self.dao.group_to_users, user_id, group_id)

    def remove_user_from_group(self, user_id, group_id):
        # validation
        if user_id not in self.dao.users:
            raise UnknownUser
        if group_id not in self.dao.groups:
            raise UnknownGroup
        if group_id not in self.dao.user_to_groups[user_id] and user_id not in self.dao.group_to_users[group_id]:
            raise UserNotInGroup

        self.dao.remove_relation(self.dao.user_to_groups, self.dao.group_to_users, user_id, group_id)
