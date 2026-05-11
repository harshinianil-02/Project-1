from flask import Flask,render_template,request,redirect
import random
import string
import mysql.connector
app = Flask(__name__)
db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="harshini02@",
        database="url_shortener",
        auth_plugin="mysql_native_password"
)
cursor = db.cursor()
def generate_code(length=6):
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))
@app.route("/")
def home():
         return render_template("index.html")
@app.route("/shorten",methods=["POST"])
def shorten():
        user_url = request.form["url"]
        short_code = generate_code()
        cursor.execute(
                "INSERT INTO urls (original_url,short_code) VALUES (%s, %s)",
        [user_url, short_code]
        )
        db.commit()
        return f"short URL code is: {short_code}"
@app.route("/<code>")
def redirect_url(code):
        cursor.execute("SELECT original_url FROM urls WHERE short_code = %s", [code])
        result = cursor.fetchone()
        if result:
                return redirect(result[0])
        else:
                return "Invalid short URL"
        
if(__name__ == "__main__"):
        app.run(debug=True)
