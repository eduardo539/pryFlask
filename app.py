from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    peso = None
    nombre = None
    if request.method == 'POST':
        peso = request.form['peso']
        nombre = request.form['nombre']
    return render_template('index.html', peso=peso, nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)