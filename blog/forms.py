from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Post

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
        
    

class CustomAuthenticationForm(AuthenticationForm):

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, obj in self.fields.items():
            obj.widget.attrs['class'] = 'form-control'
        

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, obj in self.fields.items():
            obj.widget.attrs['class'] = 'form-control'
        
    

class AddPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key, obj in self.fields.items():
            obj.widget.attrs['class'] = 'form-control'
        
    

       
          
