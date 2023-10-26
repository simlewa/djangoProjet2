from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Info

def index(request):
    if request.method == 'POST':
            nom = request.POST.get('name')
            email = request.POST.get('email')
            commentaire = request.POST.get('message')

            info_instance = Info(nom=nom, email=email, commentaire=commentaire)
            info_instance.save()

        # Ajoutez ici toute logique de traitement supplémentaire ou de redirection après l'enregistrement des données

    return render(request, 'monapp/index.html')# Create your views here.

def index2(request):
    infos = Info.objects.all()
    return render(request, 'monapp/index2.html', {'infos': infos})

def index3(request, info_id):
    info = get_object_or_404(Info, pk=info_id)
    return render(request, 'monapp/update_info.html', {'info': info})


def update_info(request,info_id):
    info_instance = get_object_or_404(Info, pk=info_id)

    if request.method == 'POST':
        info_instance.nom = request.POST.get('nom')
        info_instance.email = request.POST.get('email')
        info_instance.commentaire = request.POST.get('commentaire')
        info_instance.save()

        # Ajoutez ici toute logique de traitement supplémentaire ou de redirection après la mise à jour

    return render(request, 'monapp/index.html')



def delete_info(request, info_id):
    info_instance = get_object_or_404(Info, pk=info_id)

    if request.method == 'POST':
        info_instance.delete()

    return render(request, 'monapp/update_info.html')


