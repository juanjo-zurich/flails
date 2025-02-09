# Flails Framework

Flails is a Python web application framework built on top of Flask, providing a robust foundation for building web applications with built-in authentication, admin interface, and database integration.

## Features

- Built on Flask 3.1.x
- Integrated authentication system
- Admin interface using Flask-Admin
- Database integration with SQLAlchemy
- CLI tools for project scaffolding
- SQLite as default database with optional PostgreSQL support

## Requirements

- Python 3.9 or higher

## Installation

```bash
pip install flails
```

## Quick Start

1. Create a new Flails project:
```bash
flails new myproject
cd myproject
```

2. Set up your database:
```bash
flails db init
flails db migrate
flails db upgrade
```

3. Run the development server:
```bash
flails run
```

## Configuration

Flails uses environment variables for configuration. Create a `.env` file in your project root:

```env
FLAILS_APP=app
FLAILS_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db  # Optional: postgresql://localhost/your_database
```

## Project Structure

```
myproject/
├── app/
│   ├── __init__.py
│   ├── admin/
│   ├── auth/
│   ├── models/
│   └── config.py
├── migrations/
├── .env
├── config.py
└── requirements.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.