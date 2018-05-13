from app.views import ToDoList, ToDoDetail, ToDoCreate, ToDoVote


# Setup routers for our cms app
def setup_routes(app):
    app.router.add_route('OPTIONS', '/', ToDoList)
    app.router.add_route('GET', '/', ToDoList)

    app.router.add_route('POST', '/', ToDoCreate)

    app.router.add_route('OPTIONS', '/vote/{id}', ToDoVote)
    app.router.add_route('PUT', '/vote/{id}', ToDoVote)

    app.router.add_route('OPTIONS', '/{id}', ToDoDetail)
    app.router.add_route('GET', '/{id}', ToDoDetail)
