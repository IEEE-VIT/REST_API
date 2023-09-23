
# Secret Key and Connection to DB
app=Flask(__name__)
app.config['SECRET_KEY']='thisisthesecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library.db'


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
