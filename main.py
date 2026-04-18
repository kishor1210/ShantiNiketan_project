from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Shanti Niketan School")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Lookup table for students and teachers by program
staff_lookup = {
    "Pre-Primary": {"students": 40, "teachers": 2},
    "Primary School": {"students": 60, "teachers": 3},
    "Middle School": {"students": 50, "teachers": 2},
    "Secondary School": {"students": 30, "teachers": 2},
    "Senior Secondary": {"students": 20, "teachers": 1},
}

school_data = {
    "name": "Shanti Niketan",
    "tagline": "Where Knowledge Blossoms",
    "founded": 2028,
    "students": 200,
    "teachers": 10,
    "programs": 24,
    "address": "Jahanpur, Araria Bihar, Pin- 854329",
    "phone": "9674412942",
    "email": "info@shantiniketan.edu.in",
    "staff_lookup": staff_lookup,
    "announcements": [
        {"title": "Annual Day Celebration", "date": "May 10, 2026", "desc": "Join us for a grand celebration of talent and achievement."},
        {"title": "Science & Innovation Fair", "date": "April 28, 2026", "desc": "Students showcase inventions and research projects."},
        {"title": "Summer Camp Registrations Open", "date": "April 20, 2026", "desc": "Enroll now for our enriching summer programs."},
    ],
    "programs": [
        {"name": "Pre-Primary", "grades": "Nursery – KG", "icon": "🌱"},
        {"name": "Primary School", "grades": "Grade 1 – 5", "icon": "📚"},
        {"name": "Middle School", "grades": "Grade 6 – 8", "icon": "🔬"},
        {"name": "Secondary School", "grades": "Grade 9 – 10", "icon": "🎓"},
        {"name": "Senior Secondary", "grades": "Grade 11 – 12", "icon": "🏛️"},
        {"name": "Sports & Arts", "grades": "All Grades", "icon": "🎨"},
    ],
    "achievements": [
        {"title": "State Science Olympiad", "result": "1st Place – 2025"},
        {"title": "CBSE Board Results", "result": "100% Pass Rate – 2025"},
        {"title": "Inter-School Debate", "result": "Champions – 2025"},
        {"title": "National Sports Meet", "result": "Gold Medal – Athletics"},
    ]
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, **school_data})

@app.get("/api/info")
async def info():
    return {
        "school": school_data["name"],
        "founded": school_data["founded"],
        "students": school_data["students"],
        "teachers": school_data["teachers"],
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
