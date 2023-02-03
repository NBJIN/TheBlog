# from django import form
from .models import Comment


class Comment(form.ModelForm):
    class Meta:
        model = Commment
        fields = (
        'contributor_comment', 'email', 'date_of_comment', 'image', 'content', 'approved'
        )
#         widgets = {
#             "contributor_comment": froms.TextInput(attrs={
# "class": "col-sm-12"}),
#             "email": froms.TextInput(attrs={"class": "col-sm-12"}),
#             "date_of_comment": froms.TextInput(attrs={"class": "col-sm-12"}),
#             "image": froms.TextInput(attrs={"class": "col-sm-12"}),
#             "content": froms.TextInput(attrs={"class": "col-sm-12"}),
#             "approved": froms.TextInput(attrs={"class": "col-sm-12"}),
#         }
