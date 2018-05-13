from aiohttp_boilerplate.sql import consts
from aiohttp_boilerplate.views.update import UpdateView

from app.models import ToDo
from app.schemas import VoteSchema


class ToDoVote(UpdateView):

    def get_model(self):
        return ToDo

    def get_schema(self):
        return VoteSchema

    async def perform_update(self, where, params, data):
        where = 'id={id}'
        params['id'] = await self.get_id()
        set_query = ""

        if data['up'] is True:
            set_query = 'up_vote+1'
        else:
            set_query = 'up_vote-1'

        # Since we want to pass string value for the integer
        # We need to create our own sql request
        res = await self.obj.sql.execute(
            "UPDATE {} set up_vote={} where {}".format(
                self.obj.table,
                set_query,
                self.obj.sql.prepare_where(where, params, 0)
            ),
            params,
            consts.FETCHVAL,
        )
        if res:
            return int(res.split(' ')[-1])
        return None

    async def get_data(self, data):
        return {}
