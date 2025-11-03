import click
from library_manager.core import list_by_type_and_year, add_document, rename_document, remove_document

@click.group()
def cli():
    pass

@cli.command()
@click.argument('root')
def list(root):
    tree = list_by_type_and_year(root)
    for t, years in tree.items():
        click.echo(f"Type: {t}")
        for y, files in years.items():
            click.echo(f"  Year: {y} -> {len(files)} files")

@cli.command()
@click.argument('src')
@click.argument('dest')
def add(src, dest):
    res = add_document(src, dest)
    click.echo(f'Added: {res}')

@cli.command()
@click.argument('path')
@click.argument('new_name')
def rename(path, new_name):
    res = rename_document(path, new_name)
    click.echo(f'Renamed: {res}')

@cli.command()
@click.argument('path')
def remove(path):
    ok = remove_document(path)
    click.echo('Removed' if ok else 'Not found')

if __name__ == '__main__':
    cli()
