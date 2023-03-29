from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# 필수!!
# 커스텀 유저(custom user) 생성시, settings에 사용 유저 모델 정의

# AbstractUser
# django 기본 유저 모델 (기본적으로 필요한 거의 모든 모듈 내장)
# cf) AbstractBaseUser : 최소 유저 모델(필드:비밀번호, 마지막 로그인, 활성화 여부 3가지만 존재,
#                        최소한의 함수만 존재) >> 많은 부분을 커스텀 할 수 있음
class User(AbstractUser) :
    nickname = models.CharField(max_length=30, null = True)
    # nickname은 character field로 30글자로 제한을 줌 빈칸 가능
    class Meta :
        db_table = 'user'
        # table 이름을 user로 만들거야