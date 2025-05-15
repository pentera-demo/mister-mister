import random

# List of ASCII art animals
animals = [
    r"""
     /\_/\
    ( o.o ) 
     > _ <  
    """,
    r"""
     /\_/\
    ( o.o ) 
     >() <  
    """,
    r"""
     /\_/\
    ( o.o ) 
     > - <  
    """,
    r"""
     /\_/\
    ( o.o ) 
     > = <  
    """,
    r"""
     /\_/\
    ( o.o ) 
     > ^ <  
    """
]

def generate_random_animal():
    return random.choice(animals)

if __name__ == "__main__":
    print("Here is a random animal:")
    print(generate_random_animal()) 
