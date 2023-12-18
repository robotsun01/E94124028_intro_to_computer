import matplotlib.pyplot as plt
import numpy as np

with open('Temperature.txt', 'r') as file: #以r的方式，開啟檔案
    file_content = file.read()

lines = file_content.split('\n') #讀取檔案，並把換行去掉
data_list = []

for line in lines[1:]: #讀取每一行資料
    values = line.split(', ')
    temperatures = [float(value) for value in values[1:]]
    data_list.append(temperatures)

data_transposed = list(zip(*data_list))
years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

plt.figure(figsize=(8, 5)) #第一張圖片
plt.title("Tainan Monthly Mean Temperature From 2013 To 2021")
plt.xlabel("Month")
plt.ylabel("Temperature in Degree C")
plt.ylim(16, 30)
plt.yticks(range(16, 31, 2))

for i in range(len(years)):
    plt.plot(range(1, 13), data_list[i], label=str(years[i]))
plt.legend(title="Year", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(range(1, 13))


plt.tight_layout() #儲存一
plt.savefig('lab12_01.png')
plt.show()


months = list(range(1, 13)) #第二張圖片
monthly_averages = np.mean(data_transposed, axis=1)
overall_average = np.mean(data_transposed)

plt.figure(figsize=(8, 5))
plt.plot(months, monthly_averages, marker='o', label='Monthly Average')
plt.axhline(overall_average, color='red', linestyle='--', label='Overall Average')

for i, txt in enumerate(monthly_averages):
    plt.annotate(f'{txt:.2f}', (months[i], txt), textcoords="offset points", xytext=(0, 5), ha='center')

plt.annotate(f'Avg: {overall_average:.2f}', xy=(6, overall_average),
             xytext=(10, 5), textcoords='offset points',
             arrowprops=dict(arrowstyle="->"), ha='center')

plt.title('Monthly Mean Temperature Averages')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend()


plt.tight_layout() #儲存二
plt.savefig('lab12_02.png')
plt.show()

#圖片合併
plt.figure(figsize=(14, 5)) #第一張

plt.subplot(1, 2, 1)
plt.title("Tainan Monthly Mean Temperature From 2013 To 2021")
plt.xlabel("Month")
plt.ylabel("Temperature in Degree C")
plt.ylim(16, 30)
plt.yticks(range(16, 31, 2))

for i in range(len(years)):
    plt.plot(range(1, 13), data_list[i], label=str(years[i]))
plt.legend(title="Year", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(range(1, 13))

plt.subplot(1, 2, 2) #第二張
plt.plot(months, monthly_averages, marker='o', label='Monthly Average')
plt.axhline(overall_average, color='red', linestyle='--', label='Average')

for i, txt in enumerate(monthly_averages):
    plt.annotate(f'{txt:.2f}', (months[i], txt), textcoords="offset points", xytext=(0, 5), ha='center')

plt.annotate(f'Overall Avg: {overall_average:.2f}', xy=(6, overall_average),
             xytext=(10, 5), textcoords='offset points',
             arrowprops=dict(arrowstyle="->"), ha='center')

plt.title('Monthly Mean Temperature Averages')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend()

plt.tight_layout() #儲存第三張圖片
plt.savefig('lab12_03.png')
plt.show()
