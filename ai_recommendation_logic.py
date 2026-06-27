import tkinter as tk
from tkinter import scrolledtext

class Item:
    def __init__(self, name, category, tags):
        self.name = name
        self.category = category
        self.tags = tags

class RecommendationSystem:
    def __init__(self):
        self.items = []
        self.create_sample_data()

    def create_sample_data(self):
        self.items.append(Item("Inception", "Movies", ["sci-fi", "thriller", "action"]))
        self.items.append(Item("Titanic", "Movies", ["romance", "drama"]))
        self.items.append(Item("Interstellar", "Movies", ["space", "science", "sci-fi"]))
        self.items.append(Item("The Notebook", "Movies", ["romance", "love", "drama"]))
        self.items.append(Item("Avengers", "Movies", ["action", "superhero", "fantasy"]))
        self.items.append(Item("Python Basics", "Courses", ["coding", "python", "beginner"]))
        self.items.append(Item("Machine Learning", "Courses", ["ai", "data", "python"]))
        self.items.append(Item("Web Development", "Courses", ["html", "css", "javascript"]))
        self.items.append(Item("Data Science", "Courses", ["data", "analysis", "python"]))
        self.items.append(Item("Yoga for Beginners", "Fitness", ["health", "mind", "body"]))
        self.items.append(Item("Cardio Blast", "Fitness", ["workout", "energy", "strength"]))
        self.items.append(Item("Meditation Guide", "Fitness", ["mind", "relax", "focus"]))

    def calculate_similarity(self, user_tags, item_tags):
        common = len(set(user_tags).intersection(set(item_tags)))
        total = len(set(user_tags).union(set(item_tags)))
        if total == 0:
            return 0
        return common / total

    def recommend(self, category, interests):
        recommendations = []
        for item in self.items:
            if item.category == category:
                score = self.calculate_similarity(interests, item.tags)
                if score > 0:
                    recommendations.append((item.name, round(score, 2)))
        recommendations.sort(key=lambda x: x[1], reverse=True)
        return recommendations[:5]

def generate_recommendations():
    category = category_var.get()
    interests = entry_interests.get().lower().split(",")
    interests = [i.strip() for i in interests if i.strip()]
    if not category or not interests:
        chat_window.insert(tk.END, "Please select a category and enter interests.\n\n")
        return
    recs = system.recommend(category, interests)
    chat_window.insert(tk.END, f"Recommendations for {category}:\n")
    if not recs:
        chat_window.insert(tk.END, "No matches found.\n\n")
    else:
        for name, score in recs:
            chat_window.insert(tk.END, f"{name} (Match Score: {score})\n")
        chat_window.insert(tk.END, "\n")
    chat_window.see(tk.END)

system = RecommendationSystem()
root = tk.Tk()
root.title("AI Recommendation Logic 💡")
root.geometry("550x500")
root.configure(bg="#E8F0FE")

title_label = tk.Label(root, text="AI Recommendation System", font=("Arial", 16, "bold"), bg="#E8F0FE")
title_label.pack(pady=10)

category_var = tk.StringVar()
category_label = tk.Label(root, text="Select Category:", font=("Arial", 12), bg="#E8F0FE")
category_label.pack()
category_menu = tk.OptionMenu(root, category_var, "Movies", "Courses", "Fitness")
category_menu.pack(pady=5)

entry_label = tk.Label(root, text="Enter your interests (comma separated):", font=("Arial", 12), bg="#E8F0FE")
entry_label.pack()
entry_interests = tk.Entry(root, width=50, font=("Arial", 12))
entry_interests.pack(pady=5)

recommend_button = tk.Button(root, text="Get Recommendations", command=generate_recommendations, font=("Arial", 12), bg="#4CAF50", fg="white")
recommend_button.pack(pady=10)

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, font=("Arial", 11))
chat_window.pack(padx=10, pady=10)
chat_window.insert(tk.END, "Welcome! Select a category and enter your interests to get recommendations.\n\n")

root.mainloop()
