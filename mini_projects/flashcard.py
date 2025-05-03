import random

class FlashcardApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self):
        term = input("Enter the term: ")
        definition = input("Enter the definition: ")
        self.flashcards.append({'term': term, 'definition': definition})

    def quiz(self):
        if not self.flashcards:
            print("No flashcards available. Please add some first!")
            return

        print("\nStarting quiz...")
        random.shuffle(self.flashcards)
        score = 0
        for flashcard in self.flashcards:
            print(f"\nTerm: {flashcard['term']}")
            answer = input("What is the definition? ")

            if answer.lower() == flashcard['definition'].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct definition is: {flashcard['definition']}")

        print(f"\nQuiz completed! Your score: {score}/{len(self.flashcards)}")

    def view_flashcards(self):
        if not self.flashcards:
            print("No flashcards available.")
            return

        print("\nYour flashcards:")
        for flashcard in self.flashcards:
            print(f"Term: {flashcard['term']} - Definition: {flashcard['definition']}")

    def menu(self):
        while True:
            print("\nFlashcard App Menu:")
            print("1. Add Flashcard")
            print("2. View Flashcards")
            print("3. Start Quiz")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                self.add_flashcard()
            elif choice == '2':
                self.view_flashcards()
            elif choice == '3':
                self.quiz()
            elif choice == '4':
                print("Exiting Flashcard App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


flashcard_app = FlashcardApp()
flashcard_app.menu()
