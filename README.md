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

## Database Implementation

Flails supports multiple database backends through SQLAlchemy. Here's how to configure each supported database:

### SQLite (Default)

1. No additional dependencies required
2. Configure in `.env`:
```env
DATABASE_URL=sqlite:///app.db
```

### PostgreSQL

1. Install required dependencies:
```bash
pip install psycopg2-binary
```

2. Configure in `.env`:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
```

### MySQL

1. Install required dependencies:
```bash
pip install mysqlclient
```

2. Configure in `.env`:
```env
DATABASE_URL=mysql://username:password@localhost:3306/database_name
```

### Database Migrations

After configuring your database, run these commands:

```bash
# Initialize migrations directory
flails db init

# Create a new migration
flails db migrate -m "migration description"

# Apply migrations
flails db upgrade

# Rollback last migration (if needed)
flails db downgrade
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

## Running with Different Databases

Flails allows you to specify the database backend when running your application using command-line flags:

### SQLite
```bash
flails run --sqlite  # Uses SQLite (default)
# or explicitly specify the database file
flails run --sqlite=/path/to/custom.db
```

### PostgreSQL
```bash
flails run --postgresql  # Uses DATABASE_URL from .env
# or specify connection directly
flails run --postgresql=postgresql://username:password@localhost:5432/database_name
```

### MySQL
```bash
flails run --mysql  # Uses DATABASE_URL from .env
# or specify connection directly
flails run --mysql=mysql://username:password@localhost:3306/database_name
```

These flags override the DATABASE_URL setting in your .env file, making it convenient to switch between different databases during development.

```bash
# Initialize migrations directory
flails db init

# Create a new migration
flails db migrate -m "migration description"

# Apply migrations
flails db upgrade

# Rollback last migration (if needed)
flails db downgrade