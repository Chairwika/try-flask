from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    labels = ['Label 1', 'Label 2', 'Label 3']  # Exemple de liste de labels
    return render_template('index.html', labels=labels)

if __name__ == '__main__':
    app.run(debug=True)
