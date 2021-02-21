var = ['_','_','_','_','_','_',' ',' ',' ']
var_dic = [0,6,7,8,3,4,5,0,1,2]
x_O = ['X','O']
i = 0

print("""
░░░▒█ █▀▀█ █▀▀▀ █▀▀█ 　 █▀▀▄ █▀▀█ 　 ▒█░░▒█ █▀▀ █░░ █░░█ █▀▀█ 
░▄░▒█ █░░█ █░▀█ █░░█ 　 █░░█ █▄▄█ 　 ░▒█▒█░ █▀▀ █░░ █▀▀█ █▄▄█ 
▒█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ 　 ▀▀▀░ ▀░░▀ 　 ░░▀▄▀░ ▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀

Para Jogar use o teclado Numérico digite e Pressione Enter:

_7_|_8_|_9_ 
_4_|_5_|_6_ 
 1 | 2 | 3
""")
input("Para começar pressione Enter")

#limpa o tabuleiro
def reset_game():
    var[0]=var[1]=var[2]=var[3]=var[4]=var[5]='_'
    var[6]=var[7]=var[8]=' '
    return

#mostra o tabuleiro  
def show():
    linha_1 = f"_{var[0]}_|_{var[1]}_|_{var[2]}_"
    linha_2 = f"_{var[3]}_|_{var[4]}_|_{var[5]}_"
    linha_3 = f" {var[6]} | {var[7]} | {var[8]} "
    print("\n",linha_1,"\n",linha_2,"\n",linha_3)
    return

def recebe_lance(i):
    jogador = ["Jogador (X):\n","Jogador (O):\n"]
    while True:
        lance = int(input(jogador[i]))
        if lance in range(1,10):
            return lance
        else:
            print("Digite um número de 1-9")
            
def testa_jogo():
    #testa as linhas, colunas, diagonais e empate
    for j in range(3):
        if var[j*3]==var[1+j*3]==var[2+j*3]=='X' or var[j*3]==var[1+j*3]==var[2+j*3]=='O' or var[j]==var[3+j]==var[6+j]=='X' or var[j]==var[3+j]==var[6+j]=='O' or var[0] == var[4] == var[8] or var[2] == var[4] == var[6] or var.count('X') > 4 or var.count('O') > 4:    
            return True
      
    return False
    
def testa_ganhador():
    if testa_jogo():
        if var.count('X') > 4 or var.count('O') > 4:
            print("Empate")
        else:   
            print("Jogador:",x_O[1-i],"Ganhou!!")
            
        show()          
        escolha = input("Recomeçar?[S/N]")
            
        if escolha in ['N','n']:
            return False
        else:
            reset_game()
            return True         
    return True
        

while testa_ganhador():
    show()
    lance = recebe_lance(i)
    if  var[var_dic[lance]] == 'X' or var[var_dic[lance]] == 'O':
        print ("casa preenchida\n")

    else:
        var[var_dic[lance]] = x_O[i]
        if i == 0: i = 1
        else: i = 0
        
    
    
    



