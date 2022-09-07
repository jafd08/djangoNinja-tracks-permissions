import ninja
from tracks.api import router as tracks_router
# api = ninja.NinjaAPI()
api = ninja.NinjaAPI()

api.add_router("/tracks/", tracks_router)

@api.get("/get-result-of-add")
def add(request, a:int, b:int):
    return {"result":  a + b}


@api.get("/hello")
def hello(request, name):
    return f"Hello {name}!"

class HelloSchema(ninja.Schema):
    name: str = "world"

@api.post("/hello")
def hello(request, data:HelloSchema):
    return f"Hello {data.name}"



class UserSchema(ninja.Schema):
    username: str
    is_authenticated : bool
    # unathenticated users will not have the following fields so we will provide defaults:
    email: str = None
    first_name: str = None
    last_name: str = None


@api.get("/me", response=UserSchema)
def me(request):
    return request.user



# Multiple response types:

class UserSchema2(ninja.Schema):
    username: str
    email: str
    first_name: str
    last_name = str

class Error(ninja.Schema):
    message : str

@api.get("/me2", response={200:UserSchema2, 403: Error})
def me2(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user