from fastapi import FastAPI
from routers import file_routes

app = FastAPI(
    title="Chat-Driven Excel Manipulation API",
    description="Upload, manipulate, and download Excel files via chat-driven API",
    version="1.0.0",
)

# Include routes
app.include_router(file_routes.router, prefix="/file", tags=["Excel Operations"])
