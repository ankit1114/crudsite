from django.shortcuts import render, redirect
from crudapp.forms import DetailsForm
from crudapp.models import Details
# Create your views here.
def det(request):
    if request.method == "POST":
        form = DetailsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = DetailsForm()
    return render(request,'index.html',{'form':form})
def show(request):
    crudapps = Details.objects.all()
    return render(request,"show.html",{'crudapps':crudapps})
def edit(request, id):
    crudapp = Details.objects.get(id=id)
    return render(request,'edit.html', {'crudapp':crudapp})
def update(request, id):
    crudapp = Details.objects.get(id=id)
    form = DetailsForm(request.POST, instance = crudapp)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'crudapp': crudapp})
def destroy(request, id):
    crudapp = Details.objects.get(id=id)
    crudapp.delete()
    return redirect("/show")
