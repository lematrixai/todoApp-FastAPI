from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from .database.core import engine, Base
from .entities.todo import Todo  # Import models to register them
from .entities.user import User  # Import models to register them
from .api import register_routes
from .logging import configure_logging, LogLevels


configure_logging(LogLevels.info)

app = FastAPI()

Base.metadata.create_all(bind=engine)

register_routes(app)


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Lematrixai</title>
            <style>
                body {
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                }
                h1 {
                    color: #2D6936;
                }
                a {
                    padding: 12px 24px;
                    background-color: #2D6936;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 18px;
                    margin-top: 20px;
                }
                a:hover {
                    background-color: #24582A;
                }
            </style>
        </head>
        <body>
            <h1>🚀 Welcome to FastAPI App</h1>
            <a href="/docs">Open Swagger Docs</a>
        </body>
    </html>
    """