from django.shortcuts import render, redirect
from django.http import *
from .models import *
from .forms import *
from django.template import *
from datetime import datetime
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from random import randint, sample

# Create your views here.

def to_index(request):
    return redirect('miseem:index')

def index(request):
    response = render(request, 'miseem_index.html')
    return response

def example(request, current):
    context = {}
    context['current'] = current
    if current == 1:
        context['head'] = "The 1st example!"
        context['body'] = "This is the first kind of task. You should read the description and the standard answer of the question. Then give the absolute score for the following one sentence. the score range is from 1 to 10."
    elif current == 2:
        context['head'] = "The 2nd example!"
        context['body'] = "This is the second kind of task. You should read the description and the standard answer of the question. Then give the relative score for the following two sentence, the result is limited to three, either one Win or Tie."
    elif current == 3:
        context['head'] = "The 3rd example!"
        context['body'] = "This is the third kind of task. You should read the description and the standard answer of the question. Then give the rank score for the following three sentence, the result is limited to six different order of the three."
    else:
        return render(request, 'sorry.html')
    if request.method == "GET":
        if current == 1:
            total_num = Sentence.objects.count()-1
            chosen_id = randint(0, total_num)
            chosen_sentence = Sentence.objects.all()[chosen_id]
            chosen_question = chosen_sentence.belong_to_question
            context['chosen_sentence'] = [(chosen_sentence.pk, chosen_sentence.content)]
            context['chosen_description'] = chosen_question.description
            context['chosen_standard'] = chosen_question.standard
            context['form'] = PointWise()
        elif current == 2:
            chosen_sentence_list = []
            total_question_num = Question.objects.count()-1
            total_system_num = System.objects.count() - 1
            while len(chosen_sentence_list) < 2:
                chosen_system_list = sample(list(System.objects.all()), 2)
                chosen_system_1 = chosen_system_list[0]
                chosen_system_2 = chosen_system_list[1]
                chosen_question = sample(list(Question.objects.all()), 1)[0]
                chosen_sentence_list = Sentence.objects.filter(belong_to_question = chosen_question).filter(Q(belong_to_system = chosen_system_1) | Q(belong_to_system = chosen_system_2))
            chosen_sentence = sample(list(chosen_sentence_list), 2) 
            chosen_sentence_1 = chosen_sentence[0]
            chosen_sentence_2 = chosen_sentence[1]
            context['chosen_sentence'] = [(chosen_sentence_1.pk, chosen_sentence_1.content), 
                                        (chosen_sentence_2.pk, chosen_sentence_2.content)]
            context['chosen_description'] = chosen_question.description
            context['chosen_standard'] = chosen_question.standard            
            context['form'] = PairWise()
        else:
            chosen_sentence_list = []
            total_question_num = Question.objects.count()-1
            total_system_num = System.objects.count() - 1
            while len(chosen_sentence_list) < 3:
                chosen_system_list = sample(list(System.objects.all()), 3) 
                chosen_system_1 = chosen_system_list[0]
                chosen_system_2 = chosen_system_list[1]
                chosen_system_3 = chosen_system_list[2]
                chosen_question = sample(list(Question.objects.all()), 1)[0]
                chosen_sentence_list = Sentence.objects.filter(belong_to_question = chosen_question).filter(Q(belong_to_system = chosen_system_1) | Q(belong_to_system = chosen_system_2) | Q(belong_to_system = chosen_system_3))
            chosen_sentence = sample(list(chosen_sentence_list), 3) 
            chosen_sentence_1 = chosen_sentence[0]
            chosen_sentence_2 = chosen_sentence[1]
            chosen_sentence_3 = chosen_sentence[2]
            context['chosen_sentence'] = [(chosen_sentence_1.pk, chosen_sentence_1.content), 
                                        (chosen_sentence_2.pk, chosen_sentence_2.content), 
                                        (chosen_sentence_3.pk, chosen_sentence_3.content)]
            context['chosen_description'] = chosen_question.description
            context['chosen_standard'] = chosen_question.standard
            context['form'] = ListWise()
    elif request.method != "POST":
        response = render(request, 'sorry.html')
    response = render(request, 'example.html', context)
    return response

def quiz(request):
    context = {}
    if request.method == "GET":
        context['form'] = Quiz()
    elif request.method == "POST":
        context['form'] = Quiz(request.POST)
        if context['form'].is_valid():
            print(context['form'].cleaned_data)
            money = context['form'].cleaned_data['money']
            task = context['form'].cleaned_data['task']
            score = context['form'].cleaned_data['score']
            sentence = context['form'].cleaned_data['sentence']
            if money != str(1) or task != str(1) or score != str(0) or sentence != str(1):
                return render(request, 'sorry.html')
        else:
            return render(request, 'sorry.html')
    else:
        return render(request, 'sorry.html')
    response = render(request, 'quiz.html', context)
    return response

def entry(request):
    context = {}
    if request.method == "GET":
        if request.user.is_authenticated:
            response = render(request, 'sorry.html')
        else:
            response = render(request, 'entry.html', context)
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
        else:
            if User.objects.filter(username=username).first() != None:
                return render(request, 'sorry.html')
            user = User.objects.create_user(username=username, password=password)
        response = render(request, 'entry.html', context)
    else:
        response = render(request, 'sorry.html')
    return response

def task(request):
    if not request.user.is_authenticated:
        return render(request, 'sorry.html')
    MAX_ANSWER_NUM = 32
    if request.method == "GET":
        if Answer.objects.filter(belong_to_noter = request.user).count() > MAX_ANSWER_NUM:
            print(Answer.objects.filter(belong_to_noter = request.user).count())
            return render(request, 'sorry.html')
        current = randint(1, 3)
    elif request.method == "POST":
        current = int(request.POST['current'])
    else:
        return render(request, 'sorry.html')
    context = {}
    context['current'] = current
    if current == 1:
        context['head'] = "The 1st kind of task!"
        context['body'] = "This is the first kind of task. You should read the description and the standard answer of the question. Then give the absolute score for the following one sentence. the score range is from 1 to 10."
    elif current == 2:
        context['head'] = "The 2nd kind of task!"
        context['body'] = "This is the second kind of task. You should read the description and the standard answer of the question. Then give the relative score for the following two sentence, the result is limited to three, either one Win or Tie."
    elif current == 3:
        context['head'] = "The 3rd kind of task!"
        context['body'] = "This is the third kind of task. You should read the description and the standard answer of the question. Then give the rank score for the following three sentence, the result is limited to six different order of the three." 
    else:
        return render(request, 'sorry.html')
    if request.method == "GET":  
        if current == 1:
            total_num = Sentence.objects.count()-1
            chosen_id = randint(0, total_num)
            chosen_sentence = Sentence.objects.all()[chosen_id]
            chosen_question = chosen_sentence.belong_to_question
            context['chosen_sentence'] = [(chosen_sentence.pk, chosen_sentence.content)]
            context['chosen_description'] = chosen_question.description
            context['chosen_standard'] = chosen_question.standard
            context['form'] = PointWise()
        elif current == 2:
            chosen_sentence_list = []
            while len(chosen_sentence_list) < 2:
                chosen_system_list = sample(list(System.objects.all()), 2)
                chosen_system_1 = chosen_system_list[0]
                chosen_system_2 = chosen_system_list[1]
                chosen_question = sample(list(Question.objects.all()), 1)[0]
                chosen_sentence_list = Sentence.objects.filter(belong_to_question = chosen_question).filter(Q(belong_to_system = chosen_system_1) | Q(belong_to_system = chosen_system_2))
            chosen_sentence = sample(list(chosen_sentence_list), 2) 
            chosen_sentence_1 = chosen_sentence[0]
            chosen_sentence_2 = chosen_sentence[1]
            context['chosen_sentence'] = [(chosen_sentence_1.pk, chosen_sentence_1.content), 
                                        (chosen_sentence_2.pk, chosen_sentence_2.content)]
            context['chosen_description'] = chosen_question.description
            context['chosen_standard'] = chosen_question.standard            
            context['form'] = PairWise()
        else:
            chosen_sentence_list = []
            while len(chosen_sentence_list) < 3:
                chosen_system_list = sample(list(System.objects.all()), 3) 
                chosen_system_1 = chosen_system_list[0]
                chosen_system_2 = chosen_system_list[1]
                chosen_system_3 = chosen_system_list[2]
                chosen_question = sample(list(Question.objects.all()), 1)[0]
                chosen_sentence_list = Sentence.objects.filter(belong_to_question = chosen_question).filter(Q(belong_to_system = chosen_system_1) | Q(belong_to_system = chosen_system_2) | Q(belong_to_system = chosen_system_3))
            chosen_sentence = sample(list(chosen_sentence_list), 3) 
            chosen_sentence_1 = chosen_sentence[0]
            chosen_sentence_2 = chosen_sentence[1]
            chosen_sentence_3 = chosen_sentence[2]
            context['chosen_sentence'] = [(chosen_sentence_1.pk, chosen_sentence_1.content), 
                                        (chosen_sentence_2.pk, chosen_sentence_2.content), 
                                        (chosen_sentence_3.pk, chosen_sentence_3.content)]
            context['chosen_description'] = chosen_question.description
            context['chosen_standard'] = chosen_question.standard
            context['form'] = ListWise()
    else:
        if current == 1:
            form = PointWise(request.POST)
            if not form.is_valid():
                return render(request, 'sorry.html')
            chosen_sentence = Sentence.objects.get(pk=request.POST['1'])
            chosen_question = chosen_sentence.belong_to_question
            chosen_user = request.user
            absolute_score = int(form.cleaned_data['absolute_score'])
            answer = Answer(belong_to_noter = chosen_user, belong_to_type = current, 
                            first = chosen_sentence, absolute_score = absolute_score)
        elif current == 2:
            form = PairWise(request.POST)
            if not form.is_valid():
                return render(request, 'sorry.html')
            chosen_sentence_1 = Sentence.objects.get(pk=request.POST['1'])
            chosen_sentence_2 = Sentence.objects.get(pk=request.POST['2'])
            chosen_user = request.user
            relative_score = int(form.cleaned_data['relative_score'])
            answer = Answer(belong_to_noter = chosen_user, belong_to_type = current, 
                            first = chosen_sentence_1, second = chosen_sentence_2, relative_score = relative_score)
        else:
            form = ListWise(request.POST)
            if not form.is_valid():
                return render(request, 'sorry.html')
            chosen_sentence_1 = Sentence.objects.get(pk=request.POST['1'])
            chosen_sentence_2 = Sentence.objects.get(pk=request.POST['2'])
            chosen_sentence_3 = Sentence.objects.get(pk=request.POST['3'])
            chosen_user = request.user
            rank_score = int(form.cleaned_data['rank_score'])
            answer = Answer(belong_to_noter = chosen_user, belong_to_type = current, 
                            first = chosen_sentence_1, second = chosen_sentence_2, third = chosen_sentence_3, rank_score = rank_score)
        answer.save()
        context['finished_num'] = Answer.objects.filter(belong_to_noter = chosen_user).count()
        context['done'] = (context['finished_num'] > MAX_ANSWER_NUM)
    response = render(request, 'task.html', context)
    return response

def sorry(request):
    response = render(request, 'sorry.html')
    return response

def thanks(request):
    response = render(request, 'thanks.html')
    return response
