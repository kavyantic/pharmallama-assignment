import json
from multiprocessing.sharedctypes import Value
from flask import Flask, request, jsonify
import math
app = Flask(__name__)


def factorial(x):
    # edited
    x = int(x)
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def quadratic(a, b, c):
    # edited 
   
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    return root1, root2


@app.route('/', methods=['GET'])
def home():
    return "<h1>Online Math Functions</h1><p>This site is a prototype API for computing solutions to various math problems.</p>"


@app.route('/api/v1/resources/compute-factorial', methods=['GET'])
def endpoint_compute_factorial():

    number = request.args.get("number", None)
    print(f"got number {number}")
    response = {}
    if not number:
        response["ERROR"] = "no number found, please send a number."
    elif not str(number).isdigit():
        response["ERROR"] = "number can't be string."
    else:
        response["input integer"] = f"{number}"
        response["factorial"] = factorial(number)
    return jsonify(response)


# Since we are extracting payload from query parameters, GET method will do the job.
@app.route('/api/v1/resources/solve-quadratic', methods=['GET'])
def endpoint_solve_quadratic():
    response = {}
    
    # rewrote the validation code
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        c = int(request.args.get('c'))
        if 0 in [a, b, c]:
            response["ERROR"] = "a,b and c cannot contain zeros"
            return jsonify(response)
        if (not ((b * b) >= (4 * a * c))):
            response["ERROR"] = "b's square must be greater than (4 * a * c)"
            return jsonify(response)

    except ValueError:
        if not a or not b or not c:
            response["ERROR"] = "Invalid input. Please send a, b and c"
        else:
            response["ERROR"] = "numbers can't be string."
        return jsonify(response)

    print(f"got numbers {a}, {b}, {c}")

    response["input integers"] = [a, b, c]
    response["factorial"] = quadratic(a, b, c)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
