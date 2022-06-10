data1 = [
  ["Цатакий, С.Ш.#0.582", "+7 887 515-22-33", "+7 887 515-22-33"],
  ["Битли, Д.Ф.#0.096",	"+7 805 261-09-79",	"+7 805 261-09-79"],
  [None, None, None],
  ["Гонимич, А.Т.#0.835", "+7 502 300-28-51",	"+7 502 300-28-51"],
  ["Делин, Я.Д.#0.501",	"+7 504 926-16-64",	"+7 504 926-16-64"],
  ["Гонимич, А.Т.#0.835",	"+7 502 300-28-51",	"+7 502 300-28-51"],
]

data2 = [
  ["Загак, Р.А.#0.819",	"+7 693 549-65-81",	"+7 693 549-65-81"],
  ["Чудский, П.Т.#0.770",	"+7 571 690-56-36",	"+7 571 690-56-36"],
  [None, None, None],
  ["Чудский, П.Т.#0.770", "+7 571 690-56-36",	"+7 571 690-56-36"],
  ["Кисулман, Л.Н.#0.510",	"+7 625 100-60-24",	"+7 625 100-60-24"],
]

from pprint import pprint
import re


def make(table):
    rows_count = len(table)
    cols_count = len(table[0])

    cols_data = {}
    rows_data = {}

    cols_removes = []
    rows_removes = []

    for i in range(cols_count):
        res_list = list(map(lambda x: x[i] or "", table))
        res = '|'.join(res_list)
        if(not cols_data.get(res)):
            cols_data[res] = True
        else:
            cols_removes.append(i)

    for i in range(rows_count):
        res_list = list(map(lambda x: x or "", table[i]))
        res = "|".join(res_list)
        if(not rows_data.get(res) and res_list.count("") != cols_count):
            rows_data[res] = True
        else:
            rows_removes.append(i)

    tableAfterRemoveRows = list(
        map(
            lambda x: x[1],
            filter(lambda x: x[0] not in rows_removes, enumerate(table)))
    )

    def removeFn(row):
        return list(map(
            lambda x: x[1], filter(
                lambda x: x[0] not in cols_removes,
                enumerate(row)
            )
        ))

    tableAfterRemove = list(map(removeFn, tableAfterRemoveRows))

    def splitIndex0(row):
        item = row[0]
        row.insert(0, item)
        row[0] = item.split("#")[0]
        row[1] = item.split("#")[1]
        row = row[1:] + row[0:1]
        return row

    tableAfterSplit = list(map(splitIndex0, tableAfterRemove))

    def transformItem(item):
        item = str(item)
        if(item.startswith("+")):
            return str("".join(
                [char for char in item if re.search(r'\d', char)])[1:])
        if(re.search(r'^[а-яА-ЯёЁ]', item)):
            return item.split(",")[0]
        return str(round(float(item), 1))

    transformedTable = [
        list(map(transformItem, row)) for row in tableAfterSplit
    ]
    sortedList = sorted(transformedTable, key=lambda item: item[2])

    transposedTable = list(list(a) for a in zip(*sortedList))

    return transposedTable


def main(table):
    return make(table)



res1 = main(data1)
res2 = main(data2)
def print_list(table): 
  for row in table:
    # print(type(row[0]))
    # print(type(row))
    # print(type(table))
    print(" ".join(list(map(lambda x: str(x), row))))
    
    
pprint(res1)
print("---")
pprint(res2)