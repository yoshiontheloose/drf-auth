from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Pokemon

class PokemonTests(TestCase):

  @classmethod
  def setUpTestData(cls):
      testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
      testuser1.save()

      test_thing = Pokemon.objects.create(name='Bulbasaur', owner=testuser1,type='grass, poison type')
      test_thing.save()

  def test_pokemon_model(self):
      pokemon = Pokemon.objects.get(id=1)
      actual_owner = str(pokemon.owner)
      actual_name = str(pokemon.name)
      actual_type = str(pokemon.type)
      self.assertEqual(actual_owner,'testuser')
      self.assertEqual(actual_name, 'Bulbasaur')
      self.assertEqual(actual_type,'grass, poison type')