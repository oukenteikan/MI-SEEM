from django.db.models import Q
from django.forms import *
from .models import *
from random import randint, sample

class PointWise(Form):
    
    total_num = Sentence.objects.count()-1
    chosen_id = randint(0, total_num)
    chosen_sentence = Sentence.objects.all()[chosen_id]
    chosen_question = chosen_sentence.belong_to_question

    chosen_sentence_pk = IntegerField(widget = HiddenInput(), initial=chosen_sentence.pk, disabled = True)
    description = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_question.description, disabled = True)
    standard = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_question.standard, disabled = True)
    sentence = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_sentence.content, disabled = True)
    score = FloatField(max_value = 10, min_value = 0)

class PairWise(Form):
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

    chosen_sentence_pk_1 = IntegerField(widget = HiddenInput(), initial=chosen_sentence_1.pk, disabled = True)
    chosen_sentence_pk_2 = IntegerField(widget = HiddenInput(), initial=chosen_sentence_2.pk, disabled = True)
    description = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_question.description, disabled = True)
    standard = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_question.standard, disabled = True)
    first = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_sentence_1.content, disabled = True)
    second = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_sentence_2.content, disabled = True)
    score = ChoiceField(
        choices=((1, 'The first is better.'), (-1, 'The second is better.'), (0, 'I think it is a tie.')),
        widget=RadioSelect
    )

class ListWise(forms.Form):
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

    chosen_sentence_pk_1 = IntegerField(widget = HiddenInput(), initial=chosen_sentence_1.pk, disabled = True)
    chosen_sentence_pk_2 = IntegerField(widget = HiddenInput(), initial=chosen_sentence_2.pk, disabled = True)
    chosen_sentence_pk_3 = IntegerField(widget = HiddenInput(), initial=chosen_sentence_3.pk, disabled = True)
    description = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_question.description, disabled = True)
    standard = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_question.standard, disabled = True)
    first = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_sentence_1.content, disabled = True)
    second = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_sentence_2.content, disabled = True)
    third = CharField(widget = TextInput(attrs={'size': '128'}), initial=chosen_sentence_3.content, disabled = True)
    score = ChoiceField(
        choices=((1, 'The first is the best and the second is the worst.'), 
                (2, 'The first is the best and the third is the worst.'),
                (3, 'The second is the best and the first is the worst.'),
                (4, 'The second is the best and the third is the worst.'),
                (5, 'The third is the best and the first is the worst.'),
                (6, 'The third is the best and the second is the worst.')),
        widget=RadioSelect
    )

class Quiz(Form):
    score = ChoiceField(
        choices=((1, 'The first is better.'), (-1, 'The second is better.'), (0, 'I think it is a tie.')),
        widget=RadioSelect
    )