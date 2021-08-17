
# PROJECT description: This is a scalable GUI project which can create numerical puzzle game board. Here User can define
# the size of the board ( technically matrix'' dimention).

from tkinter import *

# Define the puzzle game board  size.
SIZE=int(input("Please Define the Puzzle Board Size:  "))


class GameGUI:
    def __init__(self):
        self.__mainw=Tk()
        self.__mainw.option_add('*Font','Verdana 36')
        self.__slate_location=[None]
        self.__buttons=[None]
        self.__empty_slate_location=[SIZE,SIZE]
        button_number=1
        for row in range(1,SIZE+1):
            for col in range(1,SIZE+1):

                if button_number > (SIZE * SIZE) - 1:
                    break

                #Rapper Funtion (call to another function that another function get the parameter)

                def button_clicked(button_which_pressed=button_number):
                    self.move_slate_maybe(button_which_pressed)

                    #print(f'Button {button_which_pressed} was passed!!')

                new_button=Button(self.__mainw,text=button_number,width=5,height=2,command=button_clicked)
                new_button.grid(row=row,column=col)
                self.__slate_location.append([row, col])
                self.__buttons.append(new_button)

                button_number+=1
        self.__mainw.mainloop()




    def move_slate_maybe(self,button_number):
        #print(f"{button_number} {self.__slate_location[button_number]}")
        # self.__buttons[button_number].configure(text='?')
        button=self.__buttons[button_number]
        row,col=self.__slate_location[button_number]
        empty_row,empty_col=self.__empty_slate_location

        delta_y=abs(row-empty_row)
        delta_x=abs(col-empty_col)

        if (delta_y==1 and delta_x==0) or (delta_y==0 and delta_x==1) :
            button.grid(row=empty_row,column=empty_col)
            self.__empty_slate_location=[row,col]
            self.__slate_location[button_number]=[empty_row,empty_col]
        else:
            return





def main():
    GameGUI()


main()


