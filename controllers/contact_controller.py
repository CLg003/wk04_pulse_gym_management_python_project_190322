from flask import Blueprint, render_template

contact_blueprint = Blueprint("contact", __name__)

@contact_blueprint.route("/contact", methods=['GET'])
def contact():
    return render_template('contact.html')