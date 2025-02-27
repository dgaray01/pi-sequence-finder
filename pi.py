from flask import Flask, request, render_template
from mpmath import mp

app = Flask(__name__)

# Set precision for pi generation
mp.dps = 100  # 1 million digits of pi

# Generate pi
pi_digits = str(mp.pi)[2:]  # Exclude '3.'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    sequence = request.form.get('sequence')
    if not sequence.isdigit():
        return {"error": "Input must be a number."}, 400
    position = pi_digits.find(sequence)
    if position == -1:
        return {"message": "Sequence not found in the digits of pi."}
    return {"message": f"Sequence found at position {position + 1}."}

if __name__ == '__main__':
    app.run(debug=True)