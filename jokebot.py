# Random Joke Generator
import random
import time

def clear_screen():
    # Print multiple newlines to "clear" the screen
    print("\n" * 50)

def display_joke(joke, category=None):
    print("\n" + "=" * 50)
    if category:
        print(f"Category: {category}")
    
    # For two-part jokes (setup and punchline)
    if isinstance(joke, list) and len(joke) == 2:
        print(f"\n{joke[0]}")
        print("...")
        # Add a pause for dramatic effect
        time.sleep(2)
        print(f"\n{joke[1]} 😂")
    else:
        # For one-liner jokes
        print(f"\n{joke} 😂")
    
    print("=" * 50)

def main():
    # Dictionary of jokes categorized by type
    jokes = {
        "Python": [
            ["Why did the programmer quit his job?", "Because he didn't get arrays!"],
            ["How do you tell HTML from Python?", "One is a markup language and the other is a snake!"],
            ["What's a Python programmer's favorite meal?", "Spam and eggs!"],
            ["Why was the Python programmer wearing glasses?", "Because they couldn't C#!"],
            "I told my friend I was learning Python for coding. He asked if I was scared of snakes. I said 'No, but I'm terrified of indentation errors!'"
        ],
        "Programming": [
            ["Why do programmers always mix up Halloween and Christmas?", "Because Oct 31 == Dec 25!"],
            ["Why don't programmers like nature?", "It has too many bugs!"],
            ["What's a programmer's favorite place to hang out?", "Foo Bar!"],
            ["Why do Java developers wear glasses?", "Because they don't C#!"],
            "There are only 10 types of people in the world: those who understand binary and those who don't."
        ],
        "Dad Jokes": [
            ["Did you hear about the mathematician who's afraid of negative numbers?", "He'll stop at nothing to avoid them!"],
            ["Why don't scientists trust atoms?", "Because they make up everything!"],
            ["What did the janitor say when he jumped out of the closet?", "Supplies!"],
            ["What do you call a fake noodle?", "An impasta!"],
            "I would tell you a joke about UDP, but you might not get it."
        ]
    }
    
    print("🤣 RANDOM JOKE GENERATOR 🤣")
    print("=" * 30)
    print("Need a laugh? You've come to the right place!")
    
    while True:
        print("\nJoke Categories:")
        categories = list(jokes.keys())
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")
        print(f"{len(categories)+1}. Random (Any category)")
        print("0. Exit")
        
        # Get user choice
        try:
            choice = int(input("\nSelect a category (0-4): "))
            
            if choice == 0:
                print("\nThanks for using the Random Joke Generator! Have a great day! 👋")
                break
            
            elif 1 <= choice <= len(categories):
                # Get a specific category
                selected_category = categories[choice-1]
                joke = random.choice(jokes[selected_category])
                display_joke(joke, selected_category)
            
            elif choice == len(categories)+1:
                # Get a random category
                selected_category = random.choice(categories)
                joke = random.choice(jokes[selected_category])
                display_joke(joke, selected_category)
            
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # Ask if user wants another joke
            again = input("\nWant another joke? (yes/no): ").lower()
            if again not in ["yes", "y"]:
                print("\nThanks for using the Random Joke Generator! Have a great day! 👋")
                break
            
            clear_screen()
            
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()