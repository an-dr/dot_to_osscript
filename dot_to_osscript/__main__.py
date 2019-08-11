from psutil import WINDOWS, MACOS, LINUX
import click
from .generate import *


# def start(name: str = None):
#     if WINDOWS:
#         dotenv(ps=True, sh=False)
#         dotalias(ps=True, sh=False)
#     else:
#         dotenv(ps=False, sh=True)
#         dotalias(ps=False, sh=True)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--powershell", "-p", default=WINDOWS, is_flag=True, help='Generate .env.ps1')
@click.option("--shell", "-s", default=(MACOS | LINUX), is_flag=True,  help='Generate .env.sh')
def generate(powershell, shell):
    dotenv(ps=powershell, sh=shell)
    dotalias(ps=powershell, sh=shell)


if __name__ == "__main__":
    cli()
