from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import UserProfile, Feature2
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
import random
import json


def index(request):
    points = None
    if request.user.is_authenticated:
        try:
            points = request.user.feature2.points
        except Feature2.DoesNotExist:
            feature2 = Feature2(user=request.user, points=1000)
            feature2.save()
            points = feature2.points
    return render(request, "index.html", {"points": points})


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            data = Feature2(user=user, points=1000)
            data.save()

            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome {user.username}")
                return redirect("index")
            else:
                messages.error(
                    request,
                    "Authentication failed after registration. Please try logging in.",
                )
                return redirect("login")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = SignUpForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome {user.username}")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")


@login_required
def roulette(request):
    user_feature = Feature2.objects.get(user=request.user)
    red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    black_numbers = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}

    row1_numbers = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    row2_numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    row3_numbers = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    spin_result = None
    win = False
    bet_type = None

    if request.method == "POST":
        bet_amount = request.POST.get("bet_amount")
        bet_type = request.POST.get("bet_type")
        numbers = request.POST.get("numbers")
        dozen_start = request.POST.get("dozen_start")
        column = request.POST.get("column")

        if not bet_amount or not bet_type:
            messages.error(
                request, "Please enter a valid bet amount and select a bet type."
            )
            return redirect("roulette")

        bet_amount = int(bet_amount)

        if bet_amount > user_feature.points:
            messages.error(request, "Insufficient points to place this bet.")
            return redirect("roulette")

        spin_result = random.randint(0, 36)
        payout = 0
        win = False

        def is_adjacent(num1, num2):
            return (
                abs(num1 - num2) == 1
                and (min(num1, num2) - 1) % 3 != 0
                or abs(num1 - num2) == 3
            )

        def is_consecutive(nums):
            return sorted(nums) == list(range(min(nums), max(nums) + 1))

        if bet_type == "column" and column:
            column = int(column)
            if column in [1, 2, 3]:
                column_numbers = []
                if column == 1:
                    column_numbers = row1_numbers
                elif column == 2:
                    column_numbers = row2_numbers
                elif column == 3:
                    column_numbers = row3_numbers
                
                if spin_result in column_numbers:
                    payout = bet_amount * 2
                    win = True
        elif bet_type == "dozen" and dozen_start:
            dozen_start = int(dozen_start)
            if dozen_start in [1, 13, 25]:
                if (
                    (dozen_start == 1 and 1 <= spin_result <= 12)
                    or (dozen_start == 13 and 13 <= spin_result <= 24)
                    or (dozen_start == 25 and 25 <= spin_result <= 36)
                ):
                    payout = bet_amount * 2
                    win = True
                elif bet_type == "low":
                    if 1 <= spin_result <= 18:
                        payout = bet_amount
                        win = True

        elif bet_type == "high":
            if 19 <= spin_result <= 36:
                payout = bet_amount
                win = True

        elif bet_type == "red":
            if spin_result in red_numbers:
                payout = bet_amount
                win = True

        elif bet_type == "black":
            if spin_result in black_numbers:
                payout = bet_amount
                win = True

        elif bet_type == "odd":
            if spin_result % 2 == 1:
                payout = bet_amount
                win = True

        elif bet_type == "even":
            if spin_result % 2 == 0:
                payout = bet_amount
                win = True

        elif bet_type == "single" and numbers:
            selected_number = int(numbers)
            if selected_number == spin_result:
                payout = bet_amount * 35
                win = True

        elif bet_type == "split" and numbers:
            selected_numbers = list(map(int, numbers.split(",")))
            if len(selected_numbers) == 2 and is_adjacent(*selected_numbers):
                if spin_result in selected_numbers:
                    payout = bet_amount * 17
                    win = True

        elif bet_type == "street" and numbers:
            selected_numbers = list(map(int, numbers.split(",")))
            if len(selected_numbers) == 3 and is_consecutive(selected_numbers):
                if spin_result in selected_numbers:
                    payout = bet_amount * 11
                    win = True

        elif bet_type == "corner" and numbers:
            selected_numbers = list(map(int, numbers.split(",")))
            if len(selected_numbers) == 4:
                a, b, c, d = sorted(selected_numbers)
                # Check if the numbers form a valid corner
                if (b == a + 1 and c == a + 3 and d == a + 4) or (
                    b == a + 1 and c == b + 2 and d == a + 3
                ):
                    if spin_result in selected_numbers:
                        payout = bet_amount * 8
                        win = True

        elif bet_type == "line" and numbers:
            selected_numbers = list(map(int, numbers.split(",")))
            if len(selected_numbers) == 6:
                rows = [selected_numbers[:3], selected_numbers[3:]]
                if all(is_consecutive(row) for row in rows) and all(
                    num in row1_numbers or num in row2_numbers or num in row3_numbers
                    for num in selected_numbers
                ):
                    if spin_result in selected_numbers:
                        payout = bet_amount * 5
                        win = True

        if win:
            user_feature.points += payout
            messages.success(
                request,
                f"Hurrah! You win {payout} points. The spin result was {spin_result}.",
            )
        else:
            user_feature.points -= bet_amount
            if user_feature.points < 0:
                user_feature.points = 0
            messages.error(request, f"You lose! The spin result was {spin_result}.")

        user_feature.save()

    return render(
        request,
        "roulette.html",
        {
            "red_numbers": red_numbers,
            "black_numbers": black_numbers,
            "points": user_feature.points,
            "spin_result": spin_result,
            "win": win,
            "bet_type": bet_type,
            "row1_numbers": row1_numbers,
            "row2_numbers": row2_numbers,
            "row3_numbers": row3_numbers,
        },
    )


