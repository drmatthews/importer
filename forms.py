from django import forms
from django.forms import DateTimeField, DateTimeInput, EmailField, \
						 CharField, TextInput, Textarea, ChoiceField,\
						 Select, FileField
import datetime

class GroupForm(forms.Form):  
	def __init__(self, groups=None, *args, **kwargs):
		super(GroupForm, self).__init__(*args, **kwargs)
		self.fields['group'].choices = groups

	group = ChoiceField(required=True,choices=())			

class ProjectForm(forms.Form):  
	def __init__(self, projects=None, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.fields['project'].choices = projects

	project = ChoiceField(required=True,choices=())

class DatasetForm(forms.Form):  
	def __init__(self, datasets=None, *args, **kwargs):
		super(DatasetForm, self).__init__(*args, **kwargs)
		self.fields['dataset'].choices = datasets

	dataset = ChoiceField(required=True,choices=())

class UploadForm(forms.Form):  	
	date = DateTimeField(initial=datetime.date.today,required=True,\
		widget=DateTimeInput(attrs={'style': 'display:none;'}))
	email = EmailField(widget=TextInput(attrs={'placeholder':'Email'}),required=True)
	file = FileField() 

	def save(self, temp_file, uploaded_file):  
		print 'File "%s" would presumably be saved to disk now.' % uploaded_file  
		pass
       
class FeedbackForm(forms.Form):
	name = CharField(initial='Your name',required=True)
	email = EmailField(required=True)
	comment = CharField(widget=Textarea,required=True)
      
