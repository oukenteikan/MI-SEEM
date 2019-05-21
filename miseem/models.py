from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length = 64)
    frequence = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Question(models.Model):
    description = models.TextField()
    standard = models.TextField()
    frequence = models.IntegerField(default = 0)

    def __str__(self):
        return "<Description: {}>\n<Standard: {}>".format(self.description, self.standard)

class Sentence(models.Model):
    belong_to_system = models.ForeignKey('System', on_delete = models.CASCADE)
    belong_to_question = models.ForeignKey('Question', on_delete = models.CASCADE)
    content = models.TextField()
    frequence = models.IntegerField(default = 0)

    def __str__(self):
        return "<Content: %s>" % self.content

class Answer(models.Model):
    belong_to_noter = models.ForeignKey(User, on_delete = models.CASCADE)
    belong_to_type = models.IntegerField(choices = ((1, 'pointwise'), (2, 'pairwise'), (3, 'listwise')))
    time = models.DateTimeField(auto_now_add = True)
    first = models.ForeignKey('Sentence', related_name = 'first_sentence', on_delete = models.CASCADE)
    second = models.ForeignKey('Sentence', related_name = 'second_sentence', on_delete = models.CASCADE, null = True)
    third = models.ForeignKey('Sentence', related_name = 'third_sentence', on_delete = models.CASCADE, null = True)
    absolute_score = models.IntegerField(choices = set((i, str(i/10)) for i in range(1, 101)), null = True)
    relative_score = models.IntegerField(choices = ((1, 'Win'), (0, 'Tie'), (-1, 'Lose')), null = True)
    rank_score = models.IntegerField(choices = ((1, '132'), (2, '123'), (3, '231'), (4, '213'), (5, '321'), (6, '312')), null = True)

    def __str__(self):
        if self.belong_to_type == 1:
            return "<Sentence: {}>\n<Score: {}>".format(self.first, self.absolute_score)
        elif self.belong_to_type == 2:
            return "<Sentence1: {}>\n<Sentence2: {}>\n<Score: {}>".format(self.first, self.second, self.relative_score)
        elif self.belong_to_type == 3:
            return "<Sentence1: {}>\n<Sentence2: {}>\n<Sentence3: {}>\n<Score: {}>".format(self.first, self.second, self.thrid, self.rank_score)
        else:
            return "Wrong answer!"



