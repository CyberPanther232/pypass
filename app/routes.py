from app import application
from flask import render_template, request, flash, redirect
import secrets
import requests
import hashlib
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

def check_online(password):
    try:
        times_seen = 0

        hash_string = hashlib.sha1(password.encode()).hexdigest()
        
        prefix = hash_string[0:5]
        suffix = hash_string[5:0]
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
        length = int(request.form.get("length", 16)) # 16 is default if no value is provided
        upper = "uppercase" in request.form
        lower = "lowercase" in request.form
        numbers = "numbers" in request.form
        symbols = "symbols" in request.form
        
        try:
            password = generate_random_password(length, upper, lower, numbers, symbols)
            return render_template("index.html", generated_password=password)

        except IndexError:
            return render_template("index.html")
    else:
        return redirect("/")

@application.route("/check-strength", methods=["GET", "POST"])
def check_strength():
    
    if request.method == "POST":
        password = request.form.get("password_to_check")
        strength = 0
        strength_feedback = "Please enter a password above"
        
        upper, lower, numbers, symbols = False, False, False, False
        
        if password:
            for char in password:
                if char.isupper():
                    upper = True
                if char.islower():
                    lower = True
                if char in string.punctuation:
                    symbols = True
                if char in string.digits:
                    numbers = True
            
            if upper:
                strength += .15
            if lower: 
                strength += .15
            if numbers:
                strength += .15
            if symbols:
                strength += .15
            
            print(strength)
            
            length_modifier = (len(password) / 12) * .5 # 12 is max password length strength modifier
            
            if len(password) < 6:
                strength = .25
                strength_feedback = "weak"
            else:
                strength += length_modifier
                
                if strength <= 0.3:
                    strength_feedback = "Weak"
                    color = "bg-red-500"
                elif strength <= 0.5:
                    strength_feedback = "Fair"
                    color = "bg-orange-500"
                elif strength <= 0.75:
                    strength_feedback = "Strong"
                    color = "bg-green-500"
                elif strength > 1:
                    strength = 1
                    strength_feedback = "Very Strong"
                    color = "bg-emerald-500"
    
        return render_template("index.html", password=password, strength_bar_value=strength * 100, strength_bar_color=color, strength_feedback=strength_feedback)
    
    else:
        return redirect("/")
    
@application.route("/check-breach", methods=["GET", "POST"])
def check_breach():
    
    if request.method == "POST":
        password = request.form.get("password_to_check_breach")
        occurances = check_online(password)
        
        if not occurances.is_integer():
            breach_feedback = "Error!"
        else:
            if occurances > 1:
                breach_feedback = f"Oh no... That password has been found and cracked in approximately {occurances} data breaches!"
            else:
                breach_feedback = "Phew... This password has not been found in most common breaches"
    
        return render_template("index.html", breach_feedback=breach_feedback)
    
    else:
        return redirect("/")    