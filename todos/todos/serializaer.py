from rest_framework import serializers
from .models import Todo

# 직렬화란 클래스 형식으로 작성된 데이터를 통신에 적합한 형태로 재구성해주는 것을 말한다.
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title']