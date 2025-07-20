#!/usr/bin/python3

"""
Program: pypass.py
Developer: CyberPanther232
Date Created: 7/19/2025
Date Modified: 7/19/2025
Purpose:
    - Generate passwords for users to use when creating accounts for other services
    - Check/Evaluate the strength and commoness of a password
"""

from app import application, routes

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=5000)