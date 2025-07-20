![Logo](https://github.com/CyberPanther232/pypass/blob/3efc5a8e9dbcf5b983d431c22b2e114d9d1201cc/pypass_logo_mini.png)

# PyPass - Password Toolkit

![PyPass Cyber Panther Logo](https://storage.googleapis.com/gemini-prod-us-west1-433524352522-public/images/84043b81-c71c-429a-9e12-87068551a37c)

**Generate, check strength, and verify the security of your passwords with this all-in-one password utility built with Python and Flask.**

PyPass is a simple yet powerful web application designed to help you manage your password security effectively. It provides a clean, modern, and user-friendly interface for all your password-related needs.

---

## ✨ Features

PyPass comes with three core features to enhance your online security:

* **🔐 Password Generator:** Create strong, random, and customizable passwords. You can specify the length and include or exclude uppercase letters, lowercase letters, numbers, and symbols.
* **💪 Strength Checker:** Get instant feedback on the strength of your passwords. The visual strength bar and clear labels (Weak, Fair, Strong, Very Strong) help you understand how secure your password is.
* **🛡️ Breach Check:** Verify if your password has been exposed in any known data breaches using the 'Have I Been Pwned?' API. This feature helps you avoid using compromised passwords.

---

## 🛠️ Tech Stack

This project is built with a combination of modern web technologies:

* **Backend:** Python 3, Flask
* **Frontend:** HTML5, Tailwind CSS, Vanilla JavaScript
* **APIs:** [Have I Been Pwned? API](https://haveibeenpwned.com/API/v3) for breach checking.
* **Dependencies:** `requests`

---

## 🚀 Setup and Installation

To get PyPass running on your local machine, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/pypass.git](https://github.com/your-username/pypass.git)
    cd pypass
    ```

2.  **Create and activate a virtual environment:**
    * **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Make sure you have a `requirements.txt` file containing `Flask` and `requests`)*

4.  **Run the application:**
    ```bash
    flask run
    ```

5.  **Open your browser** and navigate to `http://127.0.0.1:5000` to see the application in action!

---

## Usage

* **To Generate a Password:**
    1.  Select your desired length using the slider.
    2.  Check the boxes for the character types you want to include.
    3.  Click the "Generate Password" button.
    4.  Your new password will appear in the display box, ready to be copied.

* **To Check Password Strength:**
    1.  Type or paste a password into the "Password Strength Checker" input field.
    2.  Click the "Check Strength" button.
    3.  The strength bar and feedback text will update to show the result.

* **To Check for Breaches:**
    1.  Enter a password into the "Common Password Check" input field.
    2.  Click the "Check for Breaches" button.
    3.  The application will tell you if the password has been found in any known data breaches.

---

## Containerization
* This application is also containerized for ease of use and testing on your local machine! Which makes it easier for the user to tear up or down the application without having to manually uninstall all the dependencies / packages in the event you want to remove the application

* **Steps to Build and Run**
    1. Go to the current working directory of the repository aka. pypass/
      ```bash

      git clone https://github.com/CyberPanther232/pypass.git; cd pypass

      ```
    3. Next, run the command below to build the container on your machine!
      ```bash
       # Without elevated privileges
        sudo docker build -t "pypass" ./

       # With elevated privileges
        sudo docker build -t "pypass" ./
       
      ```

    5. After that, run the command below (set the left port to whatever port you want to open on your machine)
     ```bash
         # This will start and run the container detached
        docker run -p 5000:5000 --name PYPASS -d
     ```

     4. Finally, go to a web browser and either type localhost:5000 (or whatever other port number you may use) or the local IP address associated with your machine ex. (192.168.1.2:5000)
 
     5. Then you're done! Enjoy! 

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourAmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/YourAmazingFeature`).
5.  Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
