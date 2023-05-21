from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from conversation.models import Conversation
from conversation.forms import ConversationMessageForm


@login_required
def new_conversation(request, item_id):
    item = get_object_or_404(Item, id=item_id)

    if item.created_by == request.user:
        return redirect("dashboard:index")

    conversations = Conversation.objects.filter(members__in=[request.user.id])

    if conversations:
        pass

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect("item:show", id=item_id)

    form = ConversationMessageForm()
    return render(request, 'conversation/new.html', {
        "form": form
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    return render(request, "conversation/inbox.html", {
        "conversations": conversations
    })


@login_required
def show(request, conversation_id):
    conversation = Conversation.objects.filter(
        members__in=[request.user.id]).get(id=conversation_id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:show', conversation_id=conversation_id)
    else:
        form = ConversationMessageForm()

    return render(request, "conversation/show.html", {
        "conversation": conversation,
        "form": form
    })
