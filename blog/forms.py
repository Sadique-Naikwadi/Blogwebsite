from django import forms

class SharePostForm(forms.Form):
    Name = forms.CharField(max_length=25, required=True)
    Email = forms.EmailField(required=True)
    to = forms.EmailField(required=True)
    comment = forms.CharField(required=False, widget=forms.Textarea)


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, obj in self.fields.items():
            obj.widget.attrs['class'] = 'form-control'



    