@login_required
def guess(request):
    feature2 = request.user.feature2
    if request.method == "POST":
        lower_range = int(request.POST.get("lower_range"))
        upper_range = int(request.POST.get("upper_range"))
        number = int(request.POST.get("number"))
        betamt = int(request.POST.get("betamt"))

        if lower_range >= upper_range:
            messages.error(
                request,
                "Lower range must be less than upper range.",
                extra_tags="error-message",
            )
            return redirect("guess")

        if lower_range < 0 or upper_range < 0:
            messages.error(
                request,
                "Range values must be greater than 0.",
                extra_tags="error-message",
            )
            return redirect("guess")

        if betamt > feature2.points:
            messages.error(
                request,
                "Bet amount cannot be greater than available points.",
                extra_tags="error-message",
            )
            return redirect("guess")

        if feature2.points <= 0:
            messages.error(
                request,
                "You do not have enough points to play the game.",
                extra_tags="error-message",
            )
            return redirect("/")

        num = random.randint(lower_range, upper_range - 1)

        if num == number:
            feature2.points += 2 * betamt
            messages.success(
                request,
                f"Hurrah you win! +{2 * betamt} points. Available points: {feature2.points}",
                extra_tags="win-message",
            )
        else:
            feature2.points -= betamt
            messages.error(
                request,
                f"You lose, better luck next time! -{betamt} points. Available points: {feature2.points}",
                extra_tags="lose-message",
            )

        feature2.save()
        return render(
            request, "guess.html", {"points": feature2.points, "home_button": True}
        )
    return render(request, "guess.html", {"points": feature2.points})


@login_required
def seven(request):
    user = request.user
    if not hasattr(user, "feature2"):
        Feature2.objects.create(user=user)

    feature2 = user.feature2

    if request.method == "POST":
        bet_amount = int(request.POST.get("bet_amount", 0))

        return render(
            request,
            "seven.html",
            {
                "message": "",
                "points": feature2.points,
            },
        )
    else:
        return render(
            request,
            "seven.html",
            {
                "message": "",
                "points": feature2.points,
            },
        )


@login_required
def spin(request):
    user = request.user
    if not hasattr(user, "userprofile"):
        UserProfile.objects.create(user=user)
    if not hasattr(user, "feature2"):
        Feature2.objects.create(user=user)

    feature2 = user.feature2

    return render(
        request,
        "spin.html",
        {
            "points": feature2.points,
        },
    )


@csrf_exempt
@login_required
def update_points(request):
    if request.method == "POST":
        data = json.loads(request.body)
        win = data.get("win")
        bet_amount = data.get("betAmount")

        profile, created = Feature2.objects.get_or_create(user=request.user)

        if win:
            profile.points += 2 * bet_amount
            message = "YOU WIN!"
        else:
            profile.points -= bet_amount
            message = "YOU LOSE!"

        profile.save()

        return JsonResponse({"points": profile.points, "message": message})

    return JsonResponse({"error": "Invalid request"}, status=400)


def logout_view(request):
    auth.logout(request)
    return redirect("/")
