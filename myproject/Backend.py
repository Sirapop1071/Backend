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

@app.route("/students",methods=["POST"])
@basic_auth.required
def create_std():
    data = request.get_json()
    new_std={
        "id":data["id"],
        "Name":data["Name"],
        "major":data["major"],
        "gpa":data["gpa"]
    }
    
    if any(students["id"] == new_std["id"] for students in students):
        return jsonify({"error":"Cannot create new studen"}),500
    else:
        students.append(new_std)
        return jsonify(new_std),200

@app.route("/students/<int:std_id>",methods = ["PUT"])
@basic_auth.required
def update_std(std_id):
    std = next((b for b in students if b["id"] == std_id),None)
    if std:
        data = request.get_json()
        std.update(data)
        return jsonify(std),200
    else :
        return jsonify({"error":"Student not found"}),404
 
   


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
