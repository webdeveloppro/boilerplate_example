from aiohttp_boilerplate.views.create import CreateView

from app.models import ToDo
from app.schemas import ToDoDetailSchema


class ToDoCreate(CreateView):

    def get_model(self):
        return ToDo

    def get_schema(self):
        return ToDoDetailSchema
