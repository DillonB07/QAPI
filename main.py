from fastapi import FastAPI, HTTPException, status
from questions import questions
import random

app = FastAPI()


@app.get('/')
def index():
    return 'Hello! For QAPI documentation, please visit https://qapi.ml'


@app.get('/random-question')
def random_question():
    length = len(questions.keys())
    number = random.randint(1, length)
    print(questions.get(number))
    return questions.get(number)


# @app.get('/topic/{topic}/all-questions')
# def all_questions_in_topic(topic: str):
#     topic_questions = {}
#     topic_found = False
#     number = 0
#     for question in questions.values():
#         if question['topic'] == topic:
#             number += 1
#             topic_found = True
#             topic_questions[number] = question

#     if topic_found:
#         return topic_questions
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail='Topic not found')


@app.get('/topic/{topic}/random-question')
def random_question_in_topic(topic: str):
    topic_questions = []
    topic_found = False
    for question in questions.values():
        if question['topic'] == topic:
            topic_found = True
            topic_questions.append(question)

    if topic_found:
        question = random.choice(topic_questions)
        return question
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Topic not found')


# @app.get('/type/{type}/all-questions')
# def all_type_questions(type: str):
#     type_questions = {}
#     type_found = False
#     number = 0
#     for question in questions.values():
#         if question['type'] == type:
#             number += 1
#             type_found = True
#             type_questions[number] = question

#     if type_found:
#         return type_questions
#     else:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail='Type not found')


@app.get('/type/{type}/random-question')
def random_type_question(type: str):
    type_questions = []
    type_found = False
    for question in questions.values():
        if question['type'] == type:
            type_found = True
            type_questions.append(question)

    if type_found:
        question = random.choice(type_questions)
        return question
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Type not found')


# Statistics

@app.get('/statistics/total')
def total_questions():
    number = 0
    for question in questions:
        number += 1

    return number


@app.get('/statistics/type/{question_type}')
def statistics_for_type(question_type: str):
    type_found = False
    number = 0
    for question in questions.values():
        if question['type'] == question_type:
            number += 1
            type_found = True

    if type_found:
        return number
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Type not found')


@app.get('/statistics/topic/{topic}')
def statistics_for_topic(topic: str):
    topic_found = False
    number = 0
    for question in questions.values():
        if question['topic'] == topic:
            number += 1
            topic_found = True

    if topic_found:
        return number
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Topic not found')
