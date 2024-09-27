import random

def pick_random_person():
    # List of people
    people = ['abhi', 'jayanth', 'nagraju', 'prashant', 'pallavi', 'raksha', 'sachin']
    
    # Randomly select one person from the list
    selected_person = random.choice(people)
    
    return selected_person

# Example of how you'd call the function:
print(pick_random_person())
