from flask import Flask, request, jsonify
from models import optimal_group_formation
import numpy as np
import pulp as pl

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, OBAMA Flask!'

# End point for the OGF function
@app.route('/OGF', methods = ['POST'])
def get_OGF():
    # Get the input data from the request
    request_data = request.get_json()
    a_matrix = request_data['a']
    a = np.array(a_matrix)
    C = request_data['C']
    NM = request_data['NM']
    # Call the OGF function
    result, optim = optimal_group_formation(a = a, C = 4, NM = 3)

    out = {"objective_value": optim, "decisons": result}

    return jsonify(out)
    #return result



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

