from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
urlpatterns = [
   # path('', PollList.as_view(), name='polls_list'),
   # path('<int:pk>', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choices',  ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote',  CreateVote.as_view(), name="create_vote"),
    path("polls/users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    #path("login/", views.obtain_auth_token, name="login"),
]
urlpatterns += router.urls