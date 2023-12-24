from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.drinks import router as drinks_router
from routers.profile import router as profile_router
from routers.staff_member import router as staff_member_router
from routers.visiting_details import router as visiting_details_router
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
    current_time = datetime.now().strftime(format="%Y-%m-%d %H:%M:%S")
    return {"status": "ok", "current_time": current_time}


app.include_router(router=visitor_router, tags=["visitor"], prefix="/api/v1")
app.include_router(router=profile_router, tags=["profile"], prefix="/api/v1")
app.include_router(router=staff_member_router, tags=["staff_member"], prefix="/api/v1")
app.include_router(
    router=visiting_details_router, tags=["visiting_details"], prefix="/api/v1"
)
app.include_router(router=drinks_router, tags=["drinks"], prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run(app=app)
