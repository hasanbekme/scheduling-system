# Django Tutoring Schedule API

This is a Django-based API for managing tutoring schedules, including students, tutors, subjects, and availability management.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd scheduler
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env file with your secret key
```

5. Navigate to the source directory:
```bash
cd src
```

6. Run database migrations:
```bash
python manage.py migrate
```

7. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

8. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

- `/api/students/` - Student management
- `/api/tutors/` - Tutor management
- `/api/subjects/` - Subject management
- `/api/availability/` - Availability management

## Admin Interface

Access the admin interface at `http://localhost:8000/admin/` to manage all models.

## Development

The project uses Django REST framework for API development. Main components:

- `schedule/models.py` - Data models
- `schedule/serializers.py` - API serializers
- `schedule/views.py` - API views
- `schedule/urls.py` - URL routing
