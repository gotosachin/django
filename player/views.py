from django.shortcuts import render, redirect, get_object_or_404
from gameplay.models import Game
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .forms import InvitationForm
from .models import Invitation


# Create your views here.
@login_required
def home(request):
    myGames = Game.objects.gamesForUser(request.user)
    active_games = myGames.active()
    finished_games = myGames.difference(active_games)

    #allMyGames = myGames.active()

    # get logdedin user invitations received from other user
    invitations = request.user.invitations_recieved.all()

    return render(request, 'player/home.html', {'invitations':invitations, 'active_games': active_games, 'finished_games': finished_games})


@login_required
def new_invitation(request):
    if request.method == 'POST':
        invitation = Invitation(from_user = request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_home')
    else:
        form = InvitationForm()

    return render(request, 'player/new_invitation_form.html', {"form": form})

@login_required
def accept_invitation(request, id):
    invitation = get_object_or_404(Invitation, pk=id)
    if not request.user == invitation.to_user:
        raise PermissionDenied

    if request.method == "POST":
        if "accept" in request.POST:
            game = Game.objects.create(first_player = invitation.to_user, second_player=invitation.from_user,)
        invitation.delete()
        # return redirect('player_home')
        return redirect(game)
    else:
        return render(request, 'player/accept_invitation_form.html', {"invitation":invitation})

def profile(request):
    return True;