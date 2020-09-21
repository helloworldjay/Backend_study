from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(Post) # 장식자 문법 : Wrapping 해서 감싼 대상의 기능을 변경할 수 있다.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length','is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img scr="{post.photo.url}" style = "width: 72px;" />') # django는 보안상 그냥 태그 자체를 변환해주지 않는다.
            # 안전하다고 선언해주어야 작동한다.
        return None

    def message_length(self, post): # 매번 post 객체가 넘어온다. 우리가 명시적으로 호출하는 것이 아니라 admin이 알아서 호출해준다. 
        return len(post.message)