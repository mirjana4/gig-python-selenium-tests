from typing import List
from unittest import TestCase

from api.core.users_rest_client import UsersRestClient
from api.core.entity.user import User


class TestUsers(TestCase):
    _users_client: UsersRestClient

    def setUp(self) -> None:
        self._users_client = UsersRestClient()

    def test_users_get_all(self):
        # we don't really need to get all users, so we don't need to query all pages (that way we reduce test duration time)
        users: List[User] = self._users_client.get_all_users(single_page=True)

        self.assertIsNotNone(users, msg='Users response not returned')
        self.assertGreater(len(users), 0, msg='Users list empty')

    def test_users_name_starts_with_c(self):
        # we fetch users from all pages, so we check if any of those has a name that start with letter C
        users: List[User] = self._users_client.get_all_users(single_page=False)

        self.assertIsNotNone(users, msg='Users response not returned')
        self.assertGreater(len(users), 0, msg='Users list empty')

        users_starts_with_c: List[User] = [user for user in users if user.name.lower().startswith('c')]
        self.assertGreater(len(users_starts_with_c), 0, msg='No user which name starts with letter C')

    def test_users_get_all_and_print(self):
        # same as test_users_get_all, but here we want to print all users info in the console
        users: List[User] = self._users_client.get_all_users(single_page=False)

        self.assertIsNotNone(users, msg='Users response not returned')
        self.assertGreater(len(users), 0, msg='Users list empty')

        for user in users:
            print(user)
