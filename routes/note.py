from fastapi import APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


from config.db import conn
from Schema.note import noteEntity, notesEntity

note = APIRouter()
templates = Jinja2Templates(directory="templates")
@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.Notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs" : newDocs})

@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    note = conn.Notes.notes.insert_one(dict(form))
