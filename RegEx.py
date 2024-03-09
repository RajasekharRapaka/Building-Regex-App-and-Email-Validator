from flask import Flask, request, render_template
import re
from validate_email_address import validate_email

app = Flask(__name__)


# Define the validate_email_address function
def validate_email_address(email):
    # Regular expression pattern for email validation
    pattern = r'^[\w\.-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    return bool(re.match(pattern, email))

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
        return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern)
    return render_template("index.html")

@app.route('/results', methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern")
    matched_strings = re.findall(regex_pattern, test_string)
    return render_template("results.html", test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings)

@app.route('/validate_email', methods=["POST"])
def validate_email_route():
    email = request.form.get("email")
    is_valid = validate_email(email)
    return render_template("email_validation.html", email=email, is_valid=is_valid)

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host = "0.0.0.0", port  = 5000,debug = True)
    no hup()
