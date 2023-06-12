from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_even_numbers():
    if request.method == 'POST':
        n = int(request.form.get('n', ''))
        if n == '':
            return "Please enter a valid number."
    else:
        n = ''

    if n != '':
        numbers = [str(i * 2) for i in range(int(n))]
        result = ', '.join(numbers)
    else:
        result = ''

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
