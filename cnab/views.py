from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from utils.utils import (
    convert_from_cnab,
    convert_utf,
    add_to_database,
    get_list_of_shops_and_total,
)
from .models import Transaction
from .forms import UploadFileForm
import magic
import ipdb


def render_form_view(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES["file"]

        filetype = magic.from_buffer(file.read())
        if not "text" in filetype:
            raise ValidationError("File extension is not .txt")

        decoded = convert_utf(file)

        transactions = convert_from_cnab(decoded)

        add_to_database(transactions)

        return redirect(to="transactions/")
    else:
        form = UploadFileForm()
        return render(request, "cnab/form.html", {"form": form})


#


def render_transactions_view(request):
    all_transactions = Transaction.objects.all()

    shop_list = get_list_of_shops_and_total()

    context = {"shop_list": shop_list, "transactions": all_transactions}

    return render(request, "cnab/shop_list.html", context)


# Testes
# Heroku
