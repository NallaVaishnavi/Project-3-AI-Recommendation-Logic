# AI Recommendation Logic
# Book Recommendation System

books = {
    "Atomic Habits": ["motivation", "productivity", "self-help"],
    "Rich Dad Poor Dad": ["finance", "money", "business"],
    "The Alchemist": ["motivation", "adventure", "fiction"],
    "Deep Work": ["productivity", "focus", "career"],
    "Think and Grow Rich": ["finance", "motivation", "success"]
}

print("===== Book Recommendation System =====")
print("\nAvailable Interests:")
print("motivation, productivity, self-help, finance, money, business,")
print("adventure, fiction, focus, career, success")

# Take user input
user_input = input("\nEnter your interests separated by commas: ")

# Convert input into a list
preferences = user_input.lower().split(",")

# Store recommendation scores
scores = {}

# Compare user interests with book tags
for book, tags in books.items():

    match_score = 0

    for preference in preferences:

        preference = preference.strip()

        if preference in tags:
            match_score += 1

    scores[book] = match_score

# Sort books based on score
recommended_books = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nRecommended Books:")

found = False

for book, score in recommended_books:

    if score > 0:
        print(f"{book} - Match Score: {score}")
        found = True

if not found:
    print("No matching books found.")