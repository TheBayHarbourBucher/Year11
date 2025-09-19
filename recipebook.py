class Ingredient:#make ingredient class
    def __init__(self, name, quantity, unit):  # giving it properties
        self.name = name
        self.quantity = quantity
        self.unit = unit

class Recipe:#recipes class
    def __init__(self, recipe_id, title, category, ingredients, instructions):
        self.recipe_id = recipe_id
        self.title = title
        self.category = category
        self.ingredients = ingredients  # list of Ingredient objects
        self.instructions = instructions

class MealPlan:  # connects recipes to other attributes
    def __init__(self, recipe, day):
        self.recipe = recipe
        self.day = day

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe_id, title, category, ingredients, instructions):
        if recipe_id in self.recipes:
            raise ValueError("already exists")
        self.recipes[recipe_id] = Recipe(recipe_id, title, category, ingredients, instructions)

    def remove_recipe(self, recipe_id):
        if recipe_id in self.recipes:
            del self.recipes[recipe_id]
        else:
            raise ValueError("already exists")

    def search_by_id(self, recipe_id):
        return self.recipes.get(recipe_id, None)

    def search_by_category(self, category):
        return [r for r in self.recipes.values() if r.category.lower() == category.lower()]

    def search_by_ingredient(self, ingredient_name):
        found = []
        for recipe in self.recipes.values():
            for ing in recipe.ingredients:
                if ing.name.lower() == ingredient_name.lower():
                    found.append(recipe)
                    break
        return found

class ShoppingListManager:
    def __init__(self):
        self.ingredients = {}

    def add_recipe(self, recipe):
        for ing in recipe.ingredients:
            list = ing.name.lower()
            if list in self.ingredients:
                self.ingredients[list].quantity += ing.quantity
            else:
                self.ingredients[list] = Ingredient(ing.name, ing.quantity, ing.unit)

    def remove_ingredient(self, name):
        key = name.lower()
        if key in self.ingredients:
            del self.ingredients[key]
        else:
            raise ValueError("what your looking for in unavailable.")

    def clear_list(self):
        self.ingredients = {}

    def get_list(self):
        return list(self.ingredients.values())

class MealPlanner:
    def __init__(self):
        self.meal_plans = []

    def add_meal(self, recipe, day):
        self.meal_plans.append(MealPlan(recipe, day))

    def remove_meal_by_day(self, day):
        self.meal_plans = [mp for mp in self.meal_plans if mp.day.lower() != day.lower()]

    def get_meals_by_day(self, day):
        return [mp.recipe for mp in self.meal_plans if mp.day.lower() == day.lower()]

    def clear_plan(self):
        self.meal_plans = []


class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

class Recipe:
    def __init__(self, recipe_id, title, category, ingredients, instructions):
        self.recipe_id = recipe_id
        self.title = title
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions

class MealPlan:
    def __init__(self, recipe, day):
        self.recipe = recipe
        self.day = day

class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe_id, title, category, ingredients, instructions):
        if recipe_id in self.recipes:
            raise ValueError("Recipe ID already exists.")
        self.recipes[recipe_id] = Recipe(recipe_id, title, category, ingredients, instructions)

    def remove_recipe(self, recipe_id):
        if recipe_id in self.recipes:
            del self.recipes[recipe_id]
        else:
            raise ValueError("Recipe ID not found.")

    def search_by_id(self, recipe_id):
        return self.recipes.get(recipe_id, None)

    def search_by_category(self, category):
        return [r for r in self.recipes.values() if r.category.lower() == category.lower()]

    def search_by_ingredient(self, ingredient_name):
        found = []
        for recipe in self.recipes.values():
            for ing in recipe.ingredients:
                if ing.name.lower() == ingredient_name.lower():
                    found.append(recipe)
                    break
        return found

class ShoppingListManager:
    def __init__(self):
        self.ingredients = {}

    def add_recipe(self, recipe):
        for ing in recipe.ingredients:
            key = ing.name.lower()
            if key in self.ingredients:
                self.ingredients[key].quantity += ing.quantity
            else:
                self.ingredients[key] = Ingredient(ing.name, ing.quantity, ing.unit)

    def remove_ingredient(self, name):
        key = name.lower()
        if key in self.ingredients:
            del self.ingredients[key]
        else:
            raise ValueError("not found on the list.")



    def get_list(self):
        return list(self.ingredients.values())

class MealPlanner:
    def __init__(self):
        self.meal_plans = []

    def add_meal(self, recipe, day):
        self.meal_plans.append(MealPlan(recipe, day))

    def remove_meal_by_day(self, day):
        self.meal_plans = [mp for mp in self.meal_plans if mp.day.lower() != day.lower()]

    def get_meals_by_day(self, day):
        return [mp.recipe for mp in self.meal_plans if mp.day.lower() == day.lower()]

    def clear_plan(self):
        self.meal_plans = []
#code end