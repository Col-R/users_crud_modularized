from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.user import Users

@app.route("/")
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('index.html', users=Users.get_all())

@app.route('/users/new')
def new():
    return render_template('create.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Users.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route('/users/<int:user_id>/edit')
def edit(user_id):
    data = {
    "id": user_id
    }
    user = Users.get(data)
    return render_template('edit.html', user = user )

@app.route('/users/<int:user_id>/update', methods = ['POST'])
def update_user(user_id):
    Users.edit(request.form)
    return redirect(f'/users/{user_id}/edit')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    data = {
    "id": user_id
    }
    user = Users.get(data)
    return render_template('delete.html', user = user )

@app.route('/users/<int:user_id>/destroy', methods = ['POST'])
def destroy(user_id):
   data = {
   "id": user_id
   }
   Users.delete(data)
   return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
