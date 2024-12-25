from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/message', methods=['GET', 'POST'])
def message():
    # Default response data
    response_data = {
        "message": "Check out the new update!",
        "showModal": True
    }

    # Handle POST requests
    if request.method == 'POST':
        data = request.get_json()  # Get JSON data from the request
        if data and 'message' in data and 'showModal' in data:
            response_data['message'] = data['message']
            response_data['showModal'] = bool(data['showModal'])

    # Return the response as JSON
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
