from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
#서비스쪽 함수, sql용어사용, insert
def  insert_user(username:str, password:str, email:str) -> None:
    CustomUser.objects.create_user(
        name=username,
        password=password,
        email=email
    )
#한 개 선택 -> get, 여러개 -> select
def get_user(
    username:str, password:str) -> CustomUser:
    if not CustomUser.objects.filter(name=username).exists():
        raise ValueError(f"{username}은 존재하지 않는 사용자 아이디입니다.")
    is_user = authenticate(username=username, password=password)
    if not is_user:
        raise ValueError("비밀번호가 올바르지 않습니다.")
    return is_user
