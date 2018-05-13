from aiohttp.test_utils import unittest_run_loop
from aiohttp_boilerplate.tests import E2ETestCase


class ListTest(E2ETestCase):
    url = '/'
    fixtures = {'todo': 'tests/fixtures/01_todo_todo.json'}

    @unittest_run_loop
    async def test_list(self):

        status, data = await self.request(
            self.url,
            'GET',
        )
        assert status == 200
        assert len(data['data']) == 1
