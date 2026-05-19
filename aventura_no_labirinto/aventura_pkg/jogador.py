from pynput import keyboard

def iniciar_jogador():
    return {"pos": [1, 1], "pontos": 0, "venceu": False}

def mover(direcao, pos_atual, labirinto):
    y, x = pos_atual
    nova_pos = [y, x]
    
    if direcao == "up": nova_pos[0] -= 1
    elif direcao == "down": nova_pos[0] += 1
    elif direcao == "left": nova_pos[1] -= 1
    elif direcao == "right": nova_pos[1] += 1
    
    # Checar colisão 
    if labirinto[nova_pos[0]][nova_pos[1]] != "#":
        return nova_pos
    return pos_atual

def pontuar(pos, labirinto, pontos):
    char = labirinto[pos[0]][pos[1]]
    if char == "$":
        labirinto[pos[0]][pos[1]] = "."
        return pontos + 10
    return pontos

def resolver_recursivo(lab, pos, visitados=None):
    """Desafio: DFS para encontrar o caminho até a saída 'E'."""
    y, x = pos
    if lab[y][x] == "E": return []
    if visitados is None: visitados = set()
    
    visitados.add((y, x))
    direcoes = [("down", (y+1, x)), ("up", (y-1, x)), ("right", (y, x+1)), ("left", (y, x-1))]
    
    for nome, (ny, nx) in direcoes:
        if lab[ny][nx] != "#" and (ny, nx) not in visitados:
            caminho = resolver_recursivo(lab, [ny, nx], visitados)
            if caminho is not None:
                return [nome] + caminho
    return None