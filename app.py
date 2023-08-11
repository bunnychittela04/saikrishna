from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulate admin login (replace this with actual authentication)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"

# Sample leave requests (replace this with a database)
leave_requests = []

@app.route('/')
def index():
    return render_template('leave_form.html')

@app.route('/submit', methods=['POST'])
def submit_leave():
    name = request.form['name']
    date = request.form['date']
    reason = request.form['reason']

    leave_requests.append({'name': name, 'date': date, 'reason': reason})

    return f"Leave request submitted for {name} on {date}. Reason: {reason}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect(url_for('admin_page'))
        else:
            return "Invalid credentials. Please try again."

    return render_template('login.html')

@app.route('/admin')
def admin_page():
    return render_template('admin_page.html', leave_requests=leave_requests)

if __name__ == '__main__':
    app.run(debug=True)
