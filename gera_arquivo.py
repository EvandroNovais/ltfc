#Abre o arquivo para escrever.
def gravar(gerados):
    try:
        arq = open("C:\\dados\ltfc\\gerados.txt", "w")
        for linha in gerados:
            arq.write(str(linha).replace("(","").replace(")","").replace(" ",""))
            arq.write("\n")
        arq.close()
    except:
        print("Ocorreu um erro ao tentar salvar o arquivo. Tente novamente.")
