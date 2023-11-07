# TODO Напишите функцию для поиска индекса товара

def index(list_: list, find_item: str) -> int:
    for i in enumerate(list_):
        if i[1] == find_item:
            return i[0]



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

if __name__ == "__main__":
    for find_item in ['банан', 'груша', 'персик']:
        index_item = index(items_list, find_item)
        if index_item is not None:
            print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
        else:
            print(f"Товар '{find_item}' не найден в списке.")