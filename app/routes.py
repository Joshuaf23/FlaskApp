from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm
from flask import request
from flask import url_for
from flask import jsonify

#routes – URLs where a flask app accepts requests
@app.route('/')
@app.route('/index')
#a view function – route handler
def index():
    user = {'username': 'Joshua Fuller'}
    classes = [{'classInfo': {'code': 'CSC324', 'title': 'DevOps'}, 'instructor': 'Baoqiang Yan'},{'classInfo': {'code': 'CSC184', 'title': 'Python Programming'}, 'instructor': 'Evan Noynaert'}]
    return render_template('index.html', title='Home', user=user, classes=classes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Welcome user {}! You opted for remember_me={}'.format(form.username.data, form.remember_me.data))
            return redirect(url_for('success'))
    else:
        if request.args:
            flash('GET method now allowed for login!')
        #else:
        #    flash('No data in request!')

    return render_template('login.html', title='Sign In', form=form)

@app.route('/json')
def jsonTest():
    # return jsonify(list(range(5)))
    instructor = {"username": "byan",
                  "role": "instructor",
                  "uid": 11,
                  "name":
                      {"firstname": "Baoqiang",
                       "lastname": "Yan"
                       }
                  }

    return jsonify(instructor)

@app.route('/success')
def success():
    return render_template('jfuller6.html', title='Success')
