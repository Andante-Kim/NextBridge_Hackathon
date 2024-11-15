from django.contrib import admin
from .models import Question, Answer

# 질문(Question) 조회
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject'] # 제목으로 찾음

admin.site.register(Question, QuestionAdmin)

# 답변(Answer) 조회
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content'] # 내용으로 찾음

admin.site.register(Answer, AnswerAdmin)
