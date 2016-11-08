from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/load')
def Subject():
    if username = "Buloy":
        list = [
            {"subject": "CSC101", "time": "7:30-9:00", "day": "MTH"}
        ]
    if username = "Kalay":
         list =  [ 
             {"subject": "FIL1", "time": "7:30-9:00", "day": "TF"}
         ]
            
    return jsonify(results=list)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
