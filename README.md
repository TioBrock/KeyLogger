# Keylogger Python + Server em Flask pra Receber os logs
## O que é este projeto?

Este projeto consiste em duas partes principais:

1. **Keylogger em Python**  
   Utiliza a biblioteca `pynput` para capturar as teclas digitadas, salva os logs localmente em um arquivo txt.  
   Ao pressionar a tecla ESC (pode ser alterada), a captura para e o arquivo de logs é enviado via HTTP POST para um servidor remoto.

2. **Servidor Flask para Recebimento dos Logs**  
   Um pequeno servidor em Flask que recebe os logs enviados pelo keylogger, e salva em um arquivo local (`keylogs_recebidos.txt`).

---

## Como usar?

### Requisitos

- Python 3.x instalado
- Bibliotecas Python: `pynput`, `requests`, `flask`
  
Para facilitar a instalação das dependências, há um arquivo `requirements.txt` com as bibliotecas necessárias.

Instale tudo de uma vez com o comando:

```bash
pip install -r requirements.txt
```

---

### Passo a passo

1. **Configurar o servidor Flask**

   * No arquivo do servidor (`Flask.py`), certifique-se de que o Flask está conectado no IP correto e porta (padrão é `0.0.0.0:5000`).
   * Execute o servidor com:

   ```bash
   python Flask.py
   ```

2. **Configurar o keylogger**

   * No script do keylogger (`KeyLogger.py`), ajuste a variável `server_url` para o IP e porta do servidor Flask. Ex:

   ```python
   server_url = "http://192.168.0.105:5000/receber_dados"
   ```

3. **Rodar o keylogger**

   * Execute o keylogger:

   ```bash
   python KeyLogger.py
   ```

   * O programa irá capturar as teclas digitadas e salvar localmente.
   * Para parar a captura e enviar os dados ao servidor, pressione a tecla ESC.
   * Se o servidor confirmar o recebimento, os arquivos .txt da máquina que possui o keylogger serão excluídos.

4. **Verificar os logs no servidor**

   * Os logs serão armazenados no arquivo `keylogs_recebidos.txt` na máquina que está rodando o Flask.

---

## Compilando o código

Você pode (e recomendo) compilar o script Python em um executável com ferramentas como [PyInstaller](https://www.pyinstaller.org/). Assim, é possível aplicar um uso real, além de facilitar sua distribuição.

Por exemplo, para gerar um executável do `KeyLogger.py`, basta rodar:

```bash
pyinstaller --onefile KeyLogger.py
```

Isso gera um arquivo executável, que pode ser usado sem precisar instalar o python e as dependências.

---

## Possíveis melhorias

* **Criptografia dos dados:**
  Os logs podem ser criptografados antes do envio e descriptografados no servidor. Isso garante maior segurança no transporte de dados
  **Atenção:** Se for utilizar esse projeto em redes públicas ou pela internet, é importante usar criptografia.

* **Envio periódico:**
  Enviar os logs em intervalos regulares, sem precisar parar a ferramenta

* **Autenticação e segurança:**
  Proteger o endpoint do servidor com autenticação para evitar acesso não autorizado

* **Salvar logs em banco de dados:**
  Salvar os dados em bancos de dados, como MySQL por exemplo, para assim facilitar a visualização.

---

## Orientações importantes

* **Uso responsável:**
Use apenas em máquinas onde você tem autorização para monitorar, não use de forma anti-ética, isso pode causar em implicações legais. O intuito da ferramenta é apenas para aprendizado e testes.

* **Backup dos logs:**
  O script faz backup do arquivo antes de enviar para o servidor para evitar perda de dados.

## Licença

Este projeto está licenciado sob os termos da **MIT License**. Veja o arquivo `LICENSE` para mais informações.

---