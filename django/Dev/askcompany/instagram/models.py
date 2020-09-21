from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to = 'instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    # def message_length(self): # 인자 없는 속성(함수)만 가능
    #     return len(self.message)
    # message_length.short_description = "메세지 글자수"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 여기서 다른 앱의 model을 가져다 쓸 때에 상단에 import로 다른 앱의 모델을 불러올수도 있지만
    # 그냥 여기에서 Post대신에 'blog1.Post'로 써주는 것도 가능하다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

