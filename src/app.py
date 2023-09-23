from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
import datetime
import jwt
# Secret Key and Connection to DB
app=Flask(__name__)
app.config['SECRET_KEY']='thisisthesecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library.db'

db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Create a route to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    # Get user data from the request body
    user_id = request.json.get('user_id')
    user_name = request.json.get('user_name')
    password = request.json.get('password')

    # Check if user_name already exists in the database
    existing_user = User.query.filter_by(user_name=user_name).first()
    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    # Hash the password using SHA-256
    hashed_password = generate_password_hash(password, method='sha256')

    # Create a new User object
    new_user = User(user_id=user_id, user_name=user_name, password=hashed_password)

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "New user created successfully"}), 201

# login route has been provided for you , creates JWT valid for 20 mins and the roken is returned
# This token needs to be present in the request header to authorize users
@app.route('/login')
def login():
    auth=request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify",401,{"WWW-Authenticate" :'Basic realm="Login required"'})
    user=User.query.filter_by(name=auth.username).first()
    if not user:
        return make_response("Could not verify",401,{"WWW-Authenticate" :'Basic realm="Login required"'})
    if check_password_hash(user.password,auth.password):
        token=jwt.encode({"user_id":user.user_id,"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=20)},app.config['SECRET_KEY'])
        return jsonify({"token":token})
    return make_response("Could not verify",401,{"WWW-Authenticate" :'Basic realm="Login required"'})
    
# Run the flask app

if __name__=='__main__':
    app.run(debug=True)
