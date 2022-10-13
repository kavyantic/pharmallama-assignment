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
    a = int(a)
    b = int(b)
    c = int(c)
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)
    # Return the solutions root1, root2
    return root1, root2


@app.route('/', methods=['GET'])
def home():
    return "<h1>Online Math Functions</h1><p>This site is a prototype API for computing solutions to various math problems.</p>"
# This endpoint computes factorial of given number


@app.route('/api/v1/resources/compute-factorial', methods=['GET'])
def endpoint_compute_factorial():

    # Retrieve the number from url parameter
    number = request.args.get("number", None)
    # For debugging
    print(f"got number {number}")
    response = {}
    # Check if user sent a number at all
    if not number:
        response["ERROR"] = "no number found, please send a number."
    # Check if the user entered a string not a integer
    elif not str(number).isdigit():
        response["ERROR"] = "number can't be string."
    # Now the user entered a valid number
    else:
        response["input integer"] = f"{number}"
        response["factorial"] = factorial(number)
    # Return the response in json format
    return jsonify(response)
    # This endpoint finds the real solutions to a quadratic


@app.route('/api/v1/resources/solve-quadratic', methods=['POST'])
def endpoint_solve_quadratic():
    response = {}

    # Retrieve the numbers from post body
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

    # For debugging
    print(f"got numbers {a}, {b}, {c}")
    # Check if user sent a, b and c at all

    # Now the user entered a valid number
    response["input integers"] = [a, b, c]
    response["factorial"] = quadratic(a, b, c)
    # Return the response in json format
    return jsonify(response)


# driver function
if __name__ == '__main__':
    app.run(debug=True)
