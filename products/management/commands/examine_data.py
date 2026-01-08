from django.core.management.base import BaseCommand
from products.models import Category, Product

class Command(BaseCommand):
    help = 'Examine current categories and products with custom patterns'

    def handle(self, *args, **options):
        self.stdout.write('=== CATEGORIES ===')
        categories = Category.objects.all()
        for category in categories:
            self.stdout.write(f'  {category.name}')
        
        self.stdout.write('\n=== PRODUCTS WITH CUSTOM PATTERNS ===')
        custom_products = Product.objects.filter(pattern='custom')
        for product in custom_products:
            self.stdout.write(f'  {product.name} - {product.custom_pattern}')
        
        self.stdout.write(f'\nTotal categories: {categories.count()}')
        self.stdout.write(f'Total products with custom patterns: {custom_products.count()}')
