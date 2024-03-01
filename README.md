# Port Scanner em Python

## Introdução

Este projeto implementa uma ferramenta de escaneamento de portas utilizando a linguagem de programação Python. A ferramenta foi desenvolvida para ser simples e amigável, permitindo aos usuários escanear portas TCP para identificar quais estão abertas em um host específico. O escaneamento de portas é uma prática comum em pentests (testes de penetração) para descobrir vulnerabilidades e serviços disponíveis em um alvo. Este projeto atende a requisitos específicos, incluindo a fácil utilização, a capacidade de escanear um host ou uma rede, inserir um intervalo de portas a ser escaneado e relacionar portas conhecidas (Well-Known Ports) com seus respectivos serviços.

## Funcionalidades

- **Interface Amigável**: A ferramenta foi projetada para ser de fácil utilização, com prompts claros e saída de resultados de fácil compreensão.
- **Escanear Host ou Rede**: Possibilita o escaneamento de portas em um único host ou em múltiplos endereços IP dentro de uma rede.
- **Seleção de Intervalo de Portas**: Permite ao usuário definir um intervalo específico de portas para o escaneamento, otimizando o processo de acordo com a necessidade da análise.
- **Identificação de Serviços**: Após o escaneamento, a ferramenta exibe não apenas as portas abertas encontradas, mas também associa essas portas a serviços conhecidos, baseando-se em uma lista de portas bem conhecidas.

## Pré-requisitos

Antes de executar o script `port_scanner.py`, certifique-se de que o Python está instalado em sua máquina. Este projeto foi testado com Python 3.8, mas deve ser compatível com outras versões do Python 3. Para verificar a instalação do Python, execute:

```bash
python --version
```

ou

```bash
python3 --version
```

## Como Usar

1. **Clone o Repositório ou Baixe o Script**: Primeiro, obtenha uma cópia do script `port_scanner.py` em sua máquina local.

2. **Execute o Script**: Abra um terminal ou prompt de comando e navegue até o diretório onde o script está salvo. Execute o script usando o seguinte comando:

    ```bash
    python port_scanner.py
    ```
    ou
    ```bash
    python3 port_scanner.py
    ```

3. **Siga as Instruções**: Insira o endereço do host alvo e o intervalo de portas quando solicitado pelo script. Por exemplo:

    ```
    Digite o host alvo: exemplo.com
    Digite o intervalo de portas (ex., 1-100): 1-100
    ```

4. **Avalie os Resultados**: Após o escaneamento, o script exibirá uma lista de portas abertas encontradas, junto com os nomes dos serviços associados a essas portas, se disponíveis.

## Considerações Finais

O uso de ferramentas de escaneamento de portas deve ser feito com responsabilidade e apenas em redes ou sistemas onde você tem permissão explícita para fazê-lo. A varredura não autorizada pode ser considerada ilegal e resultar em consequências legais.

## Contribuições

Contribuições para o projeto são bem-vindas. Se você tiver melhorias ou correções, sinta-se à vontade para forkar o repositório e enviar um pull request com suas alterações.
