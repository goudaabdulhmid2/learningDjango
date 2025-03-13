from django.db import models

# migration mean put this class in django files => python manage.py makemigrations
# This is like drawing a plan to build or update your shelves based on your blueprint (the Product class).
# When you change the Product class (e.g., add a new field like image or change max_length), you run python manage.py makemigrations. Django looks at your changes, creates a set of instructions (saved in special files), and says, “Okay, here’s how we’ll update the shelves.”
# These instructions are stored in a folder called migrations inside your app, but you don’t need to worry about the details—they’re just the plan!

# migrate mean put in db => python manage.py migrate
# This is like actually building the shelves or making changes to them based on the plan.
# When you run python manage.py migrate, Django takes the instructions from makemigrations and updates your database (the shelves) to match your Product blueprint. This creates tables in the database where your products will be stored.
# After this, you can start adding products (data) to those shelves using your Django app!
# Simple Analogy: Think of makemigrations as writing a to-do list for building furniture, and migrate as assembling the furniture based on that list. You need both steps to get your store ready!

# Create your models here.
class Product(models.Model):

    # It’s not creating a new product; it’s just adding details about how to display or manage the Product class.
    # Simple Analogy: Imagine Product is a recipe for a cake, and Meta is a note on the recipe card saying, “Call this cake ‘Chocolate Delight’ and serve it alphabetically by flavor.” It’s extra info to make the recipe (class) work better!
    # Class Inside Class (Meta): This is a Python feature called a nested class. It’s not unique to Django but is commonly used in Django models to provide metadata. In other Python code, you might see nested classes for other purposes (e.g., organizing related functionality), but in Django, Meta is the standard way to add model options.
    
    class Meta:
    # verbose_name = 'product'
        ordering = ['-name','price']

    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y%m%d')
    actaive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name 
    

  