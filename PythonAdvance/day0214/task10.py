from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def index():
    return "首页"
@app.route("/ljk")
def ljkinfo():
    return "李江坤的个人主页"
@app.route("/ljk/pay")
def ljkpay():
    return render_template('pay.html')
app.run()

