# import os
# from flask import Flask, request, abort, jsonify, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS
# import random
# from random import randint 
# from models import setup_db, Question, Category

# QUESTIONS_PER_PAGE = 10
# #Pagination section
# def paginate_questions(request, selection):
#   page = request.args.get('page', 1, type=int)
#   start = (page - 1) * QUESTIONS_PER_PAGE
#   end = start + QUESTIONS_PER_PAGE

#   questions = [question.format() for question in selection]
#   current_questions = questions[start:end]

#   return current_questions

#   #  @app.route('/questions', methods=['POST'])
 


# def create_app(test_config=None):
#   # create and configure the app
#   app = Flask(__name__)
#   setup_db(app)
#   # '
#     # @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
#     # '
#   CORS(app, resources={r'/': {'origins': '*'}})
#   # '
#   # @TODO: Use the after_request decorator to set Access-Control-Allow
#   # '

#   @app.after_request
#   def after_request(response):
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
#     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     return (response)

#   # def search_code(searchTerm):
#   #     #  # load the request body
#   #     body = request.get_json()

#   #     # if search term is present
#   #     if (body.get('searchTerm')):
#   #       search_term = body.get('searchTerm')

#   #       # Go through database using searchTerm to fetch the results
#   #       selection = Question.query.filter(
#   #           Question.question.ilike(f'%{search_term}%')).all()

#   #       # return 404 if no results found
#   #       if (len(selection) == 0):
#   #           abort(404)

#   #       # paginate the results
#   #       paginated = paginate_questions(request, selection)

#   #       # return results
#   #       return jsonify({
#   #           'success': True,
#   #           'questions': paginated,
#   #           'total_questions': len(Question.query.all())
#   #       })

#     # '
#   # @TODO: 
#   # Create an endpoint to handle GET requests 
#   # for all available categories.
#   # '
#   @app.route('/categories')
#   def retrieve_categories():
   

#     # get all categories and add to dict
#     categories = Category.query.all()
#     categories_dict = {}
#     for category in categories:
#       #  store the category type in the dictionary
#         categories_dict[category.id] = category.type

#     # abort 404 if no categories found
#     if (len(categories_dict) == 0):
#         abort(404)

#     # return data to view
#     return jsonify({
#         'success': True,
#         'categories': categories_dict
#     })
  

#   # '
#   # @TODO: 
#   # Create an endpoint to handle GET requests for questions, 
#   # including pagination (every 10 questions). 
#   # This endpoint should return a list of questions, 
#   # number of total questions, current category, categories. 

#   # TEST: At this point, when you start the application
#   # you should see questions and categories generated,
#   # ten questions per page and pagination at the bottom of the screen for three pages.
#   # Clicking on the page numbers should update the questions. 
#   # '
 
#   @app.route('/questions')
#   def retrieve_questions():
    

#       # get all questions and paginate
#       selection = Question.query.order_by(Question.id).all()
#       total_questions = len(selection)
#       current_questions = paginate_questions(request, selection)

#       # get all categories and add to dict
#       categories = Category.query.all()
#       categories_dict = {}
#       for category in categories:

#       # store the category type in the dictionary
#           categories_dict[category.id] = category.type

#       # abort 404 if no questions
#       if (len(current_questions) == 0):
#           abort(404)

#       # return data to view
#       return jsonify({
#           'success': True,
#           'questions': current_questions,
#           'total_questions': total_questions,
#           'categories': categories_dict
#       })
  
#   # '
#   # @TODO: 
#   # Create an endpoint to DELETE question using a question ID. 

#   # TEST: When you click the trash icon next to a question, the question will be removed.
#   # This removal will persist in the database and when you refresh the page. 
#   # '
#   @app.route('/questions/<int:question_id>', methods=['DELETE'])
#   def delete_question(question_id):

#     try:
#       question = Question.query.filter(Question.id == question_id).one_or_none()
      
      
#       # abort 404 if no question found
#       if question is None:
#         abort(404) 
    
    
#       # delete the question
#       question.delete()
#       # flash('Question ' + question_id + ' was successfully deleted!')
#       return jsonify(
#         {
#           'success': True,
#           'deleted': question_id,
#           'message': 'Question Successfully deleted'

#         }
#       )

#     except:
#         abort(422)

  

#   # '
#   # @TODO: 
#   # Create an endpoint to POST a new question, 
#   # which will require the question and answer text, 
#   # category, and difficulty sc

#   # TEST: When you submit a question on the 'Add' tab, 
#   # the form will clear and the question will appear at the end of the last page
#   # of the questions list in the 'List' tab.  
#   # '
#   @app.route('/questions', methods=['POST'])
#   def create_question():

#     # search = search_code(searchTerm)

#     # load the request body
#     body = request.get_json()

#     #  if search term is present
#     if (body.get('searchTerm')):
#       search_term = body.get('searchTerm')
#       # Wildcards search before and after
#       selection = Question.query.filter(
#           Question.question.ilike('%' + search_term + '%')).all()

#       # return 404 if no results found
#       if (len(selection) == 0):
#           abort(404)

#       # paginate the results
#       paginated = paginate_questions(request, selection)

#       # return results
#       return jsonify({
#           'success': True,
#           'questions': paginated,
#           'total_questions': len(Question.query.all())
#       })

#     else:
   
#            # Assign the keyed in values to the variables
#           new_question = body.get('question', None)
#           new_answer = body.get('answer', None)
#           new_difficulty = body.get('difficulty', None)
#           new_category = body.get('category', None)
    
    
#     try:
#       # Assign variables to the column names
#       question = Question(
#       question=new_question, 
#       answer=new_answer, 
#       difficulty=new_difficulty, 
#       category=new_category)

#       # Update the table records
#       question.insert()

