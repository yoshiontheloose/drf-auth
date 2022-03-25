from rest_framework import generics
from .serializer import PokemonSerializer
from .models import Pokemon
from .permissions import IsOwnerOrReadOnly

class PokemonList(generics.ListCreateAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Pokemon.objects.all()
  serializer_class = PokemonSerializer

class PokemonDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Pokemon.objects.all()
  serializer_class = PokemonSerializer
