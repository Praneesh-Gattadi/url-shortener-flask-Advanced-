from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import string, random, re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_shortener.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(9), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500))
    short_code = db.Column(db.String(10), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def valid_url(url):
    regex = re.compile(
        r'^(http|https)://'
        r'([\w.-]+)'
        r'(\.[a-zA-Z]{2,})'
    )
    return re.match(regex, url)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash("Invalid credentials")
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not (5 <= len(username) <= 9):
            flash("Username must be between 5 to 9 characters")
            return redirect(url_for('signup'))

        if User.query.filter_by(username=username).first():
            flash("This username already exists")
            return redirect(url_for('signup'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Signup successful. Please login.")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        original_url = request.form['url']

        if not valid_url(original_url):
            flash("Invalid URL format")
            return redirect(url_for('dashboard'))

        short_code = generate_short_code()
        new_url = URL(
            original_url=original_url,
            short_code=short_code,
            user_id=current_user.id
        )
        db.session.add(new_url)
        db.session.commit()

    urls = URL.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', urls=urls)

@app.route('/<short_code>')
def redirect_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first_or_404()
    return redirect(url.original_url)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)