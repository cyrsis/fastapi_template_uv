from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.routers import router as main_router

app = FastAPI(
    title="Fast Template for development and Production",
    description="",
    version="11.3.1",
    contact={
        "name": "Victor Tong",
        "url": "http://x-force.example.com/contact/",
        "email": "victor@budgetapp.works",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }, )

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of origins allowed (you can use ["*"] to allow all)
    allow_credentials=True,  # Allows cookies to be sent with the requests
    allow_methods=["*"],  # List of methods allowed (you can use ["*"] to allow all)
    allow_headers=["*"],  # List of headers allowed (you can use ["*"] to allow all)
)

app.get("/")


async def docs_redirect():
    return RedirectResponse(url='/docs')


app.include_router(main_router)
