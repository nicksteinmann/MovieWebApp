# MoviWeb App

A Flask web application for managing users and their favorite movies.

## Features

- Create and delete users
- View a user's movie list
- Add movies using the OMDb API
- Update movie titles
- Delete movies
- Prevent duplicate movies for the same user
- Custom 404 error page
- Responsive card-based layout

## Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML / CSS
- OMDb API
- python-dotenv

## Project Structure

MovieWebApp/
├── app.py
├── data_manager.py
├── models.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── data/
│   └── movies.db
├── static/
│   └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── movies.html
    └── 404.html

## Setup Instructions

Clone the repository:

git clone https://github.com/nicksteinmann/MovieWebApp.git  
cd MovieWebApp  

Create and activate virtual environment:

Windows:
python -m venv .venv  
.venv\Scripts\activate  

Mac/Linux:
python3 -m venv .venv  
source .venv/bin/activate  

Install dependencies:

pip install -r requirements.txt  

Create a .env file in the root directory and add:

OMDB_API_KEY=your_api_key_here  

## Run the Application

python app.py  

Then open in browser:

http://127.0.0.1:5000  

## Deployment / Codio Support

The app is configured to run with environment-based ports.

It automatically uses:
- PORT from environment (Codio / hosting)
- fallback to port 5000 locally

The server runs on:

host = 0.0.0.0  

So it works for:
- local development
- Codio
- deployment environments

## OMDb API

This project uses the OMDb API to fetch movie data such as:

- Title
- Director
- Year
- Poster

## Notes

- Do NOT upload your .env file to GitHub
- Database is stored locally in data/movies.db
- Duplicate movies are prevented per user

## Author

Nick Steinmann