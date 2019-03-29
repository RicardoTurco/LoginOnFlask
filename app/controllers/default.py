from flask import render_template
from app import app, db


from app.models.tables import User
from app.models.forms import LoginForm


@app.route("/index/<user>")
@app.route("/", defaults={"user":None})
def index(user):
    return render_template('index.html', user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template('login.html', form=form)


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
