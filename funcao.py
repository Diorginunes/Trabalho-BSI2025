def filtra_maquina(arquivo_origem, maquina):
    with open(arquivo_origem, 'r', encoding='utf-8') as arquivo:  #leitura
        with open(arquivo_origem + '_relatorio_' + maquina + '.csv', 'w', encoding='utf-8') as relatorio:    #abre em modo escrita
            linhas = arquivo.readlines()   #transforma em uma lista das linhas

            for linha in linhas:  #percorre a lista
                if (maquina.upper() in linha) or (maquina.lower() in linha) or (maquina.capitalize() in linha):
                    print(linha)      #exibe item da lista
                    relatorio.write(linha)
                
            arquivo.close()
            relatorio.close()

def filtra_operador(arquivo, operador):
    filtra_maquina(arquivo, operador)


# maquina = input("nome da maquina: ")
# filtra_maquina('dados_faq.csv', 'bobst')


filtra_operador('dados_onduladeira.csv', 'odair')
