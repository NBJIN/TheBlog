from django import forms
from .models import Comment 

class Comment(form.ModelForm): 
    class Meta:
        model = Commment
        fields = (
        'contributor_comment', 'email', 'date_of_comment', 'image', 'content', 'approved'
        )
        widgets = 


    @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'contributor_comment', 'email', 'date_of_comment', 'image', 'content', 'approved'
        )
    list_filter = ('approved', 'date_of_comment', 'contributor_comment')
    search_fields = ('contributor_comment', 'email', 'content')

