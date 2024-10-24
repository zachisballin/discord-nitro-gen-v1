print("""
 
       .__  __                                         
  ____ |__|/  |________  ____      ____   ____   ____  
 /    \|  \   __\_  __ \/  _ \    / ___\_/ __ \ /    \ 
|   |  \  ||  |  |  | \(  <_> )  / /_/  >  ___/|   |  
|___|  /__||__|  |__|   \____/   \___  / \___  >___|  /
     \/                         /_____/      \/     \/ 
""")

import random
import string

def generate_random_code():
    # Define the characters to use for the random code
    characters = string.ascii_letters + string.digits
    # Generate a random 16-character code
    random_code = ''.join(random.choice(characters) for _ in range(16))
    # Append the code to the URL
    url = f"https://discord.gift/{random_code}"
    return url

def save_to_file(url):
    # Open the file in append mode ('a'), so new links are added without overwriting the existing ones
    with open("generated_links.txt", "a") as file:
        file.write(url + "\n")  # Write the URL to the file with a newline

def main():
    while True:
        # Generate the random URL
        generated_url = generate_random_code()
        print(generated_url)

        # Save the generated URL to the text file
        save_to_file(generated_url)
        print("The link has been saved to 'generated_links.txt'.")

        # Ask if the user wants to generate another link
        repeat = input("Would you like to generate another link? (yes/no): ").strip().lower()

        if repeat not in ('yes', 'y'):
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()
