# REST_API
Welcome to Source Sprint's back-end repository!

Here's an explanation of the project you will be working on!

We are going to make a virtual library!
We need two roles, an admin and a user

An admin can:
1) Add a book
2) Delete a book ( it's no longer in stock for example)
3) View detais on the user
4) A user can be promoted to an admin by typing a pre-set passcode(not the most secure lol)

A user can:
1) Create an account / Log In
2) Viewing books of the library
3) Return a borrowed book
4) View user details

The user and admin routes must be protected, i.e, they can only be accessed when the user logs in!
This must be achieved using JWT ( JSON Web Tokens)

The tech stack used must be Flask, and a database can be made with the help of SQLAlchemy

<h3>Resources:</h3>
You can test the routes in the repository with Postman. (You may have to download the application) <br>
https://www.geeksforgeeks.org/basics-of-api-testing-using-postman/
