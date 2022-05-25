import tkinter as tk
from tkinter import PhotoImage
from cat import Cat
from tkinter import filedialog

class GUI:

  def __init__(self,breed_input,age_input,gender_input,color_input,pic_input=''):

    self.breed_input = breed_input
    self.age_input = age_input
    self.gender_input = gender_input
    self.color_input = color_input
    self.pic_input = ''

    #Window Box
    
    self.window = tk.Tk()
    self.window.title('Cats 4$ho!!')

    self.valid = PhotoImage(file="check.png")

    self.breed_validate = tk.Label(text='', bg='#E5EFC1')
    self.breed_validate.grid(row=0, column=3)
    
    self.age_validate = tk.Label(text='',bg='#E5EFC1')
    self.age_validate.grid(row=1, column=3)
    
    self.gender_validate = tk.Label(text='',bg='#E5EFC1')
    self.gender_validate.grid(row=2, column=3)
    
    self.color_validate = tk.Label(text='',bg='#E5EFC1')
    self.color_validate.grid(row=3, column=3)
    
    self.window.geometry('400x300')
    
    self.window_bg = '#E5EFC1'
    self.button_bg = '#557B83'
    
    self.window.config(bg=self.window_bg)

        
    # text labels
    breed_label = tk.Label(text="Breed:",bg=self.window_bg, font=('', 10, 'bold'))
    breed_label.grid(row=0, column=0)
    
    age_label = tk.Label(text="Age:",bg=self.window_bg, font=('', 10, 'bold'))
    age_label.grid(row=1, column=0)
    
    gender_label = tk.Label(text="Gender:",bg=self.window_bg, font=('', 10, 'bold'))
    gender_label.grid(row=2, column=0)
    
    color_label = tk.Label(text="Color:",bg=self.window_bg, font=('', 10, 'bold'))
    color_label.grid(row=3, column=0)

    pic_label = tk.Label(text="Picture:",bg=self.window_bg, font=('', 10, 'bold'))
    pic_label.grid(row=4, column=0)
    
    #input fields
    self.breed_input = tk.Entry()
    self.breed_input.grid(row=0, column=1)
    
    self.age_input = tk.Entry()
    self.age_input.grid(row=1, column=1)
    
    self.gender_input = tk.Entry()
    self.gender_input.grid(row=2, column=1)
    
    self.color_input = tk.Entry()
    self.color_input.grid(row=3, column=1)

    # self.pic_input = tk.Entry()
    # self.path = filedialog.askopenfilename(initialdir = "/", title = "Select file",
    #                 filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    # self.pic_input.insert('0', self.path)
    
    #buttons
    pic_button = tk.Button(text="Import Picture", bg=self.button_bg, command=self.pic_input)
    pic_button.grid(row=4, column=1)
    
    submit_button = tk.Button(text="Submit", bg=self.button_bg, command=self.user_input)
    submit_button.grid(row=20, column=1)
    
    clear_button = tk.Button(text="Clear", bg=self.button_bg, command=self.clear_button)
    clear_button.grid(row=50, column=1)
    
    exit_button = tk.Button(text="Exit", bg=self.button_bg, command=self.exit_button)
    exit_button.grid(row=70, column=1)
    

  # Clear button function
  def clear_button(self):
    self.breed_input.delete(0,tk.END)
    self.breed_validate.config(image='', text='')
    self.age_input.delete(0,tk.END)
    self.age_validate.config(image='', text='')
    self.gender_input.delete(0,tk.END)
    self.gender_validate.config(image='', text='')
    self.color_input.delete(0,tk.END)
    self.color_validate.config(image='', text='')
    return None
  
  # Exit button function
  def exit_button(self):
    self.window.destroy()

  def pic_input(self):
    self.pic_input = tk.Entry()
    self.path = filedialog.askopenfilename(initialdir = "/", title = "Select file",
                    filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    self.pic_input.insert('0', self.path)


  # Capture User Input
  def user_input(self):
    self.breed = self.breed_input.get()
    self.age = self.age_input.get()
    self.gender = self.gender_input.get()
    self.color = self.color_input.get()
    
      
    # Validate Breed letters only  
    if self.breed.isalpha():                            
        self.breed_validate.config(image=self.valid)         
    else:
      self.breed_validate.config(image='', text="Invalid Character",bg=self.window_bg,fg='red', font=('', 10, 'bold'))
   
    # Validate Age numbers only
    if self.age.isnumeric():                            
       self.age_validate.config(image=self.valid) 
    else:
       self.age_validate.config(image='', text="Invalid Character",bg=self.window_bg,fg='red', font=('', 10, 'bold'))

    # Validate Gender letters only
    if self.gender.isalpha():                       
       self.gender_validate.config(image=self.valid)
    else:
       self.gender_validate.config(image='', text="Invalid Character",bg=self.window_bg,fg='red', font=('', 10, 'bold'))
 
    # Validate Color letters only  
    if self.color.isalpha():              
       self.color_validate.config(image=self.valid)
    else:
       self.color_validate.config(image='', text="Invalid Character",bg=self.window_bg,fg='red', font=('', 10, 'bold'))
    
    # Write to file if all fields valid    
    if self.breed.isalpha():
      if self.age.isnumeric():
        if self.gender.isalpha():
          if self.color.isalpha():
            cat = Cat(self.breed,self.age,self.gender,self.color)
            with open('cats.txt','a',) as file:
              file.write(f"{cat.breed},{cat.age},{cat.gender},{cat.color},{cat.picture} \n")
          
    self.window.mainloop()
