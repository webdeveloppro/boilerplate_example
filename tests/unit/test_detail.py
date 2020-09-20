import mock

from aiohttp.test_utils import unittest_run_loop
from aiohttp_boilerplate.test_utils import UnitTestCase


class DetailCase(UnitTestCase):
    url = '/{slug}'

    async def select(self, **args):
        print('hello ', args)
        if args['params']['slug'] == 'inactive':
            return None
        return {'id': 1}

    @unittest_run_loop
    async def test_inactive(self):

        with mock.patch('aiohttp_boilerplate.models.SQL.select') as mSelect:
            mSelect.side_effect = self.select

            SLUG = 'inactive'
            status, data = await self.request(
                self.url.format(slug=SLUG),
                'GET',
            )

            assert status == 404

    @unittest_run_loop
    async def test_active(self):

        with mock.patch('aiohttp_boilerplate.models.SQL.select') as mSelect:
            mSelect.side_effect = self.select

            SLUG = 'active'
            status, data = await self.request(
                self.url.format(slug=SLUG),
                'GET',
            )

            assert data['id'] == 1
            assert status == 200
