from flask import render_template, url_for, flash, redirect
from FlaskBlog import app
from FlaskBlog.models import User, Post


from FlaskBlog.forms import RegistrationForm, LoginForm


posts = [
    {
        'author': 'Crespo',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Mohamed',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'April 21, 2018'
    }

]

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login' , methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!' , category='success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', category='danger')
    return render_template('login.html', title='login', form=form)