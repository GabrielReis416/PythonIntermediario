import random

def criar_labirinto(largura=15, altura=7):
    """
    Gera um labirinto aleatório. 
    # = Parede, . = Caminho, $ = Item, E = Saída
    """
    labirinto = []
    for y in range(altura):
        linha = []
        for x in range(largura):
            if x == 0 or x == largura - 1 or y == 0 or y == altura - 1:
                linha.append("#")
            else:
                sorteio = random.random()
                if sorteio < 0.2: linha.append("#")
                elif sorteio < 0.3: linha.append("$")
                else: linha.append(".")
        labirinto.append(linha)
    
    # Garantir início e fim acessíveis
    
    labirinto[1][1] = "."
    labirinto[altura-2][largura-2] = "E"
    return labirinto

def imprimir_labirinto(labirinto, pos_jogador, cor="green"):
    """Renderiza o labirinto no console usando Rich."""
    from rich.console import Console
    console = Console()
    
    for y, linha in enumerate(labirinto):
        render_linha = ""
        for x, char in enumerate(linha):
            if [y, x] == pos_jogador:
                render_linha += f"[{cor}]P[/{cor}]"
            elif char == "#": render_linha += "█"
            elif char == "$": render_linha += "[yellow]$[/yellow]"
            elif char == "E": render_linha += "[bold red]E[/bold red]"
            else: render_linha += " "
        console.print(render_linha)