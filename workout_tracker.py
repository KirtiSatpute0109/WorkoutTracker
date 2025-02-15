import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        return '\n'.join(str(workout) for workout in self.workouts)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                date, exercise_type, duration, calories_burned = line.strip().split(',')
                workout = Workout(date, exercise_type, int(duration), int(calories_burned))
                self.workouts.append(workout)

class WorkoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Workout Tracker")
        self.root.geometry("500x400")
        self.root.config(bg="#f0f0f0")
        self.root.resizable(False, False)

        self.user = None

        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#4CAF50", foreground="white", font=("Arial", 12))
        self.style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
        
        # Welcome label
        self.welcome_label = tk.Label(root, text="Welcome to Workout Tracker", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#4CAF50")
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

        # User input section
        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(root, font=("Arial", 12))
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.age_label = tk.Label(root, text="Enter your age:")
        self.age_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.age_entry = tk.Entry(root, font=("Arial", 12))
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        self.weight_label = tk.Label(root, text="Enter your weight (kg):")
        self.weight_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.weight_entry = tk.Entry(root, font=("Arial", 12))
        self.weight_entry.grid(row=3, column=1, padx=10, pady=5)

        self.submit_button = ttk.Button(root, text="Create Account", command=self.create_user)
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Workout buttons (Initially disabled)
        self.workout_button = ttk.Button(root, text="Add Workout", state=tk.DISABLED, command=self.add_workout)
        self.workout_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.view_button = ttk.Button(root, text="View Workouts", state=tk.DISABLED, command=self.view_workouts)
        self.view_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.save_button = ttk.Button(root, text="Save Data", state=tk.DISABLED, command=self.save_data)
        self.save_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.load_button = ttk.Button(root, text="Load Data", state=tk.DISABLED, command=self.load_data)
        self.load_button.grid(row=8, column=0, columnspan=2, pady=10)

    def create_user(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        weight = self.weight_entry.get()

        if not name or not age or not weight:
            messagebox.showerror("Input Error", "Please fill out all fields.")
            return

        try:
            age = int(age)
            weight = float(weight)
        except ValueError:
            messagebox.showerror("Input Error", "Age must be an integer and weight must be a number.")
            return

        self.user = User(name, age, weight)

        # Hide entry fields and display buttons for workout tracking
        self.name_label.grid_forget()
        self.name_entry.grid_forget()
        self.age_label.grid_forget()
        self.age_entry.grid_forget()
        self.weight_label.grid_forget()
        self.weight_entry.grid_forget()
        self.submit_button.grid_forget()

        self.workout_button.config(state=tk.NORMAL)
        self.view_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.NORMAL)
        self.load_button.config(state=tk.NORMAL)

        messagebox.showinfo("Success", f"Account created for {name}!")

    def add_workout(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Workout")
        add_window.geometry("400x300")
        add_window.config(bg="#f0f0f0")

        tk.Label(add_window, text="Enter the date (YYYY-MM-DD):", bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        date_entry = tk.Entry(add_window, font=("Arial", 12))
        date_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Enter the exercise type:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        exercise_entry = tk.Entry(add_window, font=("Arial", 12))
        exercise_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Enter the duration (minutes):", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        duration_entry = tk.Entry(add_window, font=("Arial", 12))
        duration_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Enter the calories burned:", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        calories_entry = tk.Entry(add_window, font=("Arial", 12))
        calories_entry.grid(row=3, column=1, padx=10, pady=10)

        def submit_workout():
            date = date_entry.get()
            exercise_type = exercise_entry.get()
            duration = duration_entry.get()
            calories_burned = calories_entry.get()

            if not date or not exercise_type or not duration or not calories_burned:
                messagebox.showerror("Input Error", "Please fill out all fields.")
                return

            try:
                duration = int(duration)
                calories_burned = int(calories_burned)
            except ValueError:
                messagebox.showerror("Input Error", "Duration and calories must be integers.")
                return

            workout = Workout(date, exercise_type, duration, calories_burned)
            self.user.add_workout(workout)
            messagebox.showinfo("Success", "Workout added successfully!")
            add_window.destroy()

        submit_button = ttk.Button(add_window, text="Submit", command=submit_workout)
        submit_button.grid(row=4, column=0, columnspan=2, pady=20)

    def view_workouts(self):
        if self.user.workouts:
            workout_list = self.user.view_workouts()
            messagebox.showinfo("Workouts", workout_list)
        else:
            messagebox.showinfo("Workouts", "No workouts available.")

    def save_data(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            self.user.save_data(filename)
            messagebox.showinfo("Success", "Data saved successfully!")

    def load_data(self):
        filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename:
            self.user.load_data(filename)
            messagebox.showinfo("Success", "Data loaded successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkoutApp(root)
    root.mainloop()
