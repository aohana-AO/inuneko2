from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル', widget=forms.Textarea(attrs={'cols': '100', 'rows': '2'}))
    content = forms.CharField(label='内容', widget=forms.Textarea(attrs={'cols': '140', 'rows': '6'}))
    image = forms.ImageField(label='イメージ画像', required=False)
    category = forms.fields.ChoiceField(

        choices=(
            ('雑記', '雑記'),
            ('皮膚・毛並み', '皮膚・毛並み'),
            ('眼', '眼'),
            ('消化器官', '消化器官'),
            ('口', '口'),
            ('耳', '耳'),
            ('食事', '食事'),
            ('認知・行動', '認知・行動'),

        ),
        label='カテゴリー',
        required=True,
        widget=forms.widgets.Select
    )

