from admin import admin_loop
from common import process_user_input
from difflib import get_close_matches
from db import sessions

def list_menu_items():
    print("1. list sessions")
    print("2. search movie")
    print("3. my tickets")
    print("4. admin")
    return process_user_input()

def greetings():
    print("Welcome to the movie ticket booking system")
    print("Please enter EXIT to exit")
    

def search_movie():
    print("Search for a movie")
    query = input("Enter movie name: ").strip()
    exact_matches = {k: v for k, v in sessions.items() if v["film_name"].lower() == query.lower()}
    if exact_matches:
        print("Exact matches:")
        for session_id, session in exact_matches.items():
            print(f"\t{session['film_name']} at {session['start_time']} (Session ID: {session_id})")
    else:
        movie_titles = [session["film_name"] for session in sessions.values()]
        fuzzy_matches = get_close_matches(query, movie_titles)
        if fuzzy_matches:
            print("No exact matches found. Did you mean:")
            for fuzzy_matches in fuzzy_matches:
                print(f"\t{fuzzy_matches}")
        else:
            print("No matches found")
   

def program_loop():
    while True:
        user_input = list_menu_items()
        match user_input:
            case "1":
                print("Listing sessions")
            case "2":
                print("Searching movie")
            case "3":
                print("Listing tickets")
            case "4":
                admin_loop()
            case _:
                print("Invalid input")

def main():
    greetings()
    program_loop()


if __name__ == "__main__":
    main()
