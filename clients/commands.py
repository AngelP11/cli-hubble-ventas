import click
from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manage the client lifecycle"""
    pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help="The client name")
@click.option('-c', '--company', type=str, prompt=True, help="The client company")
@click.option('-e', '--email', type=str, prompt=True, help="The client email")
@click.option('-p', '--position', type=str, prompt=True, help="The client position")
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_list = client_service.list_clients()

    click.echo(' ID  |  NAME  |  EMAIL  |  COMPANY  |  POSITION ')
    click.echo('*' * 100)

    for client in client_list:
        click.echo(' {uid} | {name} | {email} | {company} | {position} '.format(
            uid=client['uid'],
            name=client['name'],
            email=client['email'],
            company=client['company'],
            position=client['position'],
        ))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    pass


all = clients
