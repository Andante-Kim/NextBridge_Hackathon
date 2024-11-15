from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')   # 글쓴이
    subject = models.CharField(max_length=200)                                                   # 제목
    content = models.TextField()                                                                 # 내용
    create_date = models.DateTimeField()                                                         # 등록 일시
    modify_date = models.DateTimeField(null=True, blank=True)                                    # 수정 일시
    voter = models.ManyToManyField(User, related_name='voter_question')                          # 추천인 추가

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')     # 글쓴이
    question = models.ForeignKey(Question, on_delete=models.CASCADE)                             # 해당 질문
    content = models.TextField()                                                                 # 내용
    create_date = models.DateTimeField()                                                         # 등록 일시
    modify_date = models.DateTimeField(null=True, blank=True)                                    # 수정 일시
    voter = models.ManyToManyField(User, related_name='voter_answer')                            # 추천인 추가