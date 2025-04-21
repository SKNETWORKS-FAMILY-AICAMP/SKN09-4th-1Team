import uuid
from django.db import models

# 사용자 정보 
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# 사용자 추가 정보
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # 혼인 정보
    marital_skipped = models.BooleanField(default=False)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    marriage_duration = models.CharField(max_length=50, blank=True, null=True)
    divorce_status = models.CharField(max_length=50, blank=True, null=True)

    # 자녀 정보
    children_skipped = models.BooleanField(default=False)
    has_children = models.BooleanField(blank=True, null=True)
    children_ages = models.TextField(blank=True, null=True)

    # 기타 정보
    other_skipped = models.BooleanField(default=False)
    property_range = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=100, blank=True, null=True)

    # 상세 고민
    detail_skipped = models.BooleanField(default=False)
    detail_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"UserInfo of {self.user.email}"