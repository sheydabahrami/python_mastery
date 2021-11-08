
#for intra packages reference there are two ways to import a package.
# Relative and Absolut

# Supposing we were working on our "eshopping.py" and need to import a function from "contact.py"

from ecommerce.costumer import contact # This is the absolute import

contact.contact_costumer()



from ..costumer import contact # We use the "." operator to navigate to the parent folders. This is the relative method

contact.contact_costumer()

# As a best practice prefer to use the absolute import. Thats waht PEP 8 recommends.