from flask import Flask, request, jsonify
import util

app = Flask(__name__) # Create a Flask web application instance.


# Define a route for getting location names.
@app.route('/get_location_names', methods=['GET'])
def get_location_names(): #Define the function that will be executed when the endpoint is accessed.
    response = jsonify({
        'locations': util.get_location_names()  #function to get a list of location names.
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response
    #The response is a JSON object containing the list of locations,
    # and you've added a header to allow cross-origin resource sharing (CORS).
    

@app.route("/predict_home_price", methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response    

if __name__ == "__main__":
    print("Starting Pyhton Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
