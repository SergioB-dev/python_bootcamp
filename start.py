


countries = ['ghana', 'saudi', 'nigeria', 'yemen', 'sudan']


# Task 1: create a function that takes a list and spits out the list in alphabetical order

def alphabetize(some_list):
    
    for i in range(0, len(some_list)):
        for j in range(0, len(some_list)):
            if some_list[j] > some_list[i]:
                temp = some_list[i]
                some_list[i] = some_list[j]
                some_list[j] = temp
    return some_list
    
print(alphabetize(countries))


