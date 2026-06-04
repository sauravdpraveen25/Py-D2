from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import flash

app = Flask(__name__)

app.secret_key = "abc123"

user = {}


@app.route("/")
def login():

    return render_template("Login.html")


@app.route("/register")
def register():

    return render_template("Register.html")


@app.route("/registerUser", methods=["POST"])
def registerUser():

    user["fn"] = request.form["fn"]
    user["ln"] = request.form["ln"]
    user["un"] = request.form["un"]
    user["pwd"] = request.form["pwd"]

    flash("Registration Successful")

    return redirect("/")


@app.route("/loginUser", methods=["POST"])
def loginUser():

    un = request.form["un"]
    pwd = request.form["pwd"]

    if un != user.get("un"):

        flash("Wrong Username")
        return redirect("/")

    if pwd != user.get("pwd"):

        flash("Wrong Password")
        return redirect("/")

    return render_template(
        "Welcome.html",
        fn=user["fn"],
        ln=user["ln"]
    )


if __name__ == "__main__":
    app.run(debug=True)