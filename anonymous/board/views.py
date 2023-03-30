from django.shortcuts import render, redirect
from board.models import Post, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
import uuid

def board(request):
  # 게시글 리스트
  if request.method == "GET":
    page = request.GET.get('page',1)
    search_text = request.GET.get('search_text',"")
    post_set = Post.objects.filter(
      title__icontains=search_text).order_by('id')
    paginator = Paginator(post_set, 4)
   
    post_set = paginator.get_page(page)
   
   
    context={
          "post_set":post_set,
          "search_text":search_text,      
             }
   
    return render(request, 'page/index.html', context=context)


@login_required(login_url="signin")
def post_write(request):
  if request.method == 'GET':
    return render(request, "page/post_write.html")
 
  if request.method == 'POST':
    title = request.POST["title"]
    content = request.POST["content"]
    img = request.FILES.get("img", None)
    img_url =""
   
    if img:
      img_name = uuid.uuid4()
      ext = img.name.split(".")[-1]
      default_storage.save(f"{img_name}.{ext}", img)
      img_url = f"{img_name}.{ext}"
   
    Post(
      img_url=img_url,
      user=request.user,
      title=title,
      content=content
    ).save()
    return redirect('board')