from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListAPIView, 
    CreateAPIView, 
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser,
)
from sections.models import Section, Content
from sections.permissions import IsModerator, IsSuperUser
from sections.serializers.section_seralizers import (
    SectionSerializer, 
    SectionListSerializer,
)
from sections.serializers.content_serializers import (
    ContentSerializer,
    SectionContentSerializer,
    SectionContentListSerializer,
)
from sections.paginators import (
    SectionPaginator, 
    ContentPaginator,
)
    

class SectionListAPIView(ListAPIView):
    serializer_class = SectionListSerializer
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, )
    pagination_class = SectionPaginator


class SectionCreateAPIView(CreateAPIView):
    serializer_class = SectionSerializer 
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class SectionRetrieveAPIView(RetrieveAPIView):
    serializer_class = SectionSerializer 
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, )


class SectionUpdateAPIView(UpdateAPIView):
    serializer_class = SectionSerializer 
    queryset = Section.objects.all()
    # permission_classes = (AllowAny, )
    # permission_classes = (IsAuthenticated, IsModerator | IsSuperUser)


class SectionDestroyAPIView(DestroyAPIView):
    serializer_class = SectionSerializer  
    queryset = Section.objects.all()
    # permission_classes = (IsAuthenticated, IsSuperUser)
