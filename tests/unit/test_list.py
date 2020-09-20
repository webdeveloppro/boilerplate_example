import mock

from aiohttp.test_utils import unittest_run_loop
from aiohttp_boilerplate.test_utils import UnitTestCase


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
                    'fields': 't0.down_vote as t0__down_vote,t0.id as t0__id,t0.name as t0__name,t0.up_vote as t0__up_vote',
                    'where': 'is_active={active}',
                    'limit': 50,
                    'order': 't0.id desc',
                    'offset': None,
                    'params': {'active': True},
                    'many': True
                }
            )

            assert status == 200
