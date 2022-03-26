from dataclasses import fields
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel

# CreateViewを継承しListClassを定義
# CreateViewの役割 = 
"""
CreateViewとはデータの作成をする際に用いられる汎用view。
例えば、記事や写真を投稿したり、会員登録をしたりするページで使われます。

このような投稿機能や会員登録機能は多くのWebページで実装されているため、
クラスベースビューでのDjango開発ではCreateViewの使用頻度はとても高いです。
(https://kosuke-space.com/django-createview)

①アプリのurls.pyにURLを記述しておき、
②処理を記述し
③読み込みテンプレートをセットする。
"""
class ListClass(ListView) :
    template_name = 'list.html'
    model = PostModel

class FormClass(CreateView):
    template_name = 'form.html'
    # DBに反映するためにモデルもセット
    model = PostModel
    fields = ('title','memo')
    # 投稿完了時の遷移先
    success_url = reverse_lazy('list')
