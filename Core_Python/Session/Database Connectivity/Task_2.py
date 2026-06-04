from flask import Flask, render_template, request

app = Flask(__name__)

user_data = {}

@app.route('/')
def login_page():
    return render_template("Login.html")


@app.route('/register')
def register_page():
    return render_template("Register.html")


@app.route('/registerUser', methods=['POST'])
def register_user():

    fn = request.form['fn']
    ln = request.form['ln']
    un = request.form['un']
    pwd = request.form['pwd']

    if fn == "" or ln == "" or un == "" or pwd == "":
        return render_template(
            "Register.html",
            msg="All Fields Are Mandatory"
        )

    user_data['fn'] = fn
    user_data['ln'] = ln
    user_data['un'] = un
    user_data['pwd'] = pwd

    return render_template(
        "Login.html",
        msg="Registration Successful"
    )


@app.route('/loginUser', methods=['POST'])
def login_user():

    un = request.form['un']
    pwd = request.form['pwd']

    if un != user_data.get('un'):
        return render_template(
            "Login.html",
            msg="Wrong Username"
        )

    if pwd != user_data.get('pwd'):
        return render_template(
            "Login.html",
            msg="Wrong Password"
        )

    return render_template(
        "Welcome.html",
        name=user_data['fn'] + " " + user_data['ln']
    )


if __name__ == '__main__':
    app.run(debug=True)