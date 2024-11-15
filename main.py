from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

from cat_dog import routers as cat_dog_routers


app = FastAPI()

app.include_router(cat_dog_routers.router)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(request=request, name="home.html")
