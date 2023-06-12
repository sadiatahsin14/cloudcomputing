from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def generate_even_numbers():
    n = int(request.args.get('n', '10'))  # Get the 'n' parameter from the request, defaulting to 10 if not provided
    numbers = [str(i * 2) for i in range(n)]
    result = ', '.join(numbers)
    return f'Even numbers: {result}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
