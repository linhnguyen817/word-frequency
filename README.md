# Description
A single page web application that lists the number of occurences for each inputted word in descending order.

**Frontend**: Javascript - React, Axios

**Backend**: Python - Flask

# How to run locally
Requires updated versions of [React](https://reactjs.org) and [Flask](https://flask.palletsprojects.com/en/2.1.x/installation/)
1) Start API server:

    ```
    cd backend
    flask run
    ```

2) Run the frontend React app in the development mode:
    ```
    cd frontend/client
    npm start
    ```
    Open [http://localhost:3000](http://localhost:3000) to view React application in your browser.


# Algorithm evaluation
Runtime Complexity: O(2n)

Space Complexity: O(2n)

# Possible extensions
- Connect to database to store past queries
- Allow for text file uploads
- Transition from Flask to Falcon API for faster responses
- Take advantage of python's builtin sort and bisect functions to save on space
