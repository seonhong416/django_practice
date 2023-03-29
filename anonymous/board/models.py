from django.db import models
from user.models import User

# 글작성
class Post(models.Model) :
    # 일반 게시판 일때는 유저를 FK(foreign key)로 지정
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 제약조건 필수로 들어가야 함
    # 해당 글 작성자(user) 삭제되면, 글도 함께 삭제
    # cf) on_delete = models.SET_NULL, null = True
    title = models.CharField(max_length = 100) # 게시글의 타이틀은 100자 정도로 설정
    content = models.TextField() # content는 text로 채워줘
    reg_date = models.DateTimeField(auto_now_add = True) # 등록일자 (자동으로 날짜 생성 옵션)
    img_url = models.URLField(null=True) # null=True 빈 값이여도 됨
    
    class Meta :
        db_table = 'post'
        # 테이블 이름을 post로 설정
        
# 댓글
class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    
    class Meta :
        db_table = 'comment'

