from django.forms import *

class PointWise(Form):
    absolute_score = IntegerField(max_value = 10, min_value = 0)

class PairWise(Form):
    relative_score = ChoiceField(
        choices=((1, 'The first is better.'), (-1, 'The second is better.'), (0, 'I think it is a tie.')),
        widget=RadioSelect
    )

class ListWise(Form):
    rank_score = ChoiceField(
        choices=((1, '132(The first is the best and the second is the worst.)'), 
                (2, '123(The first is the best and the third is the worst.)'),
                (3, '231(The second is the best and the first is the worst.)'),
                (4, '213(The second is the best and the third is the worst.)'),
                (5, '321(The third is the best and the first is the worst.)'),
                (6, '312(The third is the best and the second is the worst.)')),
        widget=RadioSelect
    )

class Quiz(Form):
    money = ChoiceField(
        choices=((0, '$0.5'), (1, '$0.64'), (2, '$1')),
        widget=RadioSelect
    )
    task = ChoiceField(
        choices=((0, '20'), (1, '32'), (2, '48')),
        widget=RadioSelect
    )
    score = ChoiceField(
        choices=((0, 'absolute score'), (1, 'relative score'), (2, 'rank score')),
        widget=RadioSelect
    )
    sentence = ChoiceField(
        choices=((0, '2'), (1, '3'), (2, '4')),
        widget=RadioSelect
    )    
