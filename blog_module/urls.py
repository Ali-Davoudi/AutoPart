from django.urls import path
from blog_module.views import BlogListView, BlogDetailView, SearchBlogView, AddBlogComment

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/category/<category>', BlogListView.as_view(), name='blog_list_by_category'),
    path('blog/tag/<tag>', BlogListView.as_view(), name='blog_list_by_tag'),
    path('blog/<pk>/<name>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/articles', SearchBlogView.as_view(), name='search_blog'),
    path('blog/add-blog-comment', AddBlogComment.as_view(), name='add-blog-comment'),
]
