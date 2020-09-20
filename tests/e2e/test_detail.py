import json

from aiohttp.test_utils import unittest_run_loop
from aiohttp_boilerplate.test_utils import E2ETestCase

from app.schemas import ToDoDetailSchema


class DetailCase(E2ETestCase):
    url = '/{slug}'
    fixtures = {'todo': 'tests/fixtures/01_todo_todo.json'}

    @unittest_run_loop
    async def test_options(self):
        SLUG = 'options'

        status, data = await self.request(
            self.url.format(slug=SLUG),
            'OPTIONS',
        )

        assert status == 200

    @unittest_run_loop
    async def test_inactive_non_exists(self):
        SLUG = 'inactive'
        status, data = await self.request(
            self.url.format(slug=SLUG),
            'GET',
        )

        assert status == 404
        assert data == {'__error__': 'No object found'}

        SLUG = 'none_exist'
        status, data = await self.request(
            self.url.format(slug=SLUG),
            'GET',
        )

        assert status == 404
        assert data == {'__error__': 'No object found'}

    @unittest_run_loop
    async def test_active(self):
        SLUG = 'purpose'

        status, data = await self.request(
            self.url.format(slug=SLUG),
            'GET',
        )

        assert status == 200

        # ToDo
        # Create some helper method in tests
        cleared_data = json.loads(ToDoDetailSchema().dumps(self.loaded_fixtures['todo'][1]).data)
        cleared_data['id'] = self.loaded_fixtures['todo'][1]['id']
        del data['up_vote']
        del data['down_vote']
        assert data == cleared_data
