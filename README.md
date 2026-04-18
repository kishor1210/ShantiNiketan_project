# 🪷 Shanti Niketan — School Website

A responsive school website built with **FastAPI** (Python) + **HTML/CSS/JS**.

## 📁 Project Structure

```
shanti_niketan/
├── main.py                 # FastAPI app & route handlers
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Jinja2 HTML template
└── static/                 # (optional) CSS/JS/image assets
```

## ⚙️ Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
uvicorn main:app --reload
```

### 3. Open in browser
```
http://localhost:8000
```

## 🌐 API Endpoints

| Method | Path       | Description                  |
|--------|------------|------------------------------|
| GET    | `/`        | Main school website homepage |
| GET    | `/api/info`| JSON info about the school   |

## ✏️ Customizing Content

All school data is in `main.py` inside the `school_data` dictionary:
- Update `name`, `tagline`, `founded`, `address`, `phone`, `email`
- Add/edit `announcements`, `programs`, `achievements`

## 🎨 Features

- Fully responsive (mobile, tablet, desktop)
- Smooth scroll reveal animations
- Animated count-up statistics
- News ticker bar
- Admission enquiry form
- FastAPI + Jinja2 templating
