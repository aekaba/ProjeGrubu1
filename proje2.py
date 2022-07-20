import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("NetflixOriginals.csv",encoding='ISO-8859-1')

data[["Date","Year"]] =data['Premiere'].str.split(", ",expand=True)

fig, ax = plt.subplots()


# Hangi yılın toplam "runtime" süresi en fazladır?

print("---Hangi yılın runtime süresi en fazladır---") 
yearSum=data.groupby("Year")["Runtime"].sum().reset_index()

yearSum=pd.DataFrame(yearSum)
mostRuntime=yearSum.sort_values("Runtime",ascending=False)

print(mostRuntime.head(1))

# Hangi Yılda Çok film yayınlanmıştır görselleştiriniz

print("---Hangi Yılda Çok film yayınlanmıştır görselleştiriniz---")
yearCount=data.groupby("Year").count().reset_index()

yearCount=pd.DataFrame(yearCount)

ax.bar(yearCount.Year,yearCount.Title, width=1, edgecolor="white", linewidth=1)
fig.canvas.manager.set_window_title('Hangi Yılda Çok film yayınlanmıştır')
plt.show()

# Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.

print("---Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.---")

languageAvg=data.groupby("Language")["IMDB Score"].mean()
languageAvg=pd.DataFrame(languageAvg)
languageAvg=languageAvg.sort_values(by="IMDB Score").reset_index()
languageAvg=languageAvg.head(10)
fig, ax = plt.subplots()

ax.bar(languageAvg.Language,languageAvg["IMDB Score"] , width=1, edgecolor="white", linewidth=1)
ax.set_ylim([0, 10])
fig.canvas.manager.set_window_title('Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir')
plt.gcf().autofmt_xdate()
plt.show()

# Her bir dilin en fazla kullanıldığı "Genre" nedir?

print("---Her bir dilin en fazla kullanıldığı Genre nedir?---")
result = data.groupby(["Language"])["Genre"].value_counts(sort=True).groupby(level=0)
print(result.head(1))

# İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?

print("---İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?---")

engData = data[data['Language'] == 'English']
engData=engData.groupby('Genre')['IMDB Score'].mean().sort_values(ascending=False).reset_index()

print(engData.head(1))

# 'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?

print("---'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?---")

hindiData = data[data['Language'] == 'Hindi']
hindiAvg = hindiData['Runtime'].mean()
print(hindiAvg)

# Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.

calculate_language=data.groupby('Language').size().sort_values(ascending=False)
print("En çok kullanılan 3 dil "+str(+calculate_language[:3]))