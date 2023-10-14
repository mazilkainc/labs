# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
pages = 100
lines = 50
symbols = 25
volume_flop= volume * (1024**2)
volueme_book = pages * lines * symbols * 4
print("Количество книг, помещающихся на дискету:", int(volume_flop//volueme_book))