import requests

res = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita')
res
data = res.json()
data

class Cocktails:
    def __init__(self, name, ingredients, instructions, glass_type):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.glass_type = glass_type

    def __str__(self):
        output = f"-----{self.name}-----\n"
        output += f"Glass type: {self.glass_type}\n"
        output += f"ingredients: \n"
        for ingredient in self.ingredients:
            output += f"\t {ingredient}\n"
        output += f"Instructions: \n"
        output += self.instructions
        return output

    def __repr__(self):
        return f"<Cocktail | {self.name}>"

class CocktailAPI:
    def __init__(self,key):
        self.base_url = "http://www.thecocktaildb.com/api/json/v1"
        self.api_key = key
    def _get(self,q=''):
        res = requests.get(f"{self.base_url}/{self.api_key}/search.php?s={q}")
        if res.ok:
            return res.json()
        else:
            return "invalid search. Please try again"
    def get_cocktail(self, drink_name):
        data = self._get(drink_name)
        if data and data['drinks']:
            drink = data['drinks'][0]
            drink_name = drink['strDrink']
            instructions = drink['strInstructions']
            ingredients = []
            for i in range(1,16):
                if drink[f"strIngredient{i}"]:
                    ingredients.append(f'{drink[f"strIngredient{i}"]} - {drink[f"strMeasure{i}"]}')
            glass_type = drink['strGlass']
            new_cocktail = Cocktails(drink_name, ingredients, instructions, glass_type)
            return new_cocktail
        else:
            return f"{drink_name.title()} is not a real drink. Go home. You're drunk!"

cocktail = CocktailAPI(1)
new = cocktail.get_cocktail('margarita')
print(new)