# Full CRUD for Contact in models.py

from flask import request, jsonify
from config import app,db
from models import Contact


@app.route("/contacts", methods=["GET"])
def get_contact():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.routes("/create_contact", methods=["POST"])
def create_contact():





if __name__ == '__main__':
    with app.app_context():
        db.create_all()


    app.run(debug=True)