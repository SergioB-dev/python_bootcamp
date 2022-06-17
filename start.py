def add(a,b):
    return a + b


countries = ['ghana', 'saudi', 'nigeria', 'yemen', 'sudan']


# Task 1: create a function that takes a list and spits out the list in alphabetical order

index = 1

for country in countries:
    print(f'{index}: ', country)
    index += 1

def alphabetize(some_list):

    results = copy(some_list)
    not_in_order_results = []
    for i in range(0, len(some_list) - 1):
        if some_list[i][0] < some_list[i + 1][0]:
            pass
        elif some_list[i][0] < some_list[i + 2][0]:
            pass

        
    print(not_in_order_results)

    return results

print(alphabetize(countries))