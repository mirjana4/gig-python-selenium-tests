from typing import List, Dict, Optional
from schema import Schema

from api.core.base_rest_client import BaseRestClient
from api.core.entity.user import User


class UsersRestClient(BaseRestClient):
    """ Users REST client """

    def get_all_users(self, single_page: bool = False) -> Optional[List[User]]:
        users: List[User] = []
        current_page: int = 1
        total_number_of_pages: int = 1

        while current_page <= total_number_of_pages:
            # "per_page" parameter partially works. We get corect number of items per page where max value is 100,
            # but the response headers are not updated correctly, so we cannot use it to condition exit from while loop
            # params: Dict = {'page': current_page, 'per_page': 100}
            params: Dict = {'page': current_page}
            response = self.request_get(path='/v2/users', params=params)
            if response.status_code != 200 or not response.content:
                return None

            json_list: List[Dict] = response.json()
            Schema([User.json_schema()]).validate(json_list)

            for item in json_list:
                user: User = User.from_json(data=item)
                users.append(user)

            if single_page:
                return users

            current_page += 1
            total_number_of_pages: int = int(response.headers.get('X-Pagination-Pages'))

        return users
