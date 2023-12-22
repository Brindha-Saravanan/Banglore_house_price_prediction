from flask import Flask,request,jsonify
import utill 

app=Flask(__name__)

@app.route('/hello')
def hello():
    print('hello')
    return("hello")

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'location':utill.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    # response = utill.get_location_names()
    return response

@app.route('/predict_price', methods=['POST'])
def predict_price():
    tot_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    response = jsonify({
        'estimated_price':utill.get_price(location,tot_sqft,bath,bhk)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("startinf flask")
    app.run()