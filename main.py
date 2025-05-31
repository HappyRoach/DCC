import api
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="DCC",
    description="API для системы управления доставкой",
    version="1.0.0",
    openapi_version="3.0.2"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9667)
