import os

from fastapi import APIRouter, Request, UploadFile
from starlette.templating import Jinja2Templates

from cat_dog.classifier import classify
from settings import settings


router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.post("/classify/")
async def check_result(request: Request, file: UploadFile):
    save_path = os.path.join(settings.UPLOAD_FOLDER, file.filename)

    with open(save_path, "wb") as buffer:
        buffer.write(await file.read())

    pet, percents = classify(settings.CAT_DOG_MODEL, save_path)

    return templates.TemplateResponse(
        request=request,
        name="classify.html",
        context={"pet": pet, "percents": percents}
    )
