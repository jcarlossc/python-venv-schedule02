# Importa módulos Schedule e Time
import schedule
import time

# Função(tarefa 01) a ser executada
def tarefa1():
    print("Tarefa 1 executada!")

# Função(tarefa 02) a ser executada
def tarefa2():
    print("Tarefa 2 executada!")

# Função(tarefa 03) a ser executada
def tarefa3():
    print("Tarefa 3 executada!")

# Agendando com intervalos diferentes
schedule.every(10).seconds.do(tarefa1)         # A cada 10 segundos
schedule.every().hour.do(tarefa2)              # A cada hora 
schedule.every().day.at("12:00").do(tarefa3)   # Todos os dias às 12:00 

while True:
    # Executa as tarefas agendadas
    schedule.run_pending()

    # Evita sobrecarga da CPU
    time.sleep(1)