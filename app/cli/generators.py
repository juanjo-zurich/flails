import os
import click
from jinja2 import Environment, FileSystemLoader

def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file_from_template(template_name, context, output_path):
    env = Environment(loader=FileSystemLoader('app/cli/templates'))
    template = env.get_template(template_name)
    content = template.render(**context)
    
    with open(output_path, 'w') as f:
        f.write(content)

@click.group()
def generate():
    """Generate various components for your application"""
    pass

@generate.command()
@click.argument('app_name')
def nueva_app(app_name):
    """Generate a new Flask application with the complete scaffold."""
    click.echo(f'Creating new Flails application: {app_name}')
    
    # Create directory structure
    base_dir = os.path.abspath(app_name)
    directories = [
        '',
        'app',
        'app/models',
        'app/templates',
        'app/static',
        'app/static/css',
        'app/static/js',
        'app/auth',
        'app/admin',
        'migrations',
        'tests'
    ]
    
    for directory in directories:
        create_directory_if_not_exists(os.path.join(base_dir, directory))
    
    # Copy template files
    templates = {
        'config.py.template': 'config.py',
        'requirements.txt.template': 'requirements.txt',
        'app/__init__.py.template': 'app/__init__.py',
        'app/models/user.py.template': 'app/models/user.py',
        'app/auth/__init__.py.template': 'app/auth/__init__.py',
        'app/auth/forms.py.template': 'app/auth/forms.py',
        'app/auth/routes.py.template': 'app/auth/routes.py',
        'app/admin/__init__.py.template': 'app/admin/__init__.py',
    }
    
    for template, destination in templates.items():
        create_file_from_template(template, {'app_name': app_name}, os.path.join(base_dir, destination))
    
    click.echo(f'\nFlails application {app_name} created successfully!')
    click.echo('\nNext steps:')
    click.echo(f'  cd {app_name}')
    click.echo('  python -m venv venv')
    click.echo('  source venv/bin/activate  # On Windows: venv\\Scripts\\activate')
    click.echo('  pip install -r requirements.txt')
    click.echo('  flask db init')
    click.echo('  flask db migrate')
    click.echo('  flask db upgrade')
    click.echo('  flask run')

@generate.command()
@click.argument('name')
@click.argument('fields', nargs=-1)
def model(name, fields):
    """Generate a new model with fields
    Example: flails generate model User name:string:unique email:string:unique:index age:integer:nullable
    """
    model_template = 'model.py.j2'
    model_path = f'app/models/{name.lower()}.py'
    
    # Parse fields
    parsed_fields = []
    for field in fields:
        try:
            parts = field.split(':')
            field_name = parts[0]
            field_type = parts[1].lower()
            modifiers = parts[2:] if len(parts) > 2 else []
            
            field_info = {
                'name': field_name,
                'type': field_type,
                'unique': 'unique' in modifiers,
                'nullable': 'nullable' in modifiers,
                'index': 'index' in modifiers
            }
            parsed_fields.append(field_info)
        except (ValueError, IndexError):
            click.echo(f'Invalid field format: {field}. Should be name:type[:modifier1:modifier2...]')
            return
    
    create_directory_if_not_exists('app/models')
    create_file_from_template(model_template, {
        'name': name,
        'fields': parsed_fields
    }, model_path)
    click.echo(f'Created model: {model_path} with fields: {[f["name"] for f in parsed_fields]}')

@generate.command()
@click.argument('name')
def controller(name):
    """Generate a new controller"""
    controller_template = 'controller.py.j2'
    controller_path = f'app/controllers/{name.lower()}.py'
    
    create_directory_if_not_exists('app/controllers')
    create_file_from_template(controller_template, {'name': name}, controller_path)
    click.echo(f'Created controller: {controller_path}')

@generate.command()
@click.argument('name')
def form(name):
    """Generate a new form"""
    form_template = 'form.py.j2'
    form_path = f'app/forms/{name.lower()}_form.py'
    
    create_directory_if_not_exists('app/forms')
    create_file_from_template(form_template, {'name': name}, form_path)
    click.echo(f'Created form: {form_path}')