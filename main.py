# This is a tool to help fiction writers generate ideas for
# unique characters. The user inputs the first and last name, gender and
# an archetype and a unique character is generated.


import traits
from classes import Character
import archetypes as arch


def characterize(first='Jane', last='Doe', gender='Female', archetype=arch.standard):
    # Generate a fictional character based on user arguments.
    f = open('character.txt','w')
    my_char = Character(first, last, gender, archetype)  # Create a character.
    my_char.sample_traits(archetype)   # Sample some personality traits.
    f.write(my_char.export_markdown())    # Serialize character sheet in Markdown.
    f.close()

def main():
  first_name = input("Please enter the character's First Name: ")
  last_name = input("Please enter the character's Last Name: ")
  char_gender = input("Please enter the character's Gender: ")
  choose_arch = input("Please enter the character's archetype (standard | antagonist): ")

  if choose_arch == "standard":
      characterize(first_name, last_name, char_gender, archetype=arch.standard)
  elif choose_arch == "antagonist":
      characterize(first_name, last_name, char_gender, archetype=arch.antagonist)
  else:
      print("Please make a valid selection.")

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
