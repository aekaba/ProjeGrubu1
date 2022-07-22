import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

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

# Proje 2, Task 2: Veri setinde outliar var mı ?

print("---Veri setinde outliar var mı ?---")

dataframe=pd.read_csv("NetflixOriginals.csv",encoding='ISO-8859-1')

def grab_col_names(dataframe, cat_th=10, car_th=20):
    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [
        col
        for col in dataframe.columns
        if dataframe[col].nunique() < cat_th and dataframe[col].dtypes != "O"
    ]
    cat_but_car = [
        col
        for col in dataframe.columns
        if dataframe[col].nunique() > car_th and dataframe[col].dtypes == "O"
    ]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(dataframe, cat_th=5, car_th=20)


def outlier_thresholds(dataframe, col_name, q1=0.25, q3=0.75):
    quartile1 = dataframe[col_name].quantile(q1)
    quartile3 = dataframe[col_name].quantile(q3)
    interquantile_range = quartile3 - quartile1
    up_limit = quartile3 + 1.5 * interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit


def check_outlier(dataframe, col_name, q1=0.25, q3=0.75):
    low_limit, up_limit = outlier_thresholds(dataframe, col_name, q1, q3)
    if dataframe[
        (dataframe[col_name] > up_limit) | (dataframe[col_name] < low_limit)
    ].any(axis=None):
        return True
    else:
        return False


for col in num_cols:
    print(col, check_outlier(dataframe, col, 0.1, 0.9))

print(
    "Sonuç: Veri setinde belirlenen uç değerlerle aykırı değer analizi yapan fonksiyonların çıktıları sonucunda herhangi bir aykırı değer gözlemlenmemiştir."
)

#IMDB puanı en yüksek olan ilk 10 film hangileridir?

print("---IMDB puanı en yüksek olan ilk 10 film hangileridir?---")

result=data.sort_values("IMDB Score",ascending=False)
print(result.head(10))

#Uzunmetraj olan filmler

veri = data[data['Runtime'] >=40]
sns.barplot(x=veri.Language.index, y='Language', data=veri)
plt.show()

#'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.

print("---'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.---")

genre_len = data.Genre.nunique()
calculate_genre = data.Genre.value_counts()
fig = px.bar(data_frame=calculate_genre, x=calculate_genre.index, y=calculate_genre.values, labels={"y":"Genre Movies Number", "index":"Genres"})

print(calculate_genre)
fig.show()

#IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.

print("---IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.---")

correlation=data["Runtime"].corr(data["IMDB Score"])
correlation1=data[["IMDB Score", "Runtime"]].corr()
correlation2=data[["Runtime", "IMDB Score"]].corr()


fig = px.scatter(data_frame=data, x="IMDB Score", y="Runtime")
fig.update_layout(autosize=False, width=800, height=600,)

fig.show()