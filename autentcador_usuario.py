# Listas para possibilidades e também para armazenar senha
possibilidades_sim = ["Sim", "sim", "S", "s"]
possibilidades_nao = ["Não", "Nao", "não", "nao", "N", "n"]

# Variáveis para inicialização, tentativas de login e ligar dispositivo
tentativas = 3
iniciar = False
senha = ""

# Pergunta se o usuário deseja ligar o dispositivo
botao = input("O celular está desligado, gostaria de iniciá-lo? ")

# Inicialização do dispositivo
while not iniciar:
    if botao in possibilidades_sim:
        print("Iniciando Sistema... ")
        iniciar = True
    elif botao in possibilidades_nao:
        print("Dispositivo em repouso.")
        break
    else:
        botao = input("Só são permitidas respostas como 'Sim' e 'Não', gostaria de iniciá-lo? ")

# Definir senha
if iniciar:
    print("Agora determine uma senha, apenas números e com 4 dígitos.")
    while True:
        escolha_senha = input("Digite sua senha: ")

        # Valida se a senha contém apenas números e tem 4 dígitos
        if not escolha_senha.isdigit() or len(escolha_senha) != 4:
            print("Senha inválida. A senha deve conter exatamente 4 dígitos numéricos.")
        else:
            senha = escolha_senha
            print("Senha escolhida!")
            break

    # Tentar desbloquear o dispositivo
    while True:
        for tentativa in range(tentativas, 0, -1):
            abrir_dispositivo = input("Digite a senha escolhida: ")

            if abrir_dispositivo == senha:
                print("-" * 34)
                print("| Seja bem-vindo ao seu sistema! |")
                print("-" * 34)
                iniciar = False  # Dispositivo desbloqueado, encerra
                break
            else:
                print(f"A senha está incorreta! {tentativa - 1} tentativas restantes.")

            if tentativa == 1:  # Se for a última tentativa, oferecer a opção de redefinir a senha
                resetar_senha = input("Todas as tentativas foram incorretas, deseja redefinir a senha? (Sim/Não): ")

                # Verifica se a resposta é válida
                while resetar_senha not in possibilidades_sim and resetar_senha not in possibilidades_nao:
                    resetar_senha = input("Responda apenas com 'Sim' ou 'Não'. Deseja redefinir a senha? ")

                if resetar_senha in possibilidades_sim:
                    print("Redefinindo a senha...")
                    
                    # Definir nova senha
                    while True:
                        nova_senha = input("Digite uma nova senha de 4 dígitos: ")
                        
                        if not nova_senha.isdigit() or len(nova_senha) != 4:
                            print("A nova senha deve ter exatamente 4 dígitos numéricos.")
                        else:
                            senha = nova_senha
                            tentativas = 3  # Reinicia o número de tentativas
                            print("Senha redefinida com sucesso! Tente acessar novamente.")
                            break  # Sai do loop de redefinição de senha
                else:
                    print("Desligando dispositivo.")
                    iniciar = False
                    break

        if not iniciar:  # Se o dispositivo foi desbloqueado ou desligado, encerra o loop
            break
