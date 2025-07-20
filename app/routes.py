from app import application
from flask import render_template, request, flash
import secrets
import string

def generate_random_password(length, upper, lower, numbers, symbols):
    valid_characters = ""
        
    if upper:
        valid_characters += string.ascii_uppercase
    
    if lower:
        valid_characters += string.ascii_lowercase
        
    if numbers:
        valid_characters += string.digits
    
    if symbols:
        valid_characters += string.punctuation
    
    return "".join(secrets.choice(valid_characters) for i in range(0, length + 1))


@application.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@application.route("/generate-password", methods=["POST"])
def generate_password():
    
    length = int(request.form.get("length", 16)) # 16 is default if no value is provided
    upper = "uppercase" in request.form
    lower = "lowercase" in request.form
    numbers = "numbers" in request.form
    symbols = "symbols" in request.form
    
    try:
        password = generate_random_password(length, upper, lower, numbers, symbols)
        return render_template("index.html", generated_password=password)

    except IndexError:
        flash("Please click a checkbox below to add options for password generation!")
        return render_template("index.html")

@application.route("/check-strength", methods=["POST"])
def check_strength():
    return render_template("index.html")