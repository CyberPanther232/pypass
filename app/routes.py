from app import application
from flask import render_template, request, flash, redirect
import secrets
import requests
import hashlib
import string
import os

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

def check_online(password):
    try:

        hash_string = hashlib.sha1(password.encode()).hexdigest()
        prefix = hash_string[0:5]
        suffix = hash_string[5:].upper()
        req = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}')
        
        hashes = (line.split(":") for line in req.text.splitlines())
        for hash_suffix, count in hashes:
            if hash_suffix == suffix:
                return int(count)  # Found, return number of times seen
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return False

@application.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@application.route("/generate-password", methods=["GET", "POST"])
def generate_password():
    if request.method == "POST":
        length = int(request.form.get("length", 16))
        upper = "uppercase" in request.form
        lower = "lowercase" in request.form
        numbers = "numbers" in request.form
        symbols = "symbols" in request.form

        try:
            password = generate_random_password(length, upper, lower, numbers, symbols)
            return render_template(
                "index.html",
                generated_password=password,
                length=length,
                upper=upper,
                lower=lower,
                numbers=numbers,
                symbols=symbols
            )
        except IndexError:
            return render_template("index.html", error="Please select at least one character set.")

    return redirect("/")


@application.route("/check-strength", methods=["GET", "POST"])
def check_strength():
    if request.method == "POST":
        password = request.form.get("password_to_check", "")
        strength = 0
        strength_feedback = "Please enter a password above"
        color = "bg-blue-500"  # default fallback color

        if password.strip():  # check for non-empty password
            upper = any(c.isupper() for c in password)
            lower = any(c.islower() for c in password)
            numbers = any(c.isdigit() for c in password)
            symbols = any(c in string.punctuation for c in password)

            # Base score contributions
            if upper: strength += 0.15
            if lower: strength += 0.15
            if numbers: strength += 0.15
            if symbols: strength += 0.15

            # Length modifier
            length_modifier = min((len(password) / 12) * 0.5, 0.5)
            if len(password) < 6:
                strength = 0.25
                strength_feedback = "Weak"
                color = "bg-red-500"
            else:
                strength += length_modifier

                # Assign feedback and color based on strength
                if strength <= 0.3:
                    strength_feedback = "Weak"
                    color = "bg-red-500"
                elif strength <= 0.5:
                    strength_feedback = "Fair"
                    color = "bg-orange-500"
                elif strength <= 0.75:
                    strength_feedback = "Strong"
                    color = "bg-green-500"
                else:
                    strength = 1
                    strength_feedback = "Very Strong"
                    color = "bg-emerald-500"

            # Check against common password list
            with open(os.path.realpath('pypass/app/10k-most-common.txt')) as f:
                for line in f:
                    pw = line.strip()
                    variants = {pw, pw.lower(), pw.upper(), pw.capitalize()}
                    if password in variants:
                        strength = 1
                        strength_feedback = "Weak - Common password!"
                        color = "bg-red-500"
                        break  # Stop checking after match

        else:
            strength = 0
            strength_feedback = "Enter a password please!"
            color = "bg-blue-500"

        return render_template(
            "index.html",
            password_to_check_strength=password,
            strength_bar_value=int(strength * 100),
            strength_bar_color=color,
            strength_feedback=strength_feedback
        )

    return redirect("/")

        
@application.route("/check-breach", methods=["GET", "POST"])
def check_breach():
    
    if request.method == "POST":
        password = request.form.get("password_to_check_breach")
        
        if password != "": 
            occurances = check_online(password)
        
            if not occurances.is_integer():
                breach_feedback = "Error!"
            else:
                if occurances > 1:
                    breach_feedback = f"Oh no... That password has been found and cracked in approximately {occurances} data breaches!"
                else:
                    breach_feedback = "Phew... This password has not been found in most common breaches"
        
            return render_template("index.html", breach_feedback=breach_feedback, password_breach_check=password)
        else:
            return render_template("index.html", breach_feedback="Please enter a password!", password_breach_check=password)
    else:
        return redirect("/")    