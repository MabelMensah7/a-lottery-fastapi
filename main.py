from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()

# Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Lottery play endpoint
@app.post("/play", response_class=HTMLResponse)
def play_lottery(
    request: Request,
    num1: int = Form(...),
    num2: int = Form(...),
    num3: int = Form(...),
    num4: int = Form(...),
    num5: int = Form(...),
):
    # User's numbers
    user_numbers = {num1, num2, num3, num4, num5}

    # Machine draws 5 random numbers from 1-90
    machine_numbers = set(random.sample(range(1, 91), 5))

    # Check matches
    matches = user_numbers.intersection(machine_numbers)
    count = len(matches)

    # Prize logic
    if count == 5:
        prize = "Jackpot! GHS 1,000,000 💰"
    elif count == 4:
        prize = "Great! GHS 50,000 💰"
    elif count == 3:
        prize = "Nice! GHS 500 💰"
    elif count == 2:
        prize = "Small win: GHS 50 💰"
    elif count == 1:
        prize = "You matched 1 number: GHS 10 💰"
    else:
        prize = "No matches. Better luck next time!"

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "user_numbers": sorted(user_numbers),
            "machine_numbers": sorted(machine_numbers),
            "matches": sorted(matches),
            "count": count,
            "prize": prize,
        },
    )
"""to run server.. uvicorn main:app --reload"""