from django.shortcuts import render
from db.cosmosdb_client import CosmosDb

# Create your views here.
def get_pets(request):
    client = CosmosDb()
    pets = client.all()
    context = {'pets': pets}

    return render(request, 'index.html', context)