import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Item

# Set Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


@require_http_methods(["GET"])
def item_detail(request, item_id):
    """
    GET /item/{id} - Return HTML page with item info and Buy button
    """
    item = get_object_or_404(Item, id=item_id)

    context = {
        'item': item,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    }

    return render(request, 'items/item-detail.html', context)


@require_http_methods(["GET"])
def create_checkout_session(request, item_id):
    """
    GET /buy/{id} - Create Stripe checkout session and return session ID
    """
    item = get_object_or_404(Item, id=item_id)

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': item.get_price_in_cents(),
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri(f'/item/{item.id}/'),
        )

        return JsonResponse({
            'id': checkout_session.id
        })

    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=400)


def success_view(request):
    """Success page after payment"""
    return render(request, 'items/success.html')


def cancel_view(request):
    """Cancel page if payment is cancelled"""
    return render(request, 'items/cancel.html')
