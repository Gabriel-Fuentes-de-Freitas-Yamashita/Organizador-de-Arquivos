# Organizador Automático de Arquivos
## Descrição
Este é um script em Python que automatiza a organização de arquivos em um diretório. Ele resolve o problema de pastas desorganizadas, como a de Downloads, movendo cada arquivo para uma subpasta específica com base na sua extensão (ex: .pdf, .jpg, .txt).

## Funcionalidades
* Análise de Diretório: Lista todos os arquivos e suas extensões presentes em uma pasta de origem especificada.

* Criação Automática de Pastas: Cria novas pastas de destino (ex: "Imagens", "Documentos") com base nas extensões dos arquivos, caso elas ainda não existam, podendo serem configuradas no Dicionário do programa.

* Organização Inteligente: Move cada arquivo para a pasta correspondente à sua extensão, de acordo com um mapa de regras definido no código.

## Como Usar
* Clone este repositório para a sua máquina, configure o Dicionário se necessario.
  
* Abra um terminal na pasta do projeto e execute o comando:
  python organizador.py
  
* Indique qual pasta deseja oreganizar.

Seus arquivos serão movidos para as pastas de destino corretas.

## Tecnologias Utilizadas
* Python

* Biblioteca os (nativa do Python)
