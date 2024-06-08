from django.urls import path,include
from index.views import PostView,PublicPostView
urlpatterns = [
    path('blog/', PostView.as_view()),
    path('', PublicPostView.as_view()),
]