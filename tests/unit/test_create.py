import mock

from aiohttp.test_utils import unittest_run_loop
from aiohttp_boilerplate.sql import consts as sql_consts
from aiohttp_boilerplate.test_utils import UnitTestCase


class DetailCase(UnitTestCase):
    url = '/'

    async def create(self, *args, **kargs):
        return ""

    @unittest_run_loop
    async def test_create_no_data(self):

        with mock.patch('aiohttp_boilerplate.models.SQL.insert') as mSelect:
            mSelect.side_effect = self.create

            status, data = await self.request(
                self.url,
                'POST',
                {
                }
            )

            '''
            ToDo
            Check validation message
            '''

            assert status == 400

    @unittest_run_loop
    async def test_create(self):

        with mock.patch('aiohttp_boilerplate.models.SQL.insert') as mSelect:
            mSelect.side_effect = self.create

            dataPost = {
                'name': 'new todo',
                'slug': 'new-todo',
                'content': '...',
            }

            status, data = await self.request(
                self.url,
                'POST',
                dataPost,
            )

            mSelect.assert_called_once_with(
                data=dataPost,
            )

            assert status == 201
