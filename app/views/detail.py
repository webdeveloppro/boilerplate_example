from aiohttp_boilerplate.views.retrieve import RetrieveView

from app.models import ToDo
from app.schemas import ToDoDetailSchema


class ToDoDetail(RetrieveView):

    def get_model(self):
        return ToDo

    def get_schema(self):
        return ToDoDetailSchema

    async def before_get(self):
        slug = await self.get_id()
        self.where = 'slug={slug} and is_active={active}'
        self.params['slug'] = slug
        self.params['active'] = True
