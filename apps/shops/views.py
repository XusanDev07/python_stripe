from django.http import HttpResponse


def home_view(request):
    """Simple home page that redirects to admin or shows a basic page"""
    return HttpResponse("""
    <html>
        <head><title>Django Stripe Shop</title></head>
        <body style="font-family: Arial, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px;">
            <h1>Welcome to Django Stripe Shop</h1>
            <p>This is a demo Django + Stripe integration.</p>
            <h2>Available endpoints:</h2>
            <ul>
                <li><a href="/admin/">Admin Panel</a> - Manage items</li>
                <li><code>api/items/item/{id}/</code> - View item and buy</li>
                <li><code>api/items/buy/{id}/</code> - Get Stripe session (API)</li>
            </ul>
            <p><strong>Example:</strong> <a href="/item/1/">View Item #1</a> (if it exists)</p>
        </body>
    </html>
    """)
