from bs4 import BeautifulSoup

s7 = open('s7-2.htm', encoding='UTF-8')
soup = BeautifulSoup(s7, "html.parser")
otziv = soup.find_all("span", class_="business-review-view__body-text")
print(f'Анализ отзывов S7 в аэропорту Домодедово на Яндекс Картах:\n')
print(f'Количество отзывов от 1 до 3 звёзд за последние 5 лет - {len(otziv)}')
bagazh = []
for a in otziv:
    if "багаж" in str(a).lower():
        bagazh.append(str(a))

print(f'Количество отзывов, в которых упоминается слово багаж - {len(bagazh)}\n')
print("Фрагменты отзывов:")
i = 1
for b in bagazh:
    x = b.find("багаж")
    print(f'{i}. ...{b[x-20:x+20]}...')
    i += 1