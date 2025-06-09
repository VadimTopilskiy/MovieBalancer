from random import random
from fastapi import APIRouter, Depends, Request
from starlette.responses import RedirectResponse
from urllib.parse import urlparse
from db.database import get_db
from service.config import _get_config

redirect_router = APIRouter()


@redirect_router.get("/")
async def redirect_logic(request: Request, db=Depends(get_db)):
    video_url = request.query_params.get("video")
    if not video_url:
        return {"error": "Missing video query param"}

    config = await _get_config(db)
    if not config:
        return {"error": "Config not set"}

    probability = 1 / config.ratio
    send_to_origin = random() < probability

    if send_to_origin:
        redirect_url = video_url
    else:
        parsed = urlparse(video_url)
        path_parts = parsed.path.split("/")
        origin_server = path_parts[1]
        rest_path = "/".join(path_parts[2:])
        redirect_url = f"http://{config.cdn_host}/{origin_server}/{rest_path}"

    return RedirectResponse(url=redirect_url, status_code=301)
