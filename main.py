import pandas as pd

#1. Самостоятельно создайте DataFrame с данными
df = pd.read_excel('data.xlsx')

# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
print('Первые 5 строк данных:')
print(df.head(5))

#3. Вычислите среднюю оценку по каждому предмету
columns = list(df.columns)
columns.pop(0)
print('Средний бал по предметам:')
for column in columns:
    print(f' {column} - {df[column].mean():.2f}')

#4. Вычислите медианную оценку по каждому предмету
print('Медианная оценка по предметам:')
for column in columns:
    print(f' {column} - {df[column].median():.2f}')

#5. Вычислите Q1 и Q3 для оценок по математике:
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print('Расчет первого и третьего квартиля для предмета математика:')
print(f'Q1 = {Q1_math} ..... Q3 = {Q3_math}')
#Расчет IQR
print(f'Межквартальный размах: IQR = {Q3_math-Q1_math}')

#6. Вычислите стандартное отклонение
print('Стандартные отклонения оценок по предметам:')
for column in columns:
    print(f' {column} - {df[column].std():.2f}')
print('Стандартные отклонения оценок по ученикам:')
for row_index in range(len(df['Ученик'])):
    print(f'{df.iloc[row_index,0]} - {df.iloc[row_index][1:].std():.2f}')