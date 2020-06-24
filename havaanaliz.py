import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_excel("veriseti.xlsx")

data['PM10'] = data['PM10'].astype('float')
data['DefaultPM10'] = data['DefaultPM10'].astype('float')
data['SO2'] = data['SO2'].astype('float')
data['DefaultSO2'] = data['DefaultSO2'].astype('float')
data['O3'] = data['O3'].astype('float')
data['DefaultO3'] = data['DefaultO3'].astype('float')



plt.figure(figsize=(15,10))

plt.subplot(2,2,1)   

plt.plot(data.Tarih,data.PM10,color="red",linewidth=1,linestyle="-",marker="o",
         markersize=3,label="PM10",alpha=0.9)
plt.plot(data.Tarih,data.DefaultPM10,color="red",linewidth=1,linestyle="-",marker="o",
         markersize=3,label="Ulusal Sınır Değer",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("PM10 Oranı")
plt.title("Anlatya'daki PM10 Grafiği")
plt.grid()
plt.legend()


plt.subplot(2,2,2)   
plt.plot(data.Tarih,data.SO2,color="blue",linewidth=1,linestyle="-",marker="o",
         markersize=3,label="SO2",alpha=0.9)
plt.plot(data.Tarih,data.DefaultSO2,color="red",linewidth=1,linestyle="-",marker="o",
         markersize=3,label="Ulusal Sınır Değer",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("SO2 Oranı")
plt.title("Antalya'daki SO2 Grafiği")
plt.grid()
plt.legend()


plt.subplot(2,2,3)   
plt.plot(data.Tarih,data.O3,color="green",linewidth=1,linestyle="-",marker="o",
         markersize=3,label="O3",alpha=0.9)
plt.plot(data.Tarih,data.DefaultO3,color="red",linewidth=1,linestyle="-",marker="o",
         markersize=3,label="Ulusal Sınır Değer",alpha=0.9)
plt.xlabel("Tarih")
plt.ylabel("O3 Oranı")
plt.title("Antalya'daki O3 Grafiği")
plt.grid()
plt.legend()


plt.subplot(2,2,3)
plt.plot(data.Tarih,data.O3,color="green")
plt.xlabel("Tarih")
plt.ylabel("O3 Oranı")
plt.title("Antalya'daki O3 Grafiği")
plt.grid()

plt.show()