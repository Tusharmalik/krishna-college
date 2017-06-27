from django.contrib import admin
from .models import NoticeBoard, SlideShow, Event, Highlight

# class NoticeBoardAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 		(None, {'fields': ['title']}),
# 	]
# 	list_display = ('title', 'pub_date')
# 	list_filter = ['pub_date', 'title']
# 	search_fields = ['title']


admin.site.register(NoticeBoard)
admin.site.register(SlideShow)
admin.site.register(Event)
admin.site.register(Highlight)