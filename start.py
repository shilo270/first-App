import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 1
        self.row_force_default = True
        self.row_default_height = 150
        self.col_force_default = True
        self.col_default_width = 500

        # create a second grid on top
        self.top_grid = GridLayout(
            # row_force_default=True,
            # row_default_height=100,
            # col_force_default = True,
            # col_default_width=200,

        )
        self.top_grid.cols = 2

        # add widgets
        self.top_grid.add_widget(Label(
            text="Name: ",
            # font_size=32,
            # size_hint_y=None,
            # height=50,
            # size_hint_x=None,
            # width=400
        ))
        # add input box
        self.name = TextInput(
            multiline=False,
            font_size=32,
            # size_hint_y=None,
            # height=50,
            # size_hint_x=None,
            # width=400
        )
        self.top_grid.add_widget(self.name)


        self.top_grid.add_widget(Label(
            text="favorite pizza: ",
            font_size=32,
            # size_hint_y=None,
            # height=50,
            # size_hint_x=None,
            # width=400
        ))
        self.pizza = TextInput(
            multiline=False,
            font_size=32,
            # size_hint_y=None,
            # height=50,
            # size_hint_x=None,
            # width=400
        )
        self.top_grid.add_widget(self.pizza)

        # add top grid to App
        self.add_widget(self.top_grid)

        # create submit button
        self.submit = Button(
            text="submit",
            font_size=32,
            # size_hint_y = None,
            # height=50,
            # size_hint_x = None,
            # width = 400
        )
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text

        #print(f'hello {name}, you like {pizza}')
        self.add_widget(Label(text=f'hello {name}, you like {pizza}'))
        self.name.text = ""
        self.pizza.text = ""

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()