import tkinter as tk

window = tk.Tk()
window.title("HW 1")
window.geometry("300x400")

dog_c = 0
cat_c = 0
selected = tk.StringVar(value="")

dog_img = tk.PhotoImage(file="img/dog.png")
cat_img = tk.PhotoImage(file="img/cat.png")

blank_img = tk.PhotoImage(width=256, height=256)

def show_animal():
    global dog_c, cat_c
    choice = selected.get()

    if choice == "dog":
        img_label.config(image=dog_img)
        dog_c += 1
    elif choice == "cat":
        img_label.config(image=cat_img)
        cat_c += 1

    label.config(text=f"Dog votes: {dog_c} | Cat votes: {cat_c}")

tk.Radiobutton(window, text="Dog", variable=selected, value="dog", command=show_animal).pack(anchor="n", padx=20, pady=10)
tk.Radiobutton(window, text="Cat", variable=selected, value="cat", command=show_animal).pack(anchor="n", padx=20)

img_label = tk.Label(window, image=blank_img, width=256, height=256)
img_label.pack(anchor="center",pady=20)

label = tk.Label(window, text="Dog votes: 0 | Cat votes: 0")
label.pack(side="bottom")

window.mainloop()
