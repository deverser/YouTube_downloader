# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from pytube import YouTube

# Получаем ссылку на видео у пользователя
link = input("Вставьте ссылку на видео Youtube:  ")
yt = YouTube(link)

# Выводим информацию о видео
print("Название: ", yt.title)
print("Автор: ", yt.author)
print("Просмотры: ", yt.views)
print("Рейтинг: ", yt.rating)
print("Продолжительность: ", yt.length, "сек\n")

# Выбираем для загрузки поток с максимальным разрешением
ys = yt.streams.get_highest_resolution()

# Загрузка
print("Видео загружается... ")
ys.download('C:/Users/Uzzer/Downloads')
print("Загрузка завершена")
