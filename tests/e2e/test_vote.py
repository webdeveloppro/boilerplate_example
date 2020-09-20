from aiohttp.test_utils import unittest_run_loop
from aiohttp_boilerplate.test_utils import E2ETestCase


class DetailCase(E2ETestCase):
    url = '/vote/2'
    fixtures = {'todo': 'tests/fixtures/01_todo_todo.json'}

    @unittest_run_loop
    async def test_options(self):

        status, data = await self.request(
            self.url,
            'OPTIONS',
        )

        assert status == 200

    @unittest_run_loop
    async def test_put(self):

        status, data = await self.request(
            self.url,
            'PUT',
            {
                'up': True,
            }
        )

        assert status == 200
