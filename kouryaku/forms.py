from django.forms import ModelForm
from .models import KouryakuPost
from django import forms

class KouryakuPostForm(ModelForm):#
    class Meta:
        # モデルのクラス
        model = KouryakuPost
        # フォームで使用するモデルのフィールドを指定
        fields = ['category', 'title', 'comment','image1']

class SearchForm(forms.Form):
    query = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={'placeholder': '検索キーワードを入力'}), 
        required=True,  # 入力必須
        error_messages={'required': '検索ワードを入力してください。'}
    )


from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(required=False)