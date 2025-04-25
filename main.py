from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calcular_idade():
    if request.method == 'POST':
        try:
            ano_nascimento = int(request.form.get('ano_nascimento'))
            ano_atual = 2025

            if not 1900 <= ano_nascimento <= ano_atual:
                raise ValueError

            idade = ano_atual - ano_nascimento
            return render_template('idade.html',
                                   idade=idade,
                                   ano_nascimento=ano_nascimento,
                                   ano_atual=ano_atual)

        except ValueError:
            erro = "Por favor, digite um ano válido entre 1900 e 2025"
            return render_template('idade.html', erro=erro)

    return render_template('idade.html')


if __name__ == '__main__':
    app.run(debug=True)