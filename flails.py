#!/usr/bin/env python
import click
from app.cli.generators import generate

@click.group()
def cli():
    """Flails command line interface"""
    pass

cli.add_command(generate)

if __name__ == '__main__':
    cli()