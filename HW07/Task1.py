# 1) Написать программу, где создадим класс Soup (для определения типа супа),
# принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать
# «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»


class Soup:
    def __init__(self, ingredient='ничего'):
        self.ingredient = ingredient

    def __add__(self, other):
        new_ingredient = f'{self.ingredient} и {other.ingredient}'
        return Soup(new_ingredient)

    def __str__(self) -> str:
        return f'Великий суп из: {self.ingredient}'

    def show_my_soup(self):
        if self.ingredient == 'ничего':
            return 'Обычный кипяток'
        else:
            return f'Суп - {self.ingredient}'


#  Примеры:


a = Soup()
b = Soup('мясо')
c = a + b
print(a)
print(b)
print(c)
print(a.show_my_soup())
print(b.show_my_soup())
