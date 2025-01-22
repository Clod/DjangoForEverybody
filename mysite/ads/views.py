from django.shortcuts import render, redirect, get_object_or_404, HttpResponse

# Create your views here.

from ads.models import Ad, Comment, Fav
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy, reverse
from ads.forms import CreateForm, CommentForm

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import Q


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    template_name = "ads/ad_list.html"

    # def get(self, request) :
    #     ad_list = Ad.objects.all()
    #     favorites = list()
    #     if request.user.is_authenticated:
    #         # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
    #         rows = request.user.favorite_ads.values('id')
    #         # favorites = [2, 4, ...] using list comprehension
    #         favorites = [ row['id'] for row in rows ]
    #     ctx = {'ad_list' : ad_list, 'favorites': favorites}
    #     return render(request, self.template_name, ctx)
    
    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().distinct().order_by('-updated_at')[:10]

            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval) 
            query.add(Q(text__icontains=strval), Q.OR)
            ad_list = Ad.objects.filter(query).select_related().distinct().order_by('-updated_at')[:10]
        else :
            ad_list = Ad.objects.all().order_by('-updated_at')[:10]

        # Augment the ad_list
        for obj in ad_list:
            # Add a 'natural_updated' attribute to each object containing a friendly representation of the update time
            obj.natural_updated = naturaltime(obj.updated_at)
            
        if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.favorite_ads.values('id')
            # favorites = [2, 4, ...] using list comprehension
            favorites = [ row['id'] for row in rows ]
        else:
            favorites = []

        ctx = {'ad_list' : ad_list, 'search': strval, 'favorites': favorites}
        return render(request, self.template_name, ctx)
    

class AdDetailView(OwnerDetailView):
    model = Ad
    # By convention:
    template_name = "ads/ad_detail.html"
    def get(self, request, pk) :
        x = get_object_or_404(Ad, id=pk)
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ad' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

# class AdCreateView(OwnerCreateView):
#     model = Ad
#     # List the fields to copy from the Article model to the Article form
#     fields = ['title', 'price', 'text']
    
class AdCreateView(LoginRequiredMixin, View):
    """
    View for creating a new advertisement.

    This view requires the user to be logged in. It handles the GET and POST
    requests for creating a new advertisement. The GET request renders the
    form for creating a new ad, while the POST request processes the form data
    and saves the new advertisement if the data is valid.

    Attributes:
        None

    Methods:
        get(self, request, *args, **kwargs): Renders the form for creating a new ad.
        post(self, request, *args, **kwargs): Processes the form data and saves the new ad if valid.
    """
    
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    # The get method is used to display the empty form to be filled by the user
    def get(self, request, pk=None):
        # Define the fields to be displayed in the form
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        ad = form.save(commit=False)
        ad.owner = self.request.user
        ad.save()
        # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
        form.save_m2m()    # Add this
        return redirect(self.success_url)


# class AdUpdateView(OwnerUpdateView):
#     model = Ad
#     fields = ['title', 'price', 'text']

    
class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=ad)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        ad = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=ad)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        ad = form.save(commit=False)
        ad.save()
        # https://django-taggit.readthedocs.io/en/latest/forms.html#commit-false
        form.save_m2m()    # Add this
        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad
    

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=f)
        comment.save()
        return redirect(reverse('ads:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse('ads:ad_detail', args=[ad.id])
    
    
@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Ad, id=pk)
        fav = Fav(user=request.user, ad=t)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Ad, id=pk)
        try:
            Fav.objects.get(user=request.user, ad=t).delete()
        except Fav.DoesNotExist:
            pass

        return HttpResponse()