from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Run Script</h1>
        <form action="/run" method="post">
            <button type="submit">Run Script</button>
        </form>
    '''

@app.route('/run', methods=['POST'])
def run_script():
    # Run the focus1.py script
    result = subprocess.run(['python', 'focus1.py'], capture_output=True, text=True)
    return f"Script Output: <pre>{result.stdout}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
