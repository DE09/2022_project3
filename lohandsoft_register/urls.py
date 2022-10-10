from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.lohandsoft_form,name='lohandsoft_insert'), # get and post req. for insert operation
    path('<int:id>/', views.lohandsoft_form,name='lohandsoft_update'), # get and post req. for update opertion
    path('delete/<int:id>/', views.lohandsoft_delete,name='lohandsoft_delete'),
    path('list/', views.lohandsoft_list,name='lohandsoft_list'), # get req. to retrive and display all records
    path('serach/', views.search_list,name='search_list'),
    path('login/', views.lohandsoft_login,name='lohandsoft_login'),
    path('signup/', views.signup,name='signup'),
]

    #두번째 path: 이게 수정 버튼을 누르면 업데이트 작업을 위해 입력된 정보를 표시하는 주소
    #근데 뒤에 왜 name='employee_update를 하는지 모르겠음
