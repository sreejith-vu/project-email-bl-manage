#!/usr/bin/env python
#We application to check email blacklist and whitelist them.
import hashlib
import emailwhitelist
import blacklistcheck
from functools import wraps
from flask import Flask, render_template, request, flash, Response

app = Flask(__name__)
USER = [ '7f230baf6a60d740b3cff9af87ed5622', '7f4326f77836120d5906b4cc24a876f3' ]
SALT = 'k1n65'
EMAIL = ""
RETURN_VALUE_1 = ""
RETURN_VALUE_2 = ""
RETURN_VALUE_3 = ""

def check_auth(username, password):
    u_e_u = username + SALT
    u_e_p = password + SALT
    u = hashlib.md5(u_e_u.encode())
    u_h = u.hexdigest()
    h = hashlib.md5(u_e_p.encode())
    p_h = h.hexdigest()
    return u_h == USER[0] and p_h == USER[1]


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/removefrom_wb',methods = ['POST'])
def wb():
    global EMAIL
    global RETURN_VALUE_1
    global RETURN_VALUE_2
    global RETURN_VALUE_3
    if RETURN_VALUE_1 == 1:
        wb = emailwhitelist.workflow_b(EMAIL)
        RETURN_VALUE_1 = wb 
        return render_template('output.html', email_field = EMAIL, ch1 = RETURN_VALUE_1, ch2 = RETURN_VALUE_2, ch3 = RETURN_VALUE_3)
    else:
        return render_template('output.html', email_field = EMAIL, ch1 = RETURN_VALUE_1, ch2 = RETURN_VALUE_2, ch3 = RETURN_VALUE_3)


@app.route('/removefrom_mb',methods = ['POST'])
def mb():
    global EMAIL
    global RETURN_VALUE_1
    global RETURN_VALUE_2
    global RETURN_VALUE_3
    if RETURN_VALUE_2 == 2:
        mbb = emailwhitelist.mailgun_b(EMAIL)
        RETURN_VALUE_2 = mbb
        return render_template('output.html', email_field = EMAIL, ch1 = RETURN_VALUE_1, ch2 = RETURN_VALUE_2, ch3 = RETURN_VALUE_3)
    else:
        return render_template('output.html', email_field = EMAIL, ch1 = RETURN_VALUE_1, ch2 = RETURN_VALUE_2, ch3 = RETURN_VALUE_3)


@app.route('/removefrom_mc',methods = ['POST'])
def mc():
    global EMAIL
    global RETURN_VALUE_1
    global RETURN_VALUE_2
    global RETURN_VALUE_3
    if RETURN_VALUE_3 == 3:
        mcb = emailwhitelist.mailgun_c(EMAIL)
        RETURN_VALUE_3 = mcb
        return render_template('output.html', email_field = EMAIL, ch1 = RETURN_VALUE_1, ch2 = RETURN_VALUE_2, ch3 = RETURN_VALUE_3)
    else:
        return render_template('output.html', email_field = EMAIL, ch1 = RETURN_VALUE_1, ch2 = RETURN_VALUE_2, ch3 = RETURN_VALUE_3)


@app.route('/search',methods = ['POST'])
def search():
    global EMAIL
    global RETURN_VALUE_1
    global RETURN_VALUE_2
    global RETURN_VALUE_3
    EMAIL = request.form['email_field']

    if EMAIL:
        RETURN_VALUE_1 = blacklistcheck.workflow_b(EMAIL)
        RETURN_VALUE_2 = blacklistcheck.mailgun_b(EMAIL)
        RETURN_VALUE_3 = blacklistcheck.mailgun_c(EMAIL)
        return render_template('output.html', email_field = EMAIL, ch1 = RETURN_VALUE_1, ch2 = RETURN_VALUE_2, ch3 = RETURN_VALUE_3)
    else:
        return home()


@app.route('/main',methods = ['POST'])
def calling_home():
    return home()


@app.route('/')
@requires_auth
def home():
    return render_template('index.html')


if __name__ == '__main__':
   app.run(debug = True)
