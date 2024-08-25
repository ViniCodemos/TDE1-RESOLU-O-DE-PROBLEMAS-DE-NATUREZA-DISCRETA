# Nome: Vinicius Edivaldo Souza Penhorato
# Turma: A
# Curso: Bacharelado em Ciência da Computação

def formatar_conjunto(conjunto):
    if all(isinstance(i, tuple) for i in conjunto):
        return '{ ' + ' , ' .join(f"({x}, {y})" for x, y in conjunto) + ' }'
    return '{ ' + ', ' .join(conjunto) + ' }'


def ler_operacoes(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        quantidade_operacoes = int(arquivo.readline().strip())
        resultados = []
            # Aqui é definido qual Operação o programa deve realizar
            # Coloquei o sorted para que a visualização seja em ordem Alfabetica/Ordem Numerica Crescente

        for _ in range(quantidade_operacoes):
            operacao = arquivo.readline().strip()
            conjunto1 = arquivo.readline().strip().split(', ')
            conjunto2 = arquivo.readline().strip().split(', ')

            if operacao == 'U':
                resolucao = sorted(set(conjunto1) | set(conjunto2))
                resultados.append(f"União: conjunto 1 {formatar_conjunto(conjunto1)}, conjunto 2 {formatar_conjunto(conjunto2)}. Resultado: {formatar_conjunto(resolucao)}")
            elif operacao == 'I':
                resolucao = sorted(set(conjunto1) & set(conjunto2))
                resultados.append(f"Interseção: conjunto 1 {formatar_conjunto(conjunto1)}, conjunto 2 {formatar_conjunto(conjunto2)}. Resultado: {formatar_conjunto(resolucao)}")
            elif operacao == 'D':
                resolucao = sorted(set(conjunto1) - set(conjunto2))
                resultados.append(f"Diferença: conjunto 1 {formatar_conjunto(conjunto1)}, conjunto 2 {formatar_conjunto(conjunto2)}. Resultado: {formatar_conjunto(resolucao)}")
            elif operacao == 'C':
                resolucao = sorted((x, y) for x in conjunto1 for y in conjunto2)
                resultados.append(f"Produto Cartesiano: conjunto 1 {formatar_conjunto(conjunto1)}, conjunto 2 {formatar_conjunto(conjunto2)}. Resultado: {formatar_conjunto(resolucao)}")
        return resultados

def converter_resultado_txt(resultados):
    nome_arquivo_saida = input("Digite o nome para o arquivo de saída (sem extensão): ")
    nome_arquivo_saida += ".txt"
    
    with open(nome_arquivo_saida, "w") as arquivo: 
        for linha in resultados:
            arquivo.write(linha + '\n\n')
    print(f"Resultados salvos em '{nome_arquivo_saida}'!")

def Função_Principal():
    nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
    resultados = ler_operacoes(nome_arquivo_entrada)
    
    ver_resultado = input("Deseja visualizar os resultados no terminal? (sim/não): ").lower()
    if ver_resultado.lower() == 'sim':
        for linha in resultados:
            print(linha)
    
    converter_resultado_txt(resultados)

# Executa a função principal
Função_Principal()
