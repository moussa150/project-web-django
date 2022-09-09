from urllib import request
from django.shortcuts import render

from voitures.models import Voiture
from django.shortcuts import redirect
from voitures.models import VoitureForm
from django.contrib import messages
# Create your views here.


#retourne toutes les voitures
def allVoiture(request):
    voitures=Voiture.objects.all()
    return render(request,'voitures/list-voiture.html',{'voitures':voitures})


#retourne Une Voiure
def getVoiture(request,id):
    voiture=Voiture.objects.get(id=id)
    return render(request,'voitures/detail-voiture.html',{'voiture':voiture})




#ajouter une voiture
def addVoiture(request):
    if request.method=='POST':

        form=VoitureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully saved')
            return redirect('list-voiture')
                
    else:
        form=VoitureForm()
    
    return render(request,'voitures/add-voiture.html',{'form':form})



#update voiture
def updateVoiture(request,id):
    voiture=Voiture.objects.get(id=id)

    if request.method=='POST':
        form=VoitureForm(request.POST,instance=voiture)

        if form.is_valid():
            form.save()
            return redirect('detail-voiture',voiture.id)
    
    else:
        form=VoitureForm(instance=voiture)
    
    return render (request,'voitures/update-voiture.html',{'form':form})

#delete Voiture
def deleteVoiture(request,id):
    voiture=Voiture.objects.get(id=id)

    if request.method == 'POST':
        voiture.delete()

        return redirect('list-voiture')
    
    return render(request, 'voitures/delete-voiture.html',{'voiture':voiture})