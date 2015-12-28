from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import loader
from questions.models import *

tags = [Tag(), Tag()]
tags[0].name = 'bender'
tags[1].name = 'black-jack'
usr = User()
usr.img = '/static/logo200.jpg'
usr.name = 'Bender'
question = Question()
question.id = 1
question.tags = tags
question.short_desc = 'Guys, I have trouble with a moon park. Can\'t find the black-jack...'
question.popularity = 7
question.title = 'How to build a moon park?'
question.ans_cnt = 10
question.user = usr
question.desc = 'Guys, I have trouble with a moon park. Can\'t find the black-jack... Guys, I have trouble with a moon park. Can\'t find the black-jack...'
question.ref = '/answers/'

answers = Answer()
answers.user = usr
answers.popularity = 7
answers.text = 'I don\'t know! :('


def index(request):
    rend_params = {'is_new': True, 'questions': [question] * 10, 'popular_tags': [tags[0]] * 6,
                   'popular_members': [usr] * 5, 'is_short': True}
    template = loader.get_template('questions.html')
    return HttpResponse(template.render(rend_params))


def popular(request):
    rend_params = {'is_new': False, 'questions': [question] * 10}
    template = loader.get_template('questions.html')
    return HttpResponse(template.render(rend_params))


def ask(request):
    return render_to_response('ask.html')


def answer(request):
    rend_params = {'question': question, 'answers': [answers] * 10}
    return render_to_response('answer.html', rend_params)


def search(request):
    return render_to_response('search.html')


def tag_search(request):
    return render_to_response('tag_search.html')
