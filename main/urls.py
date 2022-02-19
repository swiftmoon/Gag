from django.urls import path
from .views import MainIndex, UploadPost, PostLike, PostCommentView, gag

app_name = "main"
urlpatterns = [
    path('', MainIndex.as_view(), name="index"),
    path('cat/<int:id>/', MainIndex.as_view(), name="cat"),
    path('upload/', UploadPost.as_view(), name="uploadfile"),
    path('post/<str:action>/<int:post_id>/', PostLike.as_view(), name="like"),
    path('comments/<int:post_id>/', PostCommentView.as_view(), name="comments"),
    path('gag/', gag, name="gag")
]
