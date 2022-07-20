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

print("\n\nEn Çok Runtime a sahip yıllar:")

print(mostRuntime.head(1))

# Hangi Yılda Çok film yayınlanmıştır görselleştiriniz

print("---Hangi Yılda Çok film yayınlanmıştır görselleştiriniz---")
yearCount=data.groupby("Year").count().reset_index()

yearCount=pd.DataFrame(yearCount)

ax.bar(yearCount.Year,yearCount.Title, width=1, edgecolor="white", linewidth=1)

plt.show()

# Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.

languageAvg=data.groupby("Language")["IMDB Score"].mean()
languageAvg=pd.DataFrame(languageAvg)
languageAvg=languageAvg.sort_values(by="IMDB Score").reset_index()
languageAvg=languageAvg.head(10)
fig, ax = plt.subplots()

ax.bar(languageAvg.Language,languageAvg["IMDB Score"] , width=1, edgecolor="white", linewidth=1)
ax.set_ylim([0, 10])
plt.gcf().autofmt_xdate()
plt.show()