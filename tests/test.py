import re

with open('teste.txt') as file:
    content = file.read()
    ocorrencias = re.findall('teste', content)
    print(ocorrencias)
