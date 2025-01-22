from django.db import models

# Create your models here.

from django.core.validators import MinLengthValidator

# Define a Django model named 'Breed'. This model will represent a breed of cat in the database.
class Breed(models.Model):
    # Define a field 'name' of type CharField, which will store the name of the breed.
    # 'max_length=200' specifies that the maximum length of the name can be 200 characters.
    # 'validators' is a list of validators that will be applied to this field. Here, we use MinLengthValidator
    # to ensure that the name is at least 2 characters long. If not, the error message "Breed must be greater than 1 character" will be shown.
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Breed must be greater than 1 character")]
    )

    # Define the __str__ method, which returns a string representation of the Breed instance.
    # This is what will be displayed when you reference a Breed object in the Django admin or shell.
    def __str__(self):
        return self.name

# Define another Django model named 'Cat'. This model will represent a cat in the database.
class Cat(models.Model):
    # Define a field 'nickname' of type CharField, which will store the nickname of the cat.
    # 'max_length=200' specifies that the maximum length of the nickname can be 200 characters.
    # 'validators' is a list of validators that will be applied to this field. Here, we use MinLengthValidator
    # to ensure that the nickname is at least 2 characters long. If not, the error message "Nickname must be greater than 1 character" will be shown.
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )

    # Define a field 'weight' of type PositiveIntegerField, which will store the weight of the cat.
    # This field will only accept positive integers (e.g., 1, 2, 3, etc.).
    weight = models.PositiveIntegerField()

    # Define a field 'foods' of type CharField, which will store the types of food the cat eats.
    # 'max_length=300' specifies that the maximum length of the foods string can be 300 characters.
    foods = models.CharField(max_length=300)

    # Define a field 'breed' of type ForeignKey, which establishes a many-to-one relationship with the 'Breed' model.
    # 'on_delete=models.CASCADE' means that if the referenced Breed instance is deleted, all Cat instances associated with it will also be deleted.
    # 'null=False' specifies that this field cannot be null; every Cat must have a Breed.
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    # Define the __str__ method, which returns a string representation of the Cat instance.
    # This is what will be displayed when you reference a Cat object in the Django admin or shell.
    def __str__(self):
        return self.nickname

'''
Original:
class Breed(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Breed must be greater than 1 character")]
    )

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Nickname must be greater than 1 character")]
    )
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length=300)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nickname
'''


