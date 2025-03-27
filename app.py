from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def saudacao():
    if request.method == 'POST':
        mensagem_usuario = request.form.get('mensagem', '').strip().lower()
        
        if mensagem_usuario == "olá":
            hora_atual = datetime.now().hour
            
            if 6 <= hora_atual < 12:
                mensagem = "Bom dia!"
            elif 12 <= hora_atual < 18:
                mensagem = "Boa tarde!"
            else:
                mensagem = "Boa noite!"
            
            return f"<h1>{mensagem}</h1>"
        else:
            return "<h1>Por favor, diga 'Olá' para receber uma saudação!</h1>"
    
    # Formulário para envio da mensagem
    return '''
        <form method="POST">
            <label for="mensagem">Digite sua mensagem:</label>
            <input type="text" id="mensagem" name="mensagem">
            <button type="submit">Enviar</button>
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
