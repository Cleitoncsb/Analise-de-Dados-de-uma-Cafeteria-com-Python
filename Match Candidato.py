import PyPDF2
import os

caminho_do_diretorio = '/Users/user/Documents/CV'  # Substitua com o caminho da sua pasta
palavras_chave = ['Cleiton', 'Power BI', 'PRAD', 'Arroz']  # Substitua com suas palavras-chave

def encontrar_palavras_chave_em_pdf(caminho_do_diretorio, palavras_chave):
    resultados = {}
    palavras_encontradas_totais = set()  # Conjunto para armazenar todas as palavras-chave encontradas em todos os arquivos
    for arquivo in os.listdir(caminho_do_diretorio):
        if arquivo.endswith(".pdf"):
            caminho_do_arquivo = os.path.join(caminho_do_diretorio, arquivo)
            with open(caminho_do_arquivo, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                palavras_encontradas = set()  # Conjunto para armazenar palavras-chave encontradas neste arquivo
                for pagina in reader.pages:
                    texto = pagina.extract_text()
                    if texto:
                        for palavra in palavras_chave:
                            if palavra in texto:
                                palavras_encontradas.add(palavra)
                                palavras_encontradas_totais.add(palavra)
                resultados[arquivo] = palavras_encontradas
    return resultados, palavras_encontradas_totais

# Exemplo de uso
print("Caminho do diretório:", caminho_do_diretorio)
resultados, palavras_encontradas_totais = encontrar_palavras_chave_em_pdf(caminho_do_diretorio, palavras_chave)
qtd_chaves = len(palavras_chave)
qtd_match = len(palavras_encontradas_totais)
aderencia = (qtd_match / qtd_chaves)*100 if qtd_chaves > 0 else 0
print(resultados)
print(f"Aderência: {aderencia:.1f}%")
print("Quantidade total de palavras-chave:", qtd_chaves)
print("Quantidade de palavras-chave encontradas:", qtd_match)


