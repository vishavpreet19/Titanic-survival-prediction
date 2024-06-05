import tkinter as tk
from tkinter import messagebox

def predict_survival():
    try:
        # Get the input values
        pclass = int(entry_pclass.get())
        sex = entry_sex.get().lower()
        age = float(entry_age.get())
        fare = float(entry_fare.get())
        
        # Simple rule-based approach
        if sex == 'female':
            if pclass == 1:
                if age < 50 and fare > 50:
                    messagebox.showinfo("Survival Prediction", "Survived")
                else:
                    messagebox.showinfo("Survival Prediction", "Not Survived")
            else:
                messagebox.showinfo("Survival Prediction", "Survived")
        else:
            if age < 10:
                messagebox.showinfo("Survival Prediction", "Survived")
            else:
                messagebox.showinfo("Survival Prediction", "Not Survived")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Titanic Survival Prediction")

# Create labels and entry fields
tk.Label(root, text="Passenger Class (1, 2, 3):").grid(row=0, column=0)
entry_pclass = tk.Entry(root)
entry_pclass.grid(row=0, column=1)

tk.Label(root, text="Sex (male or female):").grid(row=1, column=0)
entry_sex = tk.Entry(root)
entry_sex.grid(row=1, column=1)

tk.Label(root, text="Age:").grid(row=2, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=2, column=1)

tk.Label(root, text="Fare:").grid(row=3, column=0)
entry_fare = tk.Entry(root)
entry_fare.grid(row=3, column=1)

# Create predict button
predict_button = tk.Button(root, text="Predict Survival", command=predict_survival)
predict_button.grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()