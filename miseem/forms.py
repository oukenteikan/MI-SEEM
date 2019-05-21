from django.forms import *

class PointWise(Form):
    absolute_score = FloatField(max_value = 10, min_value = 0)

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
    score = ChoiceField(
        choices=((1, 'The first is better.'), (-1, 'The second is better.'), (0, 'I think it is a tie.')),
        widget=RadioSelect
    )