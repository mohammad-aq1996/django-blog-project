from django.shortcuts import render
from .models import Comment, Contact
from .forms import CommentForm


def contact_view(request):
    """
    return the contact information which is the first element of Contact table
    receiving the comment of visitors
    """
    contact = Contact.objects.get(id=1)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            comment = Comment(name=name, subject=subject, email=email, message=message)
            comment.save()

    context = {
        'contact': contact
    }
    return render(request, 'contact_us/../templates/contact_us/contact.html', context)