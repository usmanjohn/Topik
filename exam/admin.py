from django.contrib import admin

from .models import Test, Question, Choice, UserAnswer
admin.site.register([Test, Question, Choice, UserAnswer])
