from django.core.mail import send_mail


def send_confirmation_email(email, code, title, cost):
    full_link = f'Привет подверди заказ на продукт {title}, на сумму {cost} http://localhost:8000/api/v1/order/confirm/{code}/'

    send_mail(
        f'Order from Internet shop',
        full_link,
        'rafievvvv@gmail.com',
        ['rafievvvv@gmail.com']
    )