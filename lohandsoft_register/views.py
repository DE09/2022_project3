from django.shortcuts import render,redirect
from .forms import lohandsoftForm
from .models import lohandsoft
from django.db.models import Q

# Create your views here.

def search_list(request):
    lohandlist = lohandsoft_list.objects.all()
    search = request.POST.get('search','')
    if search:
        lo_filtered = lohandlist.filter(
            Q(fullname__icontains = search) | 
            Q(birth__icontains = search) | 
            Q(email__icontains = search) | 
            Q(age__icontains = search)
        ).distinct()
    context = {'search': lo_filtered }
    return render(request, 'lohandsoft_register/search_list.html',context)


def lohandsoft_list(request):
    context = {'lohandsoft_list':lohandsoft.objects.all()}
    return render(request,"lohandsoft_register/lohandsoft_list.html",context)

def lohandsoft_form(request,id=0): #id추가를 해야하는 이유
    if request.method == "GET":
        if id == 0:
            form = lohandsoftForm()
        else:
            lo = lohandsoft.objects.get(pk=id)
            form = lohandsoftForm(instance=lo)
        return render(request,"lohandsoft_register/lohandsoft_form.html", {'form': form})


    else:
        if id == 0:
            form = lohandsoftForm(request.POST)
        else:
            lo = lohandsoft.objects.get(pk=id)
            form = lohandsoftForm(request.POST,instance= lo) # 기존 data에서 수정된 data를 web에서 조회할때
        if form.is_valid(): 
            form.save() 
        return redirect('/lohandsoft/list')  #요거 return하고 import redirect / employee_register_employee의 id 숫자는 employee_register_position의 id임 


def lohandsoft_delete(request,id):
    lo = lohandsoft.objects.get(pk=id)
    lo.delete()
    return redirect('/lohandsoft/list')