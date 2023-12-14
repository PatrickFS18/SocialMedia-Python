import subprocess
import time

def git_pull():
    try:
        subprocess.run(['git', 'pull'], check=True)
        print("Git pull realizado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar git pull: {e}")

if __name__ == "__main__":
    while True:
        git_pull()
        time.sleep(180)  # Esperar 3 minutos antes da próxima execução