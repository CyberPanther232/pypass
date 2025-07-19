from app import application
from flask import render_template, url_for, request

@application.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@application.route("/generate-password", methods=["POST"])
def generate_password():
    
    return render_template("index.html")