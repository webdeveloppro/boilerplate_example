import mock

from aiohttp.test_utils import unittest_run_loop
from aiohttp_boilerplate.tests import UnitTestCase


class ListCase(UnitTestCase):
    url = '/'

    async def select(self, **args):
        return []

    @unittest_run_loop
    async def test_options(self):

        status, data = await self.request(
            self.url,
            'OPTIONS',
        )
        assert status == 200

    @unittest_run_loop
    async def test_list(self):

        with mock.patch('aiohttp_boilerplate.models.SQL.select') as mSelect:
            mSelect.side_effect = self.select

            status, data = await self.request(
                self.url,
                'GET',
            )

            mSelect.assert_called_once_with(
                **{
                    'fields': '*',
                    'where': 'is_active={active}',
                    'limit': 50,
                    'order': '"id" desc',
                    'params': {'active': True},
                    'many': True
                }
            )

            assert status == 200
