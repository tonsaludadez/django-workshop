from django import forms

class CommentForm(forms.ModelForm):

	class Meta:
		model = CommentForm
		fields = ['project', 'name', 'content']