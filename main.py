from data import data as raw_data

try:
    columns = ['brand', 'model', 'fuel', 'cylinders', 'type',
               'power', 'weight', 'city_consumption', 'highway_consumption', 'price']
    data = []

    choice = input('''Select an option:
    1. Display standard deviation for a specific column
    2. Display vehicles sorted by a specific column
    3. Display the top 5 vehicles with the highest values for a specific column
    4. Display the top 5 vehicles with the lowest values for a specific column
    5. Display the quantity of cars for each type of value in a specific column
    6. Show all data for a vehicle by providing the model name

    Your choice -> ''')
    choice = int(choice)

    print('')
    print('')

    def list_size(lst):
        size = 0
        for i in lst:
            size += 1
        return size

    def sum_list(lst):
        total = 0
        for i in lst:
            total += i
        return total

    # Transforms raw data into a list of dictionaries for easier manipulation
    for i in range(list_size(raw_data)):
        dictionary = {}
        for k in range(list_size(columns)):
            dictionary[columns[k]] = raw_data[i][k]
        data.append(dictionary)

    def reverse_list(lst):
        reversed_lst = []
        for i in range(list_size(lst)):
            reversed_lst.append(lst[list_size(lst) - 1 - i])
        return reversed_lst

    def bubble_sort_by_column(lst, column):
        for i in range(list_size(lst)):
            for j in range(list_size(lst) - 1):
                if lst[j][column] > lst[j + 1][column]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst

    def standard_deviation(lst, column):
        values = [value[column] for value in lst]
        print(values)
        mean = sum_list(values) / list_size(values)
        variance = sum_list(
            [(x - mean) ** 2 for x in values]) / list_size(values)
        result = variance ** 0.5
        return ['Standard deviation by city consumption', result]

    def sort(lst, column):
        sorted_lst = bubble_sort_by_column(lst, column)

        response = [
            f'{item["brand"]} {item["model"]} -> {item["price"]}' for item in sorted_lst]

        return ['Cars sorted by price', *response]

    def sort_top_five_highest(lst, column):
        sorted_lst = bubble_sort_by_column(lst, column)
        sorted_lst = reverse_list(sorted_lst)
        top_five = [
            f'{item["brand"]} {item["model"]} -> {item[column]}' for item in sorted_lst[:5]
        ]

        return ["Top 5 most powerful cars", *top_five]

    def sort_top_five_lowest(lst, column):
        sorted_lst = bubble_sort_by_column(lst, column)
        top_five = [
            f'{item["brand"]} {item["model"]} -> {item[column]}' for item in sorted_lst[:5]]

        return ['Top 5 cars with lowest highway consumption', *top_five]

    def quantity_by_type(lst, column):
        values = [value[column] for value in lst]
        response = {}
        for value in values:
            if value in response:
                response[value] += 1
            else:
                response[value] = 1
        return ['Quantity of cars by type', response]

    def data_by_model(lst, column):
        model = input('Enter the model: ')

        for item in lst:
            if item[column] == model:
                return ['Vehicle data by model', item]
        return ['Vehicle data by model', 'Model not found']

    # Dictionary mapping user choices to functions
    choice_to_function = {
        1: {
            'column': 'city_consumption',
            'function': standard_deviation,
        },
        2: {
            'column': 'price',
            'function': sort,
        },
        3: {
            'column': 'power',
            'function': sort_top_five_highest,
        },
        4: {
            'column': 'highway_consumption',
            'function': sort_top_five_lowest,
        },
        5: {
            'column': 'type',
            'function': quantity_by_type,
        },
        6: {
            'column': 'model',
            'function': data_by_model,
        }
    }

    # Mechanism that determines which function will be executed and which column will be used based on user input
    column = choice_to_function[choice]['column']
    function = choice_to_function[choice]['function']
    response = function(data, column)

    print('---------------------------------------------')
    print(*response, sep='\n')
    print('---------------------------------------------')
except:
    print('---------------------------------------------')
    print('Command not found!')
    print('---------------------------------------------')
