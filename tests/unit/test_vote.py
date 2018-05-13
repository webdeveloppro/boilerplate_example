import mock

from aiohttp.test_utils import unittest_run_loop
from aiohttp_boilerplate.sql import consts as sql_consts
from aiohttp_boilerplate.tests import UnitTestCase


class DetailCase(UnitTestCase):
    url = '/vote/2'

    async def execute(self, *args, **kargs):
        return " 2"

    @unittest_run_loop
    async def test_put_up(self):

        with mock.patch('aiohttp_boilerplate.models.SQL.execute') as mSelect:
            mSelect.side_effect = self.execute

            status, data = await self.request(
                self.url,
                'PUT',
                {
                    'up': True,
                }
            )

            mSelect.assert_called_once_with(
                'UPDATE todo_todo set up_vote=up_vote+1 where id=$1',
                {'id': 2},
                sql_consts.FETCHVAL,
            )

            print(data)
            assert status == 200

    @unittest_run_loop
    async def test_put_down(self):

        with mock.patch('aiohttp_boilerplate.models.SQL.execute') as mSelect:
            mSelect.side_effect = self.execute

            status, data = await self.request(
                self.url,
                'PUT',
                {
                    'up': False,
                }
            )

            mSelect.assert_called_once_with(
                'UPDATE todo_todo set up_vote=up_vote-1 where id=$1',
                {'id': 2},
                sql_consts.FETCHVAL,
            )

            assert status == 200
