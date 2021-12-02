# Full Stack API Final Project


## Full Stack Trivia API Project

This project is a game where users can test their knowledge answering trivia questions. The task for the project was to create an API and test suite for implementing the following functionality:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string. 
5. Play the quiz game, randomizing either all questions or within a specific category.
# Getting Started
# Installing Dependencies
Developers using this project should already have Python3, pip, node, and npm installed.

# Frontend Dependencies
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the frontend directory of this repository. After cloning, open your terminal and run:
npm install

# Backend Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /backend directory and running:

pip install -r requirements.txt
Running the Frontend in Dev Mode
The frontend app was built using create-react-app. In order to run the app in development mode use npm start. You can change the script in the package.json file.

Open http://localhost:3000 to view it in the browser. The page will reload if you make edits.

npm start
Running the Server
From within the backend directory first ensure you are working using your created virtual environment.

# To run the server, execute:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

# Testing
To run the tests, run
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
Omit the dropdb command the first time you run tests.

# API Reference
# Getting Started
Base URL: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
Authentication: This version does not require authentication or API keys.
Error Handling
Errors are returned as JSON in the following format:

{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
The API will return three types of errors:

400 – bad request
404 – resource not found
422 – unprocessable
Endpoints
# GET /categories
General: Returns a list categories.

Sample: curl http://127.0.0.1:5000/categories

  {
      "categories": {
          "1": "Science", 
          "2": "Art", 
          "3": "Geography", 
          "4": "History", 
          "5": "Entertainment", 
          "6": "Sports"
      }, 
      "success": true
  }
# GET /questions
General:

Returns a list questions.
Results are paginated in groups of 10.
Also returns list of categories and total number of questions.
Sample:  curl http://127.0.0.1:5000/questions
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Si
ngs'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton
 about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tour
nament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist-initials M C was a creator of opti
cal illusions?"
    }
  ],
  "success": true,
  "total_questions": 23
}
# DELETE /questions/<int:id>
General:

Deletes a question by id using url parameters.
Returns id of deleted question upon success.
Sample: curl http://127.0.0.1:5000/questions/2 -X DELETE

  {
      "deleted": 2, 
      "success": true
  }
# POST /questions
This endpoint either creates a new question or returns search results.

If no search term is included in request:
General:

Creates a new question using JSON request parameters.
Returns JSON object with newly created question, as well as paginated questions.
Sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{ "question": "Where do you live?", "answer": "Nigeria", "difficulty": 5, "category": "2" }'
{
  "created": 38,
  "question_created": "Where do you live?",
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Si
ngs'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton
 about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tour
nament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist-initials M C was a creator of opti
cal illusions?"
    }
  ],
  "success": true,
  "total_question": 28
}

# GET /questions
If search term is included in request:
General:

Searches for questions using search term in JSON request parameters.
Returns JSON object with paginated matching questions.
Sample: curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm": "how"}'
{
  "questions": [
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "5",
      "category": 3,
      "difficulty": 3,
      "id": 30,
      "question": "How many finger nails do you have on your right hand"
    }
  ],
  "success": true,
  "total_questions": 23
}
# GET /categories/<int:id>/questions
General:

Gets questions by category id using url parameters.
Returns JSON object with paginated matching questions.
Sample: curl http://127.0.0.1:5000/categories/3/questions
{
  "current_category": "Geography",
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "5",
      "category": 3,
      "difficulty": 3,
      "id": 30,
      "question": "How many finger nails do you have on your right hand"
    },
    {
      "answer": "Nigeria",
      "category": 3,
      "difficulty": 3,
      "id": 36,
      "question": "Which conutry is the largest in Africa?"
    }
  ],
  "success": true,
  "total_questions": 23
}

# POST /quizzes
General:

Allows users to play the quiz game.
Uses JSON request parameters of category and previous questions.
Returns JSON object with random question not among previous questions.
Sample: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [5, 12], "quiz_category": {"type": "Art", "id": "2"}}'
{
  "question": {
    "answer": "Jackson Pollock",
    "category": 2,
    "difficulty": 2,
    "id": 19,
    "question": "Which American artist was a pioneer of Abstract Expressionism,
and a leading exponent of action painting?"
  },
  "success": true
}
# Authors
Musa Muhammed authored the API (__init__.py), test suite (test_flaskr.py), and this README.
All other project files, including the models and frontend, were created by Udacity as a project template for the Full Stack Web Developer Nanodegree.
# Acknowledgements
A specail thanks to Alexsandberg GitHub Account where I got the idea for the search, quizzes and display of the questions by categories. Also, my sincere gratitude goes to stackoverflow team(https://stackoverflow.com/questions) for the tips on how to overcome the different error messages that were encountered.