from django import forms
from .models import Comment

class SharePostForm(forms.Form):
    Name = forms.CharField(max_length=25, required=True)
    Email = forms.EmailField(required=True)
    to = forms.EmailField(required=True)
    comment = forms.CharField(required=False, widget=forms.Textarea)


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, obj in self.fields.items():
            obj.widget.attrs['class'] = 'form-control'



class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, obj in self.fields.items():
            obj.widget.attrs['class'] = 'form-control'
        
    

        
