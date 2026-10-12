import os
from datetime import datetime, timedelta


def limpar_logs(caminho):
    limite = datetime.now() - timedelta(days=15)

    for raiz, pastas, arquivos in os.walk(caminho):
        if os.path.basename(raiz).lower() == "logs":
            for arquivo in arquivos:
                if arquivo.endswith(".log") or arquivo.endswith(".txt"):
                    caminho_arquivo = os.path.join(raiz, arquivo)

                    if datetime.fromtimestamp(os.path.getmtime(caminho_arquivo)) < limite:
                        os.remove(caminho_arquivo)

limpar_logs(r"C:\Users\e.gustavo.santos.GRUPO_A&C\Documents\GitHub")