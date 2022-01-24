from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo


@app.route('/')
@app.route("/dojos")
def index():
    return render_template("dojos_index.html", dojos=Dojo.get_all_dojos())


@app.route("/dojos", methods = ["POST"])
def new_dojo():
    Dojo.create_dojo(request.form)
    return redirect("/dojos")

@app.route('/dojos/<int:id>', methods=['GET'])
def display_dojo_info(id):
    data = {
        'id':id
    }
    dojo = Dojo.ninjas_in_dojo(data)
    return render_template("ninjas_in_dojo.html", dojo=dojo)

