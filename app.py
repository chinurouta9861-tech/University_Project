from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="*9861*chinu",
    database="university"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    dob = request.form["dob"]
    gender = request.form["gender"]
    email = request.form["email"]
    phone = request.form["phone"]
    address = request.form["address"]
    course = request.form["course"]
    password = request.form["password"]
    security_question = request.form["security_question"]
    security_answer = request.form["security_answer"]
    sql = """
    INSERT INTO students
    (first_name,last_name,dob,gender,email,phone,address,course,password,security_question,security_answer)

    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        first_name,
        last_name,
        dob,
        gender,
        email,
        phone,
        address,
        course,
        password,
        security_question,
        security_answer
    )

    cursor.execute(sql, values)

    db.commit()

    return "Registration Successful"

if __name__ == "__main__":
    app.run(debug=True)