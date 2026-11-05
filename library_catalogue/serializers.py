from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'title', 'subtitle', 'author', 'isbn', 'price']

#1 Checking all fields under the one function.
    def validate(self, data):
        title = data.get('title', None)
        author = data.get("author", None)

        #title checking for verifying it is only letters
        if not title.isalpha():
            raise  ValidationError(
                {
                    "status": False,
                    "message": "Title should include only letters."
                }
            )
        #checking author and title
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Title and authors should  not be the same."
                }
            )

        return data

#2 Checking each field separately with specially created functions
    def validate_price(self, price):
        if price < 0 or price > 99999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Price is wrongly added."
                }
            )



# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField(max_length=300)
#     author = serializers.CharField(max_length=100)
#     isbn = serializers.IntegerField()
#     price = serializers.DecimalField()

# class CashSerializer(serializers.Serializer):
#     input = serializers.CharField(max_length=120)
#     output = serializers.CharField(max_length=120)

