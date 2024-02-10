
from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c3cd2ebbf3ec8769038812e04a81e574a0aa9461601dc198'

@app.route('/', methods = ["GET","POST"])
def tracker():
    # if request.method=="POST":
    #     Name=request.form.get("user_name")
    #     print(Name)
    #     return render_template("Data_Form.html")
    return render_template("form.html",items=[5,6,7,8])
if __name__ == '__main__':
    while True:
        app.run(debug=True)
    
