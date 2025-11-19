def contar_linhas_csv(nome_arquivo: str) -> int:
    """
    Lê o arquivo CSV especificado, contando o número total de linhas 
    de forma eficiente e com tratamento de erro de codificação.

    :param nome_arquivo: O nome do arquivo CSV a ser lido (ex: 'dados_faq.csv').
    :return: O número total de linhas no arquivo. Retorna 0 em caso de erro.
    """
    try:
        # CORREÇÃO: Usamos 'encoding="utf-8"' para resolver o UnicodeDecodeError.
        # O 'with open' garante que o arquivo é fechado.
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            # O jeito mais rápido e eficiente em memória de contar linhas
            total = sum(1 for linha in arquivo)
            
        return total
    
    except FileNotFoundError:
        print(f"ERRO: Arquivo '{nome_arquivo}' não encontrado. Verifique o nome e o caminho.")
        return 0
    except UnicodeDecodeError:
        print(f"ERRO DE CODIFICAÇÃO: Não foi possível ler o arquivo '{nome_arquivo}' com UTF-8. Tente 'encoding='latin-1''.")
        return 0
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return 0

# --- Exemplo de como usar a função ---
NOME_DO_SEU_ARQUIVO = "dados_faq.csv"

# Chamando a função
total_de_linhas = contar_linhas_csv(NOME_DO_SEU_ARQUIVO)

if total_de_linhas > 0:
    print("-" * 40)
    print(f"📊 O arquivo '{NOME_DO_SEU_ARQUIVO}' possui {total_de_linhas} linhas.")
    # Se você quiser ignorar o cabeçalho (header):
    print(f"   (São {total_de_linhas - 1} linhas de dados, excluindo o cabeçalho)")
    print("-" * 40)
