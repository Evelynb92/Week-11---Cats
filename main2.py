from cat import Cat

#Window Box
import tkinter as tk    

window = tk.Tk()
window.title('Cats!!!')
    
window.geometry('400x300')

# text labels
window_bg = '#E5EFC1'
button_bg = '#557B83'

window.config(bg=window_bg)


def user_input():
    breed = breed_input.get()
    age = age_input.get()
    gender = gender_input.get()
    color = color_input.get()
    
    cat = Cat(breed,age,gender,color)

    with open('cats.txt','w') as file:
            file.write(f"{cat.breed},{cat.age},{cat.gender},{cat.color},{cat.picture} \n")

def clear_button():
    breed_input.delete(0,tk.END)
    age_input.delete(0,tk.END)
    gender_input.delete(0,tk.END)  
    color_input.delete(0,tk.END)  
    return None
  
def exit_button():
    window.destroy()
      

# text labels
breed_label = tk.Label(text="Breed:",bg=window_bg, font=('', 10, 'bold'))
breed_label.grid(row=0, column=0)
    
age_label = tk.Label(text="Age:",bg=window_bg, font=('', 10, 'bold'))
age_label.grid(row=1, column=0)
    
gender_label = tk.Label(text="Gender:",bg=window_bg, font=('', 10, 'bold'))
gender_label.grid(row=2, column=0)
    
color_label = tk.Label(text="Color:",bg=window_bg, font=('', 10, 'bold'))
color_label.grid(row=3, column=0)
    
#input fields
breed_input = tk.Entry()
breed_input.grid(row=0, column=1)
    
age_input = tk.Entry()
age_input.grid(row=1, column=1)
    
gender_input = tk.Entry()
gender_input.grid(row=2, column=1)
    
color_input = tk.Entry()
color_input.grid(row=3, column=1)
    
#buttons
submit_button = tk.Button(text="Submit", bg=button_bg, command=user_input)
submit_button.grid(row=20, column=1)
    
clear_button = tk.Button(text="Clear", bg=button_bg, command=clear_button)
clear_button.grid(row=50, column=1)
    
exit_button = tk.Button(text="Exit", bg=button_bg, command=exit_button)
exit_button.grid(row=70, column=1)
        
window.mainloop()

   
      
    
    
#file.write(f"{_.breed},{_.age},{_.gender},{_.color},{_.picture} \n")
  
    
    
