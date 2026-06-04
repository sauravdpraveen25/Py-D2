from flask import *

app = Flask(__name__)

@app.route('/')
def load_page():
	return render_template("Register.html")
	
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('nm')
        # user = request.form['nm']
        return 'Welcome POST : {}'.format(user)
    else:
        user = request.args.get('nm')
        return 'Welcome GET :  {}'.format(user)


app.run()
