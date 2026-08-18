# URL Shortener

This project is a simple implementation of the concept of a URL shortener built using Python, FastAPI, and PostgreSQL.

## Overview

A URL shortener takes a long web address and converts it into a shorter code. When a user visits the shortened link, the application looks up the corresponding original URL in the database and redirects the user to the destination.

## Features

- URL Shortening: Takes a long URL and generates a short code.
- Redirection: Automatically redirects short code requests to the original destination.
- Click Analytics: Tracks the number of times a short link has been visited.

## Project Structure

- app/main.py: Defines API endpoints for creating URLs, redirecting, and fetching analytics.
- app/database.py: Handles database connections and queries with SQLAlchemy.
- app/model.py: Defines Pydantic schemas and SQLAlchemy models.
- app/services.py: Handles short code generation logic.
- templates/: HTML files for the front-end interface and analytics display.

## How to Run

1. Install the required dependencies:
   pip install -r requirements.txt

2. Set up your environment variables:
   Create a .env file in the root directory with your database connection string:
   DATABASE_URL=postgresql+psycopg2://postgres:password@localhost:5432/url_shortner

3. Start the FastAPI server:
   uvicorn app.main:app --reload

4. Open http://127.0.0.1:8000 in your browser.
