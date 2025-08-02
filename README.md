# Django Stripe Shop

A Django web application integrated with Stripe payment processing system for handling item purchases.

## 🚀 Features

- **Django Item Model**: Store items with name, description, and price
- **Stripe Integration**: Secure payment processing using Stripe Checkout
- **Admin Panel**: Django admin interface for managing items
- **API Endpoints**: RESTful endpoints for payment processing
- **Responsive UI**: Clean HTML interface with buy functionality
- **Docker Support**: Containerized deployment ready

## 📋 Requirements

- Python 3.8+
- Django 4.2+
- Stripe account (for API keys)

## 🛠️ Installation & Setup

### Method 1: Local Development

1. **Clone the repository**

```bash
git clone https://github.com/XusanDev07/python_stripe.git
cd python_stripe
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Environment setup**

```bash
cp .env.example .env
# Edit .env file with your Stripe keys
```

5**Run the server**

```bash
python manage.py runserver
```

### Method 2: Docker

**Build and run with Docker Compose**

```bash
cp .env.example .env
# Edit .env file with your Stripe keys
docker-compose up --build
```

## 🔑 Stripe Configuration

1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Get your API keys from the Stripe Dashboard
3. Add them to your `.env` file:

```env
STRIPE_PUBLISHABLE_KEY=pk_test_your_publishable_key_here
STRIPE_SECRET_KEY=sk_test_your_secret_key_here
```

## 📚 API Endpoints

- `GET /item/{id}/` - Display item page with buy button
- `GET /buy/{id}/` - Create Stripe checkout session (returns session ID)
- `GET /admin/` - Django admin panel
- `GET /success/` - Payment success page
- `GET /cancel/` - Payment cancelled page

## 🎯 Usage Examples

### View an item and make purchase:

```bash
curl -X GET http://localhost:8000/item/1/
```

### Get Stripe session ID for payment:

```bash
curl -X GET http://localhost:8000/buy/1/
```

Response:

```json
{
  "id": "cs_test_stripe_session_id_here"
}
```

## 👨‍💼 Admin Access

**Default credentials:**

- Username: `admin`
- Password: `admin`
- URL: `http://localhost:8000/admin/`

## 🏗️ Project Structure

```
django-stripe-shop/
├── config/                   # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── items/                  # Django app
│   ├── models.py          # Item model
│   ├── views.py           # API views
│   ├── admin.py           # Admin configuration
│   └── urls.py            # App URLs
├── templates/             # HTML templates
│   ├── base.html
│   ├── home.html
│   └── items/
│       ├── item_detail.html
│       ├── success.html
│       └── cancel.html
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env.example          # Environment variables template
```

## 🧪 Testing

1. **Access the application**: `http://localhost:8000`
2. **Create items** via admin panel: `http://localhost:8000/admin/`
3. **View item page**: `http://localhost:8000/item/1/`
4. **Test purchase flow** using Stripe's test card numbers:
    - Card: `4242 4242 4242 4242`
    - Expiry: Any future date
    - CVC: Any 3 digits
    - ZIP: Any 5 digits

## 🎁 Bonus Features Implemented

- ✅ **Docker support** - Full containerization with docker-compose
- ✅ **Environment variables** - Secure configuration management
- ✅ **Django Admin** - Full admin panel for item management
- ✅ **Production ready** - Ready for deployment with proper settings
- ✅ **Error handling** - Comprehensive error handling and user feedback

## 🔧 Advanced Features (Optional Extensions)

### Multiple Currency Support

```python
# Add to Item model
currency = models.CharField(max_length=3, default='USD', choices=[
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound'),
])
```

### Order Management

```python
# Additional models for orders
class Order(models.Model):
    items = models.ManyToManyField(Item, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    stripe_session_id = models.CharField(max_length=255, blank=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
```

### Discount and Tax Support

```python
class Discount(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_coupon_id = models.CharField(max_length=255)


class Tax(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    stripe_tax_rate_id = models.CharField(max_length=255)
```

## 🐛 Troubleshooting

### Common Issues

1. **Stripe keys not working**
    - Ensure you're using test keys (starting with `pk_test_` and `sk_test_`)
    - Check that keys are properly set in `.env` file

2. **CSRF errors**
    - The `/buy/{id}/` endpoint is GET-based to avoid CSRF issues
    - For POST endpoints, ensure CSRF tokens are included

3. **Database issues**
    - Run `python manage.py migrate` to apply migrations

4. **Static files not loading**
    - Run `python manage.py collectstatic`
    - Ensure `STATIC_ROOT` is properly configured

## 📱 API Response Examples

### Successful purchase session creation:

```json
{
  "id": "cs_test_a1B2c3D4e5F6g7H8i9J0k1L2m3N4o5P6q7R8s9T0"
}
```

### Error response:

```json
{
  "error": "Item not found or Stripe configuration error"
}
```

## 📝 Testing Checklist

- [ ] Items can be created via admin panel
- [ ] Item detail page loads correctly
- [ ] Buy button triggers Stripe checkout
- [ ] Payment success/cancel flows work
- [ ] Admin panel is accessible
- [ ] API endpoints return correct responses
- [ ] Docker containers build and run
- [ ] Environment variables are loaded

## 🆘 Support

For issues and questions:

1. Check the troubleshooting section
2. Review Stripe documentation
3. Create an issue in the repository

---

**Happy coding! 🚀**