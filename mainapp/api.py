from typing import List
from ninja import NinjaAPI

from .schemas import AutorSchema
from .models import Autor, Livro

api = NinjaAPI()

@api.get('pesquisar_autores/', response=List[AutorSchema])
def listar_autores(request):
    autores = Autor.objects.all()
    response = [{"id": autor.id, "nome": autor.nome} for autor in autores]
    return response