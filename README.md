# EventHub - Local Events Discovery Platform

Django Basics Regular Exam Project - A web application for discovering and managing local events, venues, and categories.

## Technologies

- **Django 5.2.1** - Web framework
- **PostgreSQL** - Database
- **Bootstrap 5** - Frontend styling

## Project Structure

```
eventhub/              # Main Django project
├── eventhub/          # Project settings
├── events/            # App: Events (CRUD, list, detail, filters)
├── venues/            # App: Venues (CRUD, list, detail)
└── categories/        # App: Categories (create, list, detail)

templates/             # Global templates
├── base.html          # Base template
├── partials/          # Reusable partials (header, footer, cards)
├── events/            # Event templates
├── venues/            # Venue templates
├── categories/        # Category templates
└── 404.html           # Custom 404 page
```

## Setup Instructions

### Prerequisites

- Python 3.10+
- PostgreSQL
- Virtual environment 

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create PostgreSQL database**
   ```sql
   CREATE DATABASE;
   ```

5. **Configure environment variables** (create `.env` or set in shell)
   ```env
   DB_NAME=
   DB_USER=
   DB_PASSWORD=
   ```

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create superuser (optional, for admin)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the server**
   ```bash
   python manage.py runserver
   ```

   Open http://127.0.0.1:8000/ in your browser.

## Features

- **Events**: Full CRUD, list with category filter and sorting, detail view
- **Venues**: Full CRUD, list, detail with upcoming events
- **Categories**: Create, list, detail with events
- Custom 404 page
- Template inheritance and reusable partials
- Custom template filters (`format_event_datetime`, `truncate_description`, `capacity_display`)
- Custom template tags (`render_event_card`, `render_venue_card`, `event_count_by_venue`)
- Bootstrap-based responsive design
- Delete confirmation for events and venues
- Form validation with user-friendly error messages
- Read-only field in Event edit form (created_at display)