#       selection = Question.query.order_by(Question.id).all()
#       current_questions = paginate_questions(request, selection)

#       return jsonify(
#         {
#           'success': True,
#           'created': question.id,
#           'question_created': question.question,
#           'questions': current_questions,
#           'total_question': len(Question.query.all()),
#         }
#       )
    
#     except:
#       # abort if unprocessable
#       abort(422)

#  # '
#   # @TODO: 
#   # Create a POST endpoint to get questions based on a search term. 
#   # It should return any questions for whom the search term 
#   # is a substring of the question. 

#   # TEST: Search by any phrase. The questions list will update to include 
#   # only question that include that string within their question. 
#   # Try using the word 'title' to start. 
#   # '

#   @app.route('/questions', methods=['POST'])
#   def search_questions():
#     # search_code(searchTerm)
#     #  # load the request body
# # search_term=request.form.get('search_term', '')
# #     venues = Venue.query.filter(Venue.name.ilike('%' + search_term + '%')).all()   # Wildcards search before and after
# #         #print(venues)
# #     venue_list = []
# #     now = datetime.now()
# #     for venue in venues:
# #         # venue_shows = Show.query.filter_by(venue_id=venue.id).all()
# #         venue_shows = Venue.query.join(Show).filter_by(artist_id=self.id).filter(
# #             Show.start_time > datetime.now()).count()
# #         num_upcoming = 0
# #         for show in venue_shows:
# #             if show.start_time > now:
# #                 num_upcoming += 1

# #         venue_list.append({
# #             "id": venue.id,
# #             "name": venue.name,
# #             "city": venue.city,
# #             "state": venue.state,
# #             "num_upcoming_shows": num_upcoming  # FYI, template does nothing with this
# #         })

# #     response = {
# #         "count": len(venues), #return the number of elements in the sequence
# #         "data": venue_list
# #     }

# #     body = request.get_json()

#      # if search term is present
#     if (body.get('searchTerm')):
#       search_term = body.get('searchTerm')

#      # Wildcards search before and after
#       selection = Question.query.filter(
#           Question.question.ilike('%' + search_term + '%')).all()

#       # return 404 if no results found
#       if (len(selection) == 0):
#           abort(404)

#       # paginate the results
#       paginated = paginate_questions(request, selection)

#       # return results
#     return jsonify({
#         'success': True,
#         'questions': paginated,
#         'total_questions': len(Question.query.all())
#     })

#   # '
#   # @TODO: 
#   # Create a GET endpoint to get questions based on category. 

#   # TEST: In the 'List' tab / main screen, clicking on one of the 
#   # categories in the left column will cause only questions of that 
#   # category to be shown. 
#   # '
#   @app.route('/categories/<int:id>/questions')
#   def retrieve_category_questions(id):
#     #fetch the category by ID
#     category = Category.query.filter_by(id=id).one_or_none()

#     # return 400 if category is none
#     if (category is None):
#       abort(400)

#       #retrieve the questions in the category
#     selection = Question.query.filter_by(category=category.id).all()

#     categorized_pages = paginate_questions(request, selection)

#     #Display result
#     return jsonify(
#       {
#         'success': True,
#         'questions': categorized_pages,
#         'total_questions': len(Question.query.all()),
#         'current_category': category.type

#       }
#     )

#   # '
#   # @TODO: 
#   # Create a POST endpoint to get questions to play the quiz. 
#   # This endpoint should take category and previous question parameters 
#   # and return a random questions within the given category, 
#   # if provided, and that is not one of the previous questions. 

#   # TEST: In the 'Play' tab, after a user selects 'All' or a category,
#   # one question at a time is displayed, the user is allowed to answer
#   # and shown whether they were correct or not. 
#   # '
#   @app.route('/quizzes', methods=['POST'])
#   def retrieve_random_quiz_question():


#     # load the request body
#     body = request.get_json()

#     # fetch the previous questions
#     previous_questions = body.get('previous_questions')

#     # fetch the category
#     category = body.get('quiz_category')

#     # return 400 if category or previous questions is not found
#     if ((category is None) or (previous_questions is None)):
#         abort(400)

#     # load all questions if the "ALL" category is selected
#     if (category['id'] == 0):
#         questions = Question.query.all()
#     # display questions for given category
#     else:
#         questions = Question.query.filter_by(category=category['id']).all()

#     # get total number of questions
#     total = len(questions)

#     # fetch a random question
#     def retrieve_random_question():
#         return questions[random.randint(0, len(questions)-1)]

#     # sort to know whether question has already been used
#     def sort_used_quiz(question):
#         used = False
#         for pq in previous_questions:
#             if (pq == question.id):
#                 used = True

#         return used

#     # retrieve random question
#     question = retrieve_random_question()

#     # check whether used, until unused question found and execute
#     while (sort_used_quiz(question)):
#         question = retrieve_random_question()

#         # if all questions have been attempted, return without question
#         if (len(previous_questions) == total):
#             return jsonify({
#                 'success': True
#             })

#     # return the question
#     return jsonify({
#         'success': True,
#         'question': question.format()
#     })
#   # '
#   # @TODO: 
#   # Create error handlers for all expected errors 
#   # including 404 and 422. 
#   # '
#      #___________ERROR HANDLER_______
#   @app.errorhandler(404)
#   def not_found(error):
#     return jsonify({
#         "success": False,
#         "error": 404,
#         "message": "resource not found"
#     }), 404

#   @app.errorhandler(422)
#   def unprocessable(error):
#       return jsonify({
#           "success": False,
#           "error": 422,
#           "message": "unprocessable"
#       }), 422

#   @app.errorhandler(400)
#   def bad_request(error):
#       return jsonify({
#           "success": False,
#           "error": 400,
#           "message": "bad request"
#       }), 400
#   return app

    