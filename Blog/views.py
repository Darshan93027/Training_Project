from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer


class PostListView(APIView):
    permission_classes = [AllowAny]  # Public view - anyone can see posts with authication

    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostCRUD(APIView):
    permission_classes = [AllowAny]  

    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        if not request.user.is_authenticated:
            print("yes your are authenticated")
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            post = Post.objects.get(id=id, author=request.user)
        except Post.DoesNotExist:
            return Response({"error": "Post not found with given id or author not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            post = Post.objects.get(id=id, author=request.user)
        except Post.DoesNotExist:
            return Response({"error": "Post not found with given id or author not found"}, status=status.HTTP_404_NOT_FOUND)

        post.delete()
        return Response({"message": "Post deleted"}, status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):
    permission_classes = [AllowAny]  
    
    #this is ppublic view for anyone to see 
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryCRUD(APIView):
    permission_classes = [AllowAny]  

    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication need if "}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            category = Category.objects.get(id=id, author=request.user)
        except Category.DoesNotExist:
            return Response({"error": "Category not found  "}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            category = Category.objects.get(id=id, author=request.user)
        except Category.DoesNotExist:
            return Response({"error": "Category not found with given id or author not found"}, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response({"message": " Category deleted"}, status=status.HTTP_204_NO_CONTENT)