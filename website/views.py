from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required

from .models import Posting, Reply
from .forms import PostingForm, ReplyForm

@login_required
@require_http_methods(['GET', 'POST'])
def posting_create(request):
    if request.method == 'POST':
        form = PostingForm(request.POST)
        if form.is_valid():
            posting = form.save(commit=False)
            posting.user = request.user
            posting.save()
            return redirect('website:posting_detail', posting.pk)
    else:
        form = PostingForm()
    return render(request, 'website/form.html', {
        'form': form,
    })
    
@require_safe    
def posting_index(request):
    postings = Posting.objects.all().order_by('-created_at')
    return render(request, 'website/index.html', {
        'postings': postings,
    })

@require_safe
def posting_detail(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    replies = posting.replies.all()
    replyform = ReplyForm()
    return render(request, 'website/detail.html', {
        'posting': posting,
        'replies': replies,
        'replyform': replyform,

    })

@login_required
@require_http_methods(['GET', 'POST'])
def posting_update(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)

    if  request.user != posting.user:
        return redirect('website:posting_index')
    
    if request.method == 'POST':
        form = PostingForm(request.POST, instance=posting)
        if form.is_valid():
            posting = form.save()
            return redirect('website:posting_detail', posting.pk)
    else:
        form = PostingForm(instance=posting)
    return render(request, 'website/form.html', {
            'form': form,
        })


@login_required
@require_POST
def posting_delete(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    posting.delete()
    return redirect('website:posting_index')


@login_required
@require_POST
def reply_create(request, posting_pk):
    posting = get_object_or_404(Posting, pk=posting_pk)
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.posting = posting
        reply.user = request.user
        reply.save()
        return redirect('website:posting_detail', posting.pk)

