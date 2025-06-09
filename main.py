import uvicorn
import socket
from fastapi import FastAPI
from api import routers

app = FastAPI()
app.include_router(routers)


@app.get("/whoami")
async def whoami():
    return {"instance": socket.gethostname()}


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
