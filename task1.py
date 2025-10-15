import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # 1. Геттеры
    @property
    def name_items(self):
        return self.__name_items.copy()  # Возвращаем копию для защиты данных

    @property
    def number_items(self):
        return self.__number_items

    # 2. Добавление товара в чек
    def add_item_to_cheque(self, name):
        if not name or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. Удаление товара из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. Расчет общей стоимости товаров
    def check_amount(self):
        total_sum = sum(self.__item_price[item] for item in self.__name_items)
        
        if self.__number_items > 10:
            total_sum *= 0.9  # Скидка 10%
        
        return total_sum

    # 5. Расчет НДС для товаров со ставкой 20%
    def twenty_percent_tax_calculation(self):
        items_20_percent = [item for item in self.__name_items if self.__tax_rate[item] == 20]
        
        if not items_20_percent:
            return 0
        
        total_price = sum(self.__item_price[item] for item in items_20_percent)
        tax_amount = total_price * 0.2
        
        # Учет скидки при большом количестве товаров
        if self.__number_items > 10:
            tax_amount *= 0.9
        
        return tax_amount

    # 6. Расчет НДС для товаров со ставкой 10%
    def ten_percent_tax_calculation(self):
        items_10_percent = [item for item in self.__name_items if self.__tax_rate[item] == 10]
        
        if not items_10_percent:
            return 0
        
        total_price = sum(self.__item_price[item] for item in items_10_percent)
        tax_amount = total_price * 0.1
        
        # Учет скидки при большом количестве товаров
        if self.__number_items > 10:
            tax_amount *= 0.9
        
        return tax_amount

    # 7. Общая сумма налогов
    def total_tax(self):
        return self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()

    # 8. Возврат номера телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        
        return f'+7{telephone_number}'

    # Дополнительный метод: получение даты и времени
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        
        time_components = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        
        for component_name, getter_func in time_components:
            value = getter_func(now)
            date_and_time.append(f'{component_name}: {value}')
        
        return date_and_time