import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgresql://{}:{}@{}/{}".format(
            "student", "student", 'localhost:5432', self.database_name
        )
        setup_db(self.app, self.database_path)

        # sample question for use in tests
        self.new_question = {
            'question': 'Which category is geography?',
            'answer': 3,
            'difficulty': 3,
            'category': '3'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

            for category in categories:
                obj = Category(type=category['type'])
                self.db.session.add(obj)
                self.db.session.commit()
    
            for question in questions:
                obj = Question(question=question['question'], answer=question['answer'], category=question['category'], difficulty=question['difficulty'])
                self.db.session.add(obj)
                self.db.session.commit()
                self.db.session.close()
                
    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
            self.db.drop_all()
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # Tests question pagination success
    def test_get_paginated_questions(self):
       

        # get response and load data
        res = self.client().get('/questions')
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that total_questions and questions return data
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))

    # Tests question pagination failure 404
    def test_404_request_beyond_valid_page(self):
        

        # send request with bad page data, load response
        res = self.client().get('/questions?page=100')
        data = json.loads(res.data)

        # check status code and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')



    # Test to delete a different question in each attempt
    def test_delete_question(self):
       

        res = self.client().delete("/questions/1")
        data = json.loads(res.data)

        # see if the question has been deleted
        question = Question.query.filter(Question.id == 1).one_or_none()

        # check status code 422 for failure
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

        # check if question id matches deleted id
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data["total_questions"])
        self.assertTrue(len(data["questions"]))
       
        # check if question equals None after delete
        self.assertEqual(question, None)

    # Tests question creation success
    def test_create_new_question(self):
        

        # create new question and load res data
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)


        # check status code and success message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        self.assertTrue(data["created"])
        self.assertTrue(len(data["questions"]))

    # Tests question creation failure 405
    def test_422_if_question_creation_not_allowed(self):
        
        res = self.client().post("/questions/77", json=self.new_question)
        data = json.loads(res.data)

        # check status code and success message
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "method not allowed")

    # Tests search questions success
    def test_search_questions(self):
      

        # send post request with searchTerm
        res = self.client().post('/questions',
                                      json={'searchTerm': 'which'})

        # load response data
        data = json.loads(res.data)

        # check response status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that number of results = 10
        self.assertEqual(len(data['questions']), 10)

        # check that id of question in res is correct
        self.assertEqual(data['questions'][0]['id'], 2)

    # Tests search questions failure 404
    def test_404_if_search_questions_fails(self):
        

        # send post request with search term that should fail
        res = self.client().post('/questions',
                                      json={'searchTerm': 'kilimanjarokenya'})

        # load response data
        data = json.loads(res.data)

        # check response status code and message
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Tests getting questions by category success
    def test_get_questions_by_category(self):
        

        # send request with category id 3 for geography
        res = self.client().get('/categories/3/questions')

        # load response data
        data = json.loads(res.data)

        # check response status code 400 for failure
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

        # check that questions are returned (len != 0)
        self.assertNotEqual(len(data['questions']), 0)

        # check that current category returned is geography
        self.assertEqual(data['current_category'], 'Geography')

        
    # Tests playing quiz game success
    def test_play_quiz_game(self):

        # send post request with category and previous questions
        res = self.client().post('/quizzes',
                                      json={'previous_questions': [9, 11],
                                            'quiz_category': {'type': 'Geography', 'id': '3'}})

        # load response data
        data = json.loads(res.data)

        # check response status code and message
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # check that a question is returned
        self.assertTrue(data['question'])

        # check that the question returned is in correct category
        self.assertEqual(data['question']['category'], '3')

        # check that question returned is not on previous q list
        self.assertNotEqual(data['question']['id'], 9)
        self.assertNotEqual(data['question']['id'], 11)

    # Tests playing quiz game failure 400
    def test_play_quiz_fails(self):
        

        # send post request without json data
        res = self.client().post('/quizzes', json={})

        # load response data
        data = json.loads(res.data)

        # check response status code and message
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()