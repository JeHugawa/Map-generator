from tkinter import ttk, constants


class MainView:
    def __init__(self, root):
        super().__init__()
        self._root = root
        self._seed_entry = None

    
        self._frame = ttk.Frame(master=self._root)

        self._random_seed_field()
        self._generate_button()

    def _random_seed_field(self):
        seed_label = ttk.Label(text='Random Seed')
        self._seed_entry = ttk.Entry()

        seed_label.grid(row = 2)
        self._seed_entry.grid(row = 3)



    def _generate_button(self):
        generate_button = ttk.Button(text='Generate')

        generate_button.grid(padx=5, pady=5,sticky=constants.N)
    
