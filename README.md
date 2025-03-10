# Employee and Task Management System

## Description
The ** Employee and Task Management System** is a Django-based web app for managing employee records. It offers user authentication, real-time updates via WebSockets, and an intuitive UI. Designed to simplify HR tasks, it ensures secure and efficient employee data management.

## Features
- Employee record management (Add, Edit, Delete)
- Secure authentication for admin users
- Real-time updates using Django Channels
- Export data functionality with OpenPyXL and ReportLab
- Cross-origin support with Django CORS Headers

## Installation
### Prerequisites
- Python 3.x
- Django

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   ```
2. Navigate to the project directory:
   ```sh
   cd office_emp_proj
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser for admin access:
   ```sh
   python manage.py createsuperuser
   ```
7. Start the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Access the app at `http://127.0.0.1:8000/`
- Log in using the admin credentials
- Manage employee records through the provided UI

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.

