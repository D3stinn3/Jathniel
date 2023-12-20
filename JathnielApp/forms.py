from django import forms
from JathnielApp.models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'mobile', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'text-body-color border-[f0f0f0] focus:border-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'text-body-color border-[f0f0f0] focus:border-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Your Phone', 'class': 'text-body-color border-[f0f0f0] focus:border-primary w-full rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 6, 'class': 'text-body-color border-[f0f0f0] focus:border-primary w-full resize-none rounded border py-3 px-[14px] text-base outline-none focus-visible:shadow-none'}),
        }