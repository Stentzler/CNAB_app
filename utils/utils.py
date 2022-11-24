from cnab.models import Transaction
from cnab.serializers import TransactionSerializer
from django.core.exceptions import ValidationError
import re


def convert_from_cnab(transactions):
    new_transactions = []

    for transaction in transactions:
        new_transaction = {
            "tipo": transaction[0:1],
            "data": f"{transaction[1:5]}-{transaction[5:7]}-{transaction[7:9]}",
            "valor": round(int(transaction[9:19]) / 100, 2),
            "cpf": transaction[19:30],
            "cartao": transaction[30:42],
            "hora": f"{transaction[42:44]}:{transaction[44:46]}:{transaction[46:48]}",
            "dono_da_loja": transaction[48:62].strip(),
            "nome_da_loja": transaction[62:82].strip(),
        }

        new_transactions.append(new_transaction)

    return new_transactions


#


def convert_utf(file):
    read_line = file.readlines()
    decoded_list = []

    result = [line.decode("utf-8") for line in read_line]
    result = [re.sub(r"\r\n", "", line) for line in result]

    for item in result:
        if len(item) != 80:
            raise ValidationError(
                "Certifique-se que o arquivo .txt contém apenas padrões CNAB separados por quebra de linha"
            )

        decoded_list.append(item)
    return decoded_list


#


def add_to_database(transactions_list):
    for transaction in transactions_list:
        serializer = TransactionSerializer(data=transaction)
        serializer.is_valid()

        Transaction.objects.create(**serializer.data)


#


def get_list_of_shops_and_total():
    transactions = Transaction.objects.all()

    shop_list = [transaction.nome_da_loja for transaction in transactions]
    shop_list = list(dict.fromkeys(shop_list))

    shop_arr = []

    for shop in shop_list:
        total = 0
        for transaction in transactions:
            if transaction.nome_da_loja == shop:
                if (
                    transaction.tipo == "2"
                    or transaction.tipo == "3"
                    or transaction.tipo == "9"
                ):
                    total -= float(transaction.valor)
                else:
                    total += float(transaction.valor)
        total = round(total, 2)
        obj = [shop, total]
        shop_arr.append(obj)

    return shop_arr
