# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open('test_file/task_3.txt', 'r') as f:
    data = f.read().strip()

buy_sum = 0  # Сумма считываемой покупки
list_sum = []  # Список сумм каждой покупки

# Проходимся по каждой строке в данных
for line in data.split('\n'):
    if line == '':  # Если текущая строка пустая, то сохраняем сумму текущей покупки и обнуляем переменную
        list_sum.append(buy_sum)
        buy_sum = 0
    else:  # Если текущая строка не пустая, то добавляем цену товара к сумме текущей покупки
        buy_sum += int(line)

# Находим три самых дорогих покупки
sorted_purchase_sums = sorted(list_sum, reverse=True)
three_most_expensive_purchases = sum(sorted_purchase_sums[:3])

print(three_most_expensive_purchases)  # самопроверка

assert three_most_expensive_purchases == 202346
