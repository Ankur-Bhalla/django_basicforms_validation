# Declare a class with fields name, email, text and botcacher for run1, run2 and run3
# Declare a class with fields name, email, verify_email and text for run4
# Run 1 - Check for bot without using in-built validators, use clean_ method inside form class.
#         Define our own error message.
# Run 2 - Check for bot using in-built validators, use validators parameter for field botcatcher.
#         This will throw in-built error message.
# Run 3 - Check for empty fields using our own custom validation function. Check for name field which start
#         with "z" and if not raise our own error.
# Run 4 - Clean entire form all at once. One method clean the entire fields of the form using super().clean() method.
#         Verify email again and raise our own error if email does not match again.


from django import forms
from django.core import validators


# Run 1 - bot check without using in-built validators
# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
#                                 # set required field to False to see this field on back of html
#                                 # using Inspect page
#                                 # hide botcatcher field from typical human using HiddenInput
#     def clean_botcatcher(self):
#         botcatcher = self.cleaned_data['botcatcher']
#         if len(botcatcher) > 0:
#             raise forms.ValidationError("GOTCHA BOT!")
#         return botcatcher

# Run 2 - bot check using in-built validators
# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,  # hide this field from typical human
#                                  validators=[
#                                      validators.MaxLengthValidator(0)])  # bot check using in-built validators

# Run 3 - our own custom validation function
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")
# #
# class FormName(forms.Form):
#     name = forms.CharField(validators=[check_for_z])
#     email = forms.EmailField()
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,
#                                  widget=forms.HiddenInput,  # hide this field from typical human
#                                  validators=[
#                                      validators.MaxLengthValidator(0)])  # bot check using in-built validators


# Run 4 Clean entire form all at once. One method clean the entire fields of the form using clean() method.
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()  # this super().clean() method will clean the entire form fields
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
