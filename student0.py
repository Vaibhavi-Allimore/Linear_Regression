import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.linear_model import LinearRegression


# Dataset
X = np.array([
    [1], [2], [3], [4], [5],
    [6], [7], [8], [9], [10]
])

y = np.array([
    35, 40, 50, 55, 65,
    70, 75, 85, 90, 95
])


# Create and train model
model = LinearRegression()
model.fit(X, y)


# Prediction function
def predict_marks():

    try:
        hours = float(entry_hours.get())

        if hours < 0:
            messagebox.showerror(
                "Error",
                "Study hours cannot be negative."
            )
            return

        prediction = model.predict([[hours]])

        result_label.config(
            text=f"Predicted Marks: {prediction[0]:.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )


# Create window
root = tk.Tk()
root.title("Student Marks Predictor")
root.geometry("450x300")


# Heading
title_label = tk.Label(
    root,
    text="Student Marks Predictor",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)


# Input label
hours_label = tk.Label(
    root,
    text="Enter Study Hours:",
    font=("Arial", 13)
)
hours_label.pack()


# Input box
entry_hours = tk.Entry(
    root,
    font=("Arial", 13),
    width=20
)
entry_hours.pack(pady=10)


# Button
predict_button = tk.Button(
    root,
    text="Predict Marks",
    font=("Arial", 13, "bold"),
    command=predict_marks
)
predict_button.pack(pady=15)


# Result
result_label = tk.Label(
    root,
    text="Predicted Marks: ",
    font=("Arial", 15, "bold")
)
result_label.pack(pady=10)


# Run application
root.mainloop()
