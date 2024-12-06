import sys
import build_data
from operations import operations_dict
from data import CountyDemographics

original_data = build_data.get_data()

operation = sys.argv[1]

def entry_count(counties:list[CountyDemographics]):
    count = 0
    for county in counties:
        count += 1
    return count

try:
    print(entry_count(original_data),"records loaded")
    with open(operation, "r") as file:
        for line in file:
            current_line = line.strip()
            if ':' not in current_line:
                operation=current_line
                operation_func = operations_dict.get(operation)
                if operation=='population-total':
                    result = operation_func(original_data)
                    print(f'2014 populations:', result)
                elif operation=='display':
                    result = operation_func(original_data)
                    print(result)
            elif ':' in current_line:
                middleman = current_line.split(':')
                if len(middleman) == 3:
                    number=middleman[2]
                    operation = middleman[0]
                    operation_func = operations_dict.get(operation)
                    field = middleman[1]
                    if operation == 'filter-state':
                        original_data = operation_func(original_data, field)
                        print(f'Filter:state ==', field, "(" + str(entry_count(original_data)), "entries)")
                    elif '.' in field:
                        new_field = field.split('.')
                        subfield1 = new_field[0].lower()
                        subfield2 = new_field[1]
                        operation_func = operations_dict.get(operation)
                        if operation == 'filter-lt':
                            original_data = operation_func(original_data, subfield1, subfield2, number)
                            print(f'Filter:', field, "lt", number, "(" + str(entry_count(original_data)), "entries)")
                        elif operation == 'filter-gt':
                            original_data = operation_func(original_data, subfield1, subfield2, number)
                            print(f'Filter:', field, "gt", number, "(" + str(entry_count(original_data)), "entries)")

                else:
                    operation = middleman[0]
                    operation_func = operations_dict.get(operation)
                    field=middleman[1]
                    if operation=='filter-state':
                        original_data = operation_func(original_data, field)
                        print(f'Filter:state ==', field, "("+str(entry_count(original_data)),"entries)")
                    elif '.' in field:
                        new_field=field.split('.')
                        subfield1 = new_field[0].lower()
                        subfield2 = new_field[1]
                        operation_func = operations_dict.get(operation)
                        if operation=='percent':
                            result = operation_func(original_data, subfield1, subfield2)
                            print(f'2014', field, "percentage:" , str(result))
                        elif operation=='population':
                            original_data = operation_func(original_data, subfield1, subfield2)
                            print(f'2014', field, "population:" , str(result))
                        elif operation=='filter-lt':
                            original_data = operation_func(original_data, subfield1, subfield2, number)
                            print(f'Filter:', field, "lt",number,"("+str(entry_count(original_data)),"entries)")
                        elif operation=='filter-gt':
                            original_data = operation_func(original_data, subfield1, subfield2, number)
                            print(f'Filter:', field, "gt",number,"("+str(entry_count(original_data)),"entries)")

except FileNotFoundError:
    print("Please enter a valid file name.")
    exit()