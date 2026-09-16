import os
import datetime
from PIL import Image, UnidentifiedImageError

pastas = []

while True:
      caminho = input("Pasta a ser renomeada: ")
      if caminho == "":
        break
      else:
        pastas.append(caminho)

for pasta in pastas:
    try:
        for filename in os.listdir(pasta):
            try:
                data = Image.open(os.path.join(pasta, filename)).getexif()       
                data = data[36867].split(" ")[0].replace(":", "-")
            except (UnidentifiedImageError, KeyError):
                data = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(pasta, filename)))
                data = data.strftime("%Y-%m-%d")
            os.rename(os.path.join(pasta, filename), os.path.join(pasta, f"{data}_{filename}"))
    except FileNotFoundError: 
        print(f"Erro: A pasta '{pasta}' não foi encontrada.")
        continue
    