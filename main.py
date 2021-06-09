# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from pytube import YouTube

# Получаем ссылку на видео у пользователя
link = input("Вставьте ссылку на видео Youtube:  ")
yt = YouTube(link)

