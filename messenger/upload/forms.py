from django import forms
from django.core.exceptions import ValidationError
from upload.models import UploadModel
import magic

class UploadFileForm(forms.ModelForm):
	class Meta:
		model = UploadModel
		fields = ['data']