from rest_framework.serializers import ModelSerializer 
from rest_framework.relations import SlugRelatedField 

from sections.models import Section, Content 


class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content 
        fields = '__all__'


class SectionContentSerializer(ModelSerializer):
    class Meta:
        model = Content 
        fields = ('id', 'title')


class SectionContentListSerializer(ModelSerializer):
    section = SlugRelatedField(slug_field='title', queryset=Section.objects.all())

    class Meta:
        model = Content
        fields = ('id', 'section', 'title')
