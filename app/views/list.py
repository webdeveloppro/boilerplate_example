from aiohttp_boilerplate.views.list import ListView

from app.models import ToDo
from app.schemas import ToDoListSchema


class ToDoList(ListView):

    def get_model(self):
        return ToDo

    def get_schema(self):
        return ToDoListSchema

    async def before_get(self):
        self.where = 'is_active={active}'
        self.params['active'] = True
        self.order = 't0.id desc'
