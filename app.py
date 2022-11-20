from flask import Flask
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__,template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////srijan.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Feed(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    no = db.Column(db.Integer,nullable=False)
    msg = db.Column(db.String(500),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True,port=8000)

