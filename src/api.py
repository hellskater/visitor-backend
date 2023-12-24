import datetime
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.visitor import router as visitor_router


app = FastAPI()


app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/health", tags=["health"], response_model=dict[str, str])
async def health_check() -> dict[str, str]:
    current_time = datetime.datetime.now().strftime(format="%Y-%m-%d %H:%M:%S")
    return {"status": "ok", "current_time": current_time}


app.include_router(router=visitor_router, tags=["visitor"])


if __name__ == "__main__":
    uvicorn.run(app=app)
