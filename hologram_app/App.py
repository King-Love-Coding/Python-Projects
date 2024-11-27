from flask import Flask, render_template, request, jsonify
from hologram_module import run_hologram_code

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_hologram', methods=['POST'])
def run_hologram():
    # Here you would call your hologram function
    hologram_result = run_hologram_code()
    return jsonify({"result": hologram_result})

if __name__ == '__main__':
    app.run(debug=True)
