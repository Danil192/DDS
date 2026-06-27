from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Subcategory
from .serializers import CategorySerializer, SubcategorySerializer

class CategoriesByTypeView(APIView):
    def get(self, request, type_id):
        categories = Category.objects.filter(cash_type_id=type_id)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class SubcategoriesByCategoryView(APIView):
    def get(self, request, category_id):
        subcategories = Subcategory.objects.filter(category_id=category_id)
        serializer = SubcategorySerializer(subcategories, many=True)
        return Response(serializer.data)