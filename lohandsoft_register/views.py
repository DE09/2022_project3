from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def search_list(request):
    qs = lohandsoft.objects.all()
    q = request.POST.get('q', '')

    if q:
        qs = qs.filter(fullname__icontains=q)|qs.filter(birth__icontains=q)|qs.filter(email__icontains=q)|qs.filter(age__icontatins=q)

    return render(request, "lohandsoft_register/search_list.html", {
        'searched_qs': qs,
        'q': q,
    })

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


def lohandsoft_login(request):
    if request.method == 'POST': # POST 방식으로 ID랑 PASS를 달고 들어오면
        # print("리퀘스트 로그" + str(request))
        id = request.POST.get('userid','')
        pw = request.POST.get('userpw','')
    
        result = authenticate(fullname=id, birth=pw) # authenticate안에 fullname & birth 파라미터를 넣으면 db랑 비교를해서 맞으면 결과값에 사용자 id를 넣어주고, 아니면 none

        if result :
            print("로그인 성공!")
            return HttpResponse(status=200)
        else:
            print("실패")
            return HttpResponse(status=401)

    return render(request, "lohandsoft_register/lohandsoft_login.html")

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')
