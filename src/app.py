
# Secret Key and Connection to DB
app=Flask(__name__)
app.config['SECRET_KEY']='thisisthesecretkey'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///library.db'


# login route has been provided for you , creates JWT valid for 20 mins and the roken is returned
# This token needs to be present in the request header to authorize users
@app.route('/login')
def login():
{
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
}
        def user():
    {
        book = input("Enter the name of the book:")
        if(book_availability_borrowed = True)
            print(book.update)
            print("Book updated sucessfully")
            return book.update
        elif(book_availability== False)
            if(book.user_borrowed_id=user_id)
               update_book_available = input("update book available:")
               user_borrowed_id = input("The user borroed id is: " + UHGB123)
               return update_book_available
               return user_borrowed_id
            else
                printf("invalid")
    elif(book_available_borrowed = False)
        print("Book available to be borrowed")
        book_not_available_borrowed = input("Not available")
        return not_availale
    else
        print("Invalid")
    }



# Run the flask app

if __name__=='__main__':
    app.run(debug=True)

