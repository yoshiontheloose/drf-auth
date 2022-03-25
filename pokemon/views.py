from rest_framework import generics
from .serializer import PokemonSerializer
from .models import Pokemon

class PokemonList(generics.ListCreateAPIView):
  queryset = Pokemon.objects.all()
  serializer_class = PokemonSerializer

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Pokemon.objects.all()
  serializer_class = PokemonSerializer
