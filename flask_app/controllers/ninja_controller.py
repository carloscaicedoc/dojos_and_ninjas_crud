from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/dojos/newninja")
def new_ninja():
    return render_template("ninja_new.html", all_dojos=Dojo.get_all_dojos())

@app.route("/dojos/createninja", methods = ["POST"])
def create_ninja():
    Ninja.create_ninja(request.form)
    return redirect("/dojos")    



# @app.route('/')
# @app.route("/dojos")
# def index():
#     return render_template("dojos_index.html", dojos=Dojo.get_all_dojos())

# @app.route("/users/new")
# def new_user():
#     return render_template("new_user.html")

# @app.route("/dojos", methods = ["POST"])
# def new_dojo():
#     Dojo.create_dojo(request.form)
#     return redirect("/dojos")