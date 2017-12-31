from flask import Blueprint, render_template, request
from .. import app
from ..forms import ContactForm
from flask_mysqldb import MySQL
from wtforms import StringField, TextAreaField, PasswordField, Form, validators

home = Blueprint('home', __name__)

# Index
@home.route('/')
def index():
    return render_template('home.html')

# Ons Aanbod
@home.route('/aanbod')
def aanbod():
    cur = mysql.connection.cursor()

    result = cur.execute('SELECT * FROM richtingen')
    richtingen = cur.fetchall()

    if result > 0:
        return render_template('aanbod.html', richtingen = richtingen)
    else:
        msg = 'Geen richtingen in het systeem.'
        return render_template('aanbod.html', msg=msg)
    cur.close()

# Wie is Wie
@home.route('/wieiswie')
def wieiswie():
    cur = mysql.connection.cursor()

    result = cur.execute('SELECT * FROM leraren')
    leraren = cur.fetchall()

    if result > 0:
        return render_template('wieiswie.html', leraren = leraren)
    else:
        msg = 'Geen leerkrachten in het systeem.'
        return render_template('wieiswie.html', msg=msg)
    cur.close()

# Contact
@home.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        naam = form.naam.data
        email = form.email.data
        onderwerp = form.onderwerp.data
        bericht = form.bericht.data

        # Create cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO contact(naam, email, onderwerp, bericht) VALUES(%s, %s, %s, %s)", (naam, email, onderwerp, bericht))

        # Commit to DB
        mysql.connection.commit()

        # Close connection
        cur.close()

        flash('Je bericht is verstuurd', 'success')

        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)
