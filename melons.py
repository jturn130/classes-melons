"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

        def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost




# w = WatermelonOrder()
# w.get_price(3)
# # w.get_price()


class CantaloupeOrder(object):
    #  species, color, imported, shape, seasons are class attributes of CantaloupeOrder
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost

# c = CantaloupeOrder()
# c.get_price(5)

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ['Winter', 'Spring']

    def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter"]

    def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ['Summer']

    def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring","Summer"]

    def get_price(self, qty):
    # """Determine price for this quantity of melons of this type.

    # Return a float of the total price.
    # """

        base_cost = 5.00

        print base_cost
        if self.species == "Casaba" or self.species == "Ogen":
            base_cost += 1

        if self.imported == True:
            base_cost *= 1.5

        if self.shape == "square":
            base_cost *= 2

        total_cost = base_cost * qty
        print total_cost

        if self.species == 'Watermelon' and qty >= 3:
            total_cost *= .75

        if self.species == "Cantaloupe" and qty >= 5:
            total_cost *= .5

        print total_cost


