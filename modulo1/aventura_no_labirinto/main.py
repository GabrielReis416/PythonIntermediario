import argparse
import time
import os
from aventura_pkg import labirinto as lab_mod, jogador as jog_mod, utils
from pynput import keyboard

# Variável global para capturar tecla
tecla_pressionada = None

def on_press(key):
    global tecla_pressionada
    try:
        if key == keyboard.Key.up: tecla_pressionada = "up"
        elif key == keyboard.Key.down: tecla_pressionada = "down"
        elif key == keyboard.Key.left: tecla_pressionada = "left"
        elif key == keyboard.Key.right: tecla_pressionada = "right"
    except AttributeError: pass

def jogar(nome, cor, diff, auto=False):
    largura = 10 * diff
    lab = lab_mod.criar_labirinto(largura=largura)
    player = jog_mod.iniciar_jogador()
    
    if auto:
        caminho = jog_mod.resolver_recursivo(lab, player["pos"])
        if not caminho:
            print("Labirinto sem saída possível!")
            return
        for passo in caminho:
            os.system('cls' if os.name == 'nt' else 'clear')
            player["pos"] = jog_mod.mover(passo, player["pos"], lab)
            lab_mod.imprimir_labirinto(lab, player["pos"], cor)
            time.sleep(0.2)
    else:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        global tecla_pressionada
        
        while lab[player["pos"][0]][player["pos"][1]] != "E":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Jogador: {nome} | Pontos: {player['pontos']}")
            lab_mod.imprimir_labirinto(lab, player["pos"], cor)
            
            if tecla_pressionada:
                player["pos"] = jog_mod.mover(tecla_pressionada, player["pos"], lab)
                player["pontos"] = jog_mod.pontuar(player["pos"], lab, player["pontos"])
                tecla_pressionada = None
            time.sleep(0.1)
        listener.stop()

    utils.animacao_vitoria()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Aventura no Labirinto CLI")
    parser.add_argument("--name", required=True, help="Nome do jogador")
    parser.add_argument("--color", default="green", help="Cor do jogador (green, blue, red)")
    parser.add_argument("--dificuldade", type=int, choices=[1, 2, 3], default=1, help="Nível (1-3)")
    parser.add_argument("--disable-sound", action="store_true", help="Desativa efeitos")
    
    args = parser.parse_args()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        op = utils.mostrar_menu()
        if op == "1": jogar(args.name, args.color, args.dificuldade)
        elif op == "2": utils.imprime_instrucoes(); input("Enter para voltar...")
        elif op == "3": jogar(args.name, args.color, args.dificuldade, auto=True)
        elif op == "4": break