from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    
    def to_representation(self, instance):
        # print(instance)
        repr = super().to_representation(instance)
        сhildren = instance.children.all()
        if сhildren:
            repr['children'] = CategorySerializer(сhildren, many=True).data
        # repr['example'] = 'hello world'
        # print(repr, '!!!!!!!!!!!!')
        return repr

    # добавляет дополнительные поля (пользовательские значание) при выводе