from django.shortcuts import *
from django.http import *
from .models import *
from .forms import *
from django.template import *
from datetime import datetime
from django.db.models import Q
from random import randint, sample

# Create your views here.

def to_index(request):
    return redirect('miseem:index')

def index(request):
    response = render(request, 'miseem_index.html')
    return response

def example(request, current):
    #if request.COOKIES.get("visited_example"+str(current)):
    #    return render(request, 'sorry.html')
    context = {}
    context['current'] = current
    if current == 1:
        context['head'] = "The 1st example!"
    elif current == 2:
        context['head'] = "The 2nd example!"
    elif current == 3:
        context['head'] = "The 3rd example!"
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
        elif current == 3:
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
        else:
            return render(request, 'sorry.html')
        response = render(request, 'example.html', context)
    elif request.method == "POST":
        response = render(request, 'example.html', context)
        response.set_cookie("visited_example"+str(current), True)
    else:
        response = render(request, 'sorry.html')
    return response

def quiz(request):
    if request.COOKIES.get("visited_quiz"):
        return render(request, 'sorry.html')
    if request.method == "GET":
        context = {}
        context['form'] = Quiz()
        response = render(request, 'quiz.html', context)
    elif request.method == "POST":
        context = {}
        context['form'] = Quiz(request.POST)
        response.set_cookie("visited_quiz", True)
        response = render(request, 'quiz.html', context)
    else:
        response = render(request, 'sorry.html')
    return response

def entry(request):
    response = render(request, 'entry.html')
    return response

def task(request):
    MAX_ANSWER_NUM = 32
    if request.method == "GET":
        if Answer.objects.filter(belong_to_noter = request.user).count() > MAX_ANSWER_NUM:
            return render(request, 'sorry.html')
        current = randint(1, 3)
    elif request.method == "POST":
        current = int(request.POST['current'])
    else:
        return render(request, 'sorry.html')
    context = {}
    context['current'] = current
    if current == 1:
        context['head'] = "The 1st type of task!"
    elif current == 2:
        context['head'] = "The 2nd type of task!"
    elif current == 3:
        context['head'] = "The 3rd type of task!"
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
            absolute_score = round(10*float(form.cleaned_data['absolute_score']))
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
