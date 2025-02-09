from setuptools import setup, find_packages

setup(
    name='flails',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'app': ['cli/templates/**/*']
    },
    install_requires=[
        'Click>=8.1.7',
        'Flask>=3.0.0',
        'Flask-SQLAlchemy>=3.1.1',
        'Flask-Login>=0.6.3',
        'Flask-WTF>=1.2.1',
        'Flask-Migrate>=4.0.5',
        'Flask-Admin>=1.6.1',
        'email-validator>=2.1.0',
        'python-dotenv>=1.0.0',
        'Werkzeug>=3.0.1',
        'SQLAlchemy>=2.0.23',
        'psycopg2-binary>=2.9.9'
    ],
    entry_points={
        'console_scripts': [
            'flails=flails:cli'
        ],
    },
)