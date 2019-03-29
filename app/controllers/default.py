from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app import app, db, lm


from app.models.tables import User
from app.models.forms import LoginForm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route("/", defaults={"user": None}, methods=["GET","POST"])
def index(user):
    if current_user.is_authenticated:
        user = current_user.username
    return render_template('index.html', user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in")
            return redirect(url_for("index"))  
        else:
            flash("Invalid login")
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logout")
    return redirect(url_for("index"))


# Route for CRUD methods ...
@app.route("/crud/<info>")
@app.route("/crud", defaults={"info": None})


def crud(info):

    # INSERT ...
    # user = User("teste","1234","User TEST","teste@gmail.com")
    # db.session.add(user)
    # db.session.commit()

    # READ ...
    # the user will be displayed in the terminal.
    # user = User.query.filter_by(username="teste").all()
    # print(user)

    # UPDATE ..
    # user = User.query.filter_by(username="teste").first()
    # user.nome = "User TEST up"
    # db.session.add(user)
    # db.session.commit()

    # DELETE ...
    # user = User.query.filter_by(username="teste").first()
    # db.session.delete(user)
    # db.session.commit()

    return "OK"
