from flask import request,Flask,jsonify
from flask_basicauth import BasicAuth
app = Flask(__name__) 

app.config['BASIC_AUTH_USERNAME']='username'
app.config['BASIC_AUTH_PASSWORD']='password'
basic_auth = BasicAuth(app)

students=[
    {"id":6530301071,"Name":"Sirapop Sorntad","major":"T12","gpa":"4.00"},
    {"id":6530301072,"Name":"Sirapa Tadsorn","major":"T12","gpa":"4.00"},
    {"id":6530301073,"Name":"Sorntad Sirapop","major":"T12","gpa":"4.00"}
]
@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

@app.route("/students",methods=["GET"])
@basic_auth.required
def get_all_students():
    return jsonify({"students":students})

@app.route("/students/<int:std_id>",methods=["GET"])
@basic_auth.required
def get_std(std_id):
    student =  next(( b for b in students if b["id"]==std_id ),None)
    if student:
        return jsonify(student)
    else:
        return jsonify({"error":"Student not found"}),404



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
