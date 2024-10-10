from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from base.models import Authors,Genre,Books
from .serializers import AuthorSerializer,GenreSerializer,BookSerializer
from rest_framework import status
from django.forms.models import model_to_dict
from django.db.models import Q


@api_view(['GET','POST'])

def author_get_post(request:Response):
    if request.method=='GET':
        author=Authors.objects.all()
        
        
        
        serializer=AuthorSerializer(author, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    
    if request.method=='POST':
        body=request.data
        serializer=AuthorSerializer(data=body)
        if serializer.is_valid():
            serializer.save()  # Save data to the database
            return Response(serializer.data, status.HTTP_201_CREATED)  # Return the saved data with a 201 Created status
        else:
            # If validation fails, return the validation errors
            return Response(serializer.errors, status=400)
        


@api_view(['GET','PUT','DELETE'])
def author_update_delete_get(request:Response,id):
    
        try:
            id=int(id)
        except ValueError:
            return Response({"details":"enter valid value"},status.HTTP_400_BAD_REQUEST)
        
        
        try:
            author=Authors.objects.get(id=id)
            if request.method=='GET':
            
                
                serializer=AuthorSerializer(author)
                return Response(serializer.data,status.HTTP_200_OK)
            
            
            
            if request.method=='PUT':
                body=request.data
                serializer=AuthorSerializer(author,data=body)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
                
            if request.method== 'DELETE':
                author.delete()
                return Response({"Message":"author directory deleted"})
        
        
        except Authors.DoesNotExist:
            return Response({"Author":"No Author found wit that ID"}, status.HTTP_404_NOT_FOUND)


#GENRE APIS


@api_view(['GET','POST'])

def Genre_get_post(request:Response):
    if request.method=='GET':
        genre=Genre.objects.all()
        serializer=GenreSerializer(genre, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    if request.method=='POST':
        body=request.data
        serializer=GenreSerializer(data=body)
        if serializer.is_valid():
            serializer.save()  # Save data to the database
            return Response(serializer.data, status.HTTP_201_CREATED)  # Return the saved data with a 201 Created status
        else:
            # If validation fails, return the validation errors
            return Response(serializer.errors, status=400)
        




@api_view(['GET','PUT','DELETE'])
def Genre_update_delete_get(request:Response,id):
    
        try:
            id=int(id)
        except ValueError:
            return Response({"details":"enter valid value"},status.HTTP_400_BAD_REQUEST)
        
        
        try:
            genre=Genre.objects.get(id=id)
            if request.method=='GET':
            
                
                serializer=GenreSerializer(genre)
                return Response(serializer.data,status.HTTP_200_OK)
            
            
            
            if request.method=='PUT':
                body=request.data
                serializer=GenreSerializer(genre,data=body)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
                
            if request.method== 'DELETE':
                genre.delete()
                return Response({"Message":"author directory deleted"})
        
        
        except Genre.DoesNotExist:
            return Response({"Genre":"No genre found wit that ID"}, status.HTTP_404_NOT_FOUND)



#BOOKS APIS


@api_view(['GET','POST'])

def book_get_post(request:Response):
    if request.method=='GET':
        
        title = request.query_params.get('title', None)
        genre_id=request.query_params.get('genre_id',None)
        author_id=request.query_params.get('author_id',None)
        
        books=Books.objects.all()
        
        filters = Q()
        
        if title is not None:
            filters &= Q(title__icontains=title)
            
        if genre_id is not None:
            filters &= Q(genre_id=genre_id)
              
        if author_id is not None:
            filters &= Q(author_id=author_id)
            
        books = books.filter(filters).all()  

        
        
        
        # # Serialize the results
        serializer = BookSerializer(books, many=True)
        
        # Return the serialized data as a response
        return Response(serializer.data, status=200)
    if request.method=='POST':
        body=request.data
        serializer=BookSerializer(data=body)
        if serializer.is_valid():
            serializer.save()  # Save data to the database
            return Response(serializer.data, status.HTTP_201_CREATED)  # Return the saved data with a 201 Created status
        else:
            # If validation fails, return the validation errors
            return Response(serializer.errors, status=400)
        




@api_view(['GET','PUT','DELETE'])
def Book_update_delete_get(request:Response,id):
    
        try:
            id=int(id)
        except ValueError:
            return Response({"details":"enter valid value"},status.HTTP_400_BAD_REQUEST)
        
        
        try:
            book=Books.objects.get(id=id)
            if request.method=='GET':
            
                
                serializer=BookSerializer(book)
                return Response(serializer.data,status.HTTP_200_OK)
            
            
            
            if request.method=='PUT':
                body=request.data
                serializer=BookSerializer(book,data=body)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status.HTTP_202_ACCEPTED)
                else:
                    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
                
            if request.method== 'DELETE':
                book.delete()
                return Response({"Message":"author directory deleted"})
        
        
        except Genre.DoesNotExist:
            return Response({"Genre":"No genre found wit that ID"}, status.HTTP_404_NOT_FOUND)
       