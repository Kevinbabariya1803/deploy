from . import models  
def total(self):
        ids=self.cart.keys()
        products=models.expense.objects.filter(id__in=ids)
        quantites=self.cart
        total=0
        for key,value in quantites.items():
            key = int(key)

            for expense in expense:
                if expense.id == key:
                    total=total+(expense)
            return total