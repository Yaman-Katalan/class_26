from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Pet
# Create your tests here.

class PetsTests(TestCase):
    @classmethod
    def setUpTestData(cls): # class method
        testuser1 = get_user_model().objects.create_user (
            username='test_user',
            email='test@email.com',
            password='1234'
        )

        test_pet = Pet.objects.create(
            owner = testuser1,
            name = 'test_pet',
            des = 'test des',
            breed = 'breed_test'
        )

    def test_str_method(self):
        pet = Pet.objects.get(id=1)
        self.assertEqual(str(pet.name), 'test_pet')
    