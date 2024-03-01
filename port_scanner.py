import socket

def verificar_portas_abertas(host, inicio_porta, fim_porta):
    """
    Verifica quais portas estão abertas em um determinado intervalo no host especificado.
    
    :param host: Endereço do host alvo como uma string.
    :param inicio_porta: Número da porta inicial do intervalo.
    :param fim_porta: Número da porta final do intervalo.
    :return: Uma lista de portas abertas.
    """
    # Lista para armazenar as portas que estão abertas.
    portas_abertas = []

    # Itera sobre o intervalo de portas fornecido.
    for porta in range(inicio_porta, fim_porta + 1):
        # Cria um socket utilizando o protocolo IPv4 e TCP.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Define um limite de tempo (timeout) para a tentativa de conexão.
            sock.settimeout(1)
            
            # Tenta estabelecer conexão com o host na porta especificada.
            if sock.connect_ex((host, porta)) == 0:
                # Se a conexão for bem-sucedida, adiciona a porta à lista de portas abertas.
                portas_abertas.append(porta)

    return portas_abertas

def obter_nome_servico(porta):
    """
    Retorna o nome do serviço associado a um determinado número de porta, se conhecido.
    
    :param porta: Número da porta.
    :return: Nome do serviço como uma string, ou "Serviço Desconhecido" se não encontrado.
    """
    # Dicionário mapeando portas bem conhecidas aos seus serviços correspondentes.
    portas_conhecidas = {
        20: "FTP - Dados",
        21: "FTP - Controle",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        465: "SMTPS",
        587: "SMTP (Submissão)",
        993: "IMAPS",
        995: "POP3S",
        3306: "MySQL",
        3389: "RDP (Protocolo de Área de Trabalho Remota)",
        # Adicione mais portas e serviços conforme necessário.
    }

    # Retorna o nome do serviço para a porta especificada ou "Serviço Desconhecido".
    return portas_conhecidas.get(porta, "Serviço Desconhecido")

def main():
    """
    Função principal para verificar as portas abertas em um host alvo e relatar os serviços em execução nelas.
    """
    host = input("Digite o host alvo: ")
    intervalo_portas = input("Digite o intervalo de portas: ")

    try:
        # Extrai o início e o fim do intervalo de portas a partir da entrada do usuário.
        inicio_porta, fim_porta = map(int, intervalo_portas.split('-'))
    except ValueError:
        print("Intervalo de portas inválido. Por favor, use o formato: inicio-fim")
        return

    # Chama a função para verificar as portas abertas.
    portas_abertas = verificar_portas_abertas(host, inicio_porta, fim_porta)

    # Exibe os resultados.
    if portas_abertas:
        print("Portas abertas:")
        for porta in portas_abertas:
            nome_servico = obter_nome_servico(porta)
            print(f"{porta}: {nome_servico}")
    else:
        print("Nenhuma porta aberta encontrada.")

if __name__ == "__main__":
    main()
