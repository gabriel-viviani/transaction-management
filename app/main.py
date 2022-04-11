from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from entrypoint.router import api_router
from repository.database import init_db

app = FastAPI()
app.include_router(api_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"message": str(exc)}
    )


@app.get("/ping", status_code=status.HTTP_200_OK)
async def ping():
    return {"message": "pong"}


init_db()
