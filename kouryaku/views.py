from django.shortcuts import render,redirect
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import KouryakuPostForm #
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Category, KouryakuPost
from django.views.generic import DetailView
from django.views.generic import DeleteView
from .forms import SearchForm
class IndexView(TemplateView):
    template_name = 'index.html'
# デコレーターにより、CreateKouryakuViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateKouryakuView(CreateView):
    form_class = KouryakuPostForm
    template_name = "post_Kouryaku.html"
    
    # データベースへの登録完了後のリダイレクト先
    success_url = reverse_lazy('kouryaku:post_done')

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        return super().form_valid(form)
class PostSuccessView(TemplateView):
    template_name ='post_success.html'
class IndexView(ListView):
    template_name ='index.html'
    
    # モデルKouryakuPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    queryset = KouryakuPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 9
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Categoryモデルから全てのカテゴリを取得してcontextに追加
        context['categories'] = Category.objects.all()
        return context


class CategoryView(ListView):
    template_name = "index.html"
    paginate_by = 9

    def get_queryset(self):
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs["category"]
        # filter(フィールド名=id)で絞り込む
        categories = KouryakuPost.objects.filter(category=category_id).order_by(
            "-posted_at"
        )
        return categories

class UserView(ListView):
    template_name = "index.html"
    paginate_by = 9

    def get_queryset(self):
        # self.kwargsでキーワードの辞書を取得し、
        # userキーの値(ユーザーテーブルのid)を取得
        user_id = self.kwargs["user"]
        # filter(フィールド名=id)で絞り込む
        user_list = KouryakuPost.objects.filter(user=user_id).order_by("-posted_at")
        return user_list
class DetailView(DetailView):
    template_name ='detail.html'
    model = KouryakuPost
class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = KouryakuPost.objects.filter(
            user = self.request.user).order_by('-posted_at')
        return queryset
class KouryakuDeleteView(DeleteView):
    model = KouryakuPost
    template_name = 'kouryaku_delete.html'
    success_url = reverse_lazy('kouryaku:mypage')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Create your views here.

# views.py
def search(request):
    form = SearchForm(request.GET)  # GETリクエストを使ってフォームを初期化
    posts = KouryakuPost.objects.all()  # 全ての投稿を取得
    if form.is_valid():  # フォームが有効であれば
        query = form.cleaned_data['query']  # 入力された検索キーワードを取得
        print(f"検索クエリ: {query}")  # デバッグ用にクエリを表示
        posts = posts.filter(title__icontains=query)  # タイトルに部分一致する投稿をフィルタリング
        print(f"検索結果件数: {posts.count()}")  # 結果件数を表示
    else:
        # 検索ワードが入力されていない場合、リダイレクトする
        if 'query' not in request.GET or not request.GET['query'].strip():
            return redirect('kouryaku:index')  # 例: indexページにリダイレクト
        return render(request, 'search.html', {'form': form, 'posts': posts})

    return render(request, 'search.html', {'form': form, 'posts': posts})


