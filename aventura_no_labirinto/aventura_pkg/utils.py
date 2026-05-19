import os
import time
from rich.console import Console
from rich.panel import Panel

console = Console()

def imprime_instrucoes():
    texto = """
    [bold cyan]COMO JOGAR:[/bold cyan]
    - Use as setas do teclado para mover o [green]P[/green].
    - Colete [yellow]$[/yellow] para ganhar pontos.
    - Chegue ao [red]E[/red] para escapar!
    """
    console.print(Panel(texto, title="Instruções"))

def mostrar_menu():
    console.print("\n[bold magenta]1.[/bold magenta] Jogar")
    console.print("[bold magenta]2.[/bold magenta] Ver Instruções")
    console.print("[bold magenta]3.[/bold magenta] Modo Automático (Recursivo)")
    console.print("[bold magenta]4.[/bold magenta] Sair")
    return input("\nEscolha uma opção: ")

def animacao_vitoria(n=5):
    """Função recursiva para animação de vitória."""
    if n == 0:
        console.print("[bold yellow]!!! VOCÊ ESCAPOU !!![/bold yellow]")
        return
    console.print("." * n + " 🎉")
    time.sleep(0.3)
    animacao_vitoria(n - 1)