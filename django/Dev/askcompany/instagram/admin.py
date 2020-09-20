from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post) # 장식자 문법 : Wrapping 해서 감싼 대상의 기능을 변경할 수 있다.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'message_length','is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

    def message_length(self, post): # 매번 post 객체가 넘어온다. 우리가 명시적으로 호출하는 것이 아니라 admin이 알아서 호출해준다. 
        return len(post.message)