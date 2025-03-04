# PROJETO PYTHON - VENV/SCHEDULE -  Executa três tarefas em intervalos de tempo diferentes.

Este pequeno projeto tem o intuito de demonstrar a utilização do ambiente virtual
VENV e o módulo SCHEDULE.

VENV: Um ambiente virtual em Python isola dependências do projeto, evitando conflitos com pacotes globais do sistema. Ele permite que cada projeto tenha suas próprias bibliotecas e versões específicas.

SCHEDULE: módulo de agendamento e automação de tarefas em Python, como executar scripts em horários específicos, fazer backups ou enviar e-mails periodicamente.

Como dito no primeiro parágrafo, este terceiro projeto é bem simples e resume-se a explicar a atualização do 
ambiente virtual VENV e implementa um pequeno algoritmo que executa três tarefas em intervalos diferentes, com o módulo SCHEDULE.

## FERRAMENTAS UTILIZADAS
* Linguagem de programação Python.
* Ambiente virtual VENV.
* Git/GitHub
* Visual studio code.
* Windows 10.

## MODO DE UTILIZAR
* Clonar repositório.
* No diretório 'python-venv-schedule02', executar ```python -m venv venv``` para instalar o ambiente virtual.
* Executar ```pip install -r requirements.txt``` para instalar as dependências.
* Executar, caso esteja no Windows, ```venv\Scripts\activate``` para iniciar o ambiente. Caso Linux ou MacOS, ```source venv/bin/activate```.
* ```python app.py``` - Executa o algoritmo.
* Para sair do ambiente virtual ```deactivate```.

## COMANDOS IMPORTANTES
* ```python -m venv venv``` - Cria um ambiente virtual chamado venv. Observação: o primeiro venv é o comando, o segundo, o nome do diretório.
* No Windows, ```venv\Scripts\activate``` e no Linux, ```source venv/bin/activate``` - Inicializa o ambiente.
* ```deactivate``` - Encerra o ambiente.
* ```pip freeze > requirements.txt``` - Gera o arquivo que contém dependências. Esse mesmo comando atualiza o arquivo.
* ```pip list``` - Lista as dependências do projeto.
* ```pip show``` - Inserindo o nome da dependência após o comando, lista informações da dependência.
* ```pip install -r requirements.txt``` - Instala dependências que estão no arquivo 'requirements.txt'.
* ```pip install``` - Inserindo o nome da dependência após o comando, instala dependências.
* ```pip uninstall``` - Inserindo o nome da dependência após o comando, desinstala dependências.
