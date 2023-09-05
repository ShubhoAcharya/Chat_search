from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Mount the 'static' folder to serve frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_chatbot():
    # Read the index.html file and return it as the response
    with open("static/HTML/index.html", "r") as file:
        html_content = file.read()
    return html_content

input_data=[]

@app.post("/chat")
async def chat_with_bot(request: Request):
    data = await request.json()
    user_input = data["user_input"]


    # Replace this API call with your chatbot logic
    # For now, we'll simply echo back the user's input
    
    response = {"response":user_input}

    return response