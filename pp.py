import tkinter as tk
from tkinter import ttk

class FullscreenApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        
        # История нажатий кнопок
        self.button_history = []
        
        # Чтение названий из файла для всех блоков
        self.blocks_data = []  # Список для хранения данных всех блоков
        try:
            with open('Abaddon.txt', 'r', encoding='utf-8') as file:
                all_lines = file.readlines()
                # Разбиваем на блоки по 30 строк
                for block_start in range(0, 120, 30):
                    block_names = []
                    block_values = []
                    for line in all_lines[block_start:block_start + 30]:
                        parts = line.strip().split()
                        # Проверяем, что строка содержит как минимум 2 части
                        if len(parts) >= 2:
                            name = parts[0].strip('"')
                            value = parts[1]
                            block_names.append(name)
                            block_values.append(value)
                        else:
                            # Если строка некорректная, добавляем значения по умолчанию
                            block_names.append(f"Name{len(block_names)+1}")
                            block_values.append("0")
                    
                    # Дополняем блок до 30 элементов, если строк меньше
                    while len(block_names) < 30:
                        block_names.append(f"Name{len(block_names)+1}")
                        block_values.append("0")
                        
                    self.blocks_data.append((block_names, block_values))
        except FileNotFoundError:
            print("Файл Abaddon.txt не найден")
            # Создаем пустые блоки данных
            for _ in range(4):
                block_names = [f"Name{i+1}" for i in range(30)]
                block_values = ["0" for _ in range(30)]
                self.blocks_data.append((block_names, block_values))
        
        # Создаем главный контейнер
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        self.show_main_page()
        
        # Привязываем клавишу Escape для выхода
        self.root.bind('<Escape>', lambda e: self.root.destroy())
    
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_main_page(self):
        self.clear_frame()
        # Сбрасываем историю при возврате на главную
        self.button_history = []
        
        title_label = ttk.Label(
            self.main_frame, 
            text="Антончик дота про/ carry mid/ solo mid/ 10000 mmr",
            font=('Helvetica', 24)
        )
        title_label.pack(pady=20)
        
        # Создаем фрейм для кнопок, чтобы они были одинакового размера
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(pady=10)
        
        # Задаем одинаковую ширину для всех кнопок
        button_width = 20
        
        description_button = ttk.Button(
            buttons_frame,
            text="Описание приложения",
            command=self.show_description,
            width=button_width
        )
        description_button.pack(pady=10)
        
        authors_button = ttk.Button(
            buttons_frame,
            text="Авторы",
            command=self.show_authors,
            width=button_width
        )
        authors_button.pack(pady=10)

        support_button = ttk.Button(
            buttons_frame,
            text="Поддержать команду",
            command=self.show_support,
            width=button_width
        )
        support_button.pack(pady=10)
        
        mode_button = ttk.Button(
            buttons_frame,
            text="Выбор режима",
            command=self.show_mode_selection,
            width=button_width
        )
        mode_button.pack(pady=10)
        
        next_page_button = ttk.Button(
            buttons_frame,
            text="Перейти к пикам",
            command=self.show_windows_page,
            width=button_width
        )
        next_page_button.pack(pady=10)
        
        exit_button = ttk.Button(
            buttons_frame,
            text="Выход",
            command=self.root.destroy,
            width=button_width
        )
        exit_button.pack(pady=10)

    def show_description(self):
        self.clear_frame()
        
        title_label = ttk.Label(
            self.main_frame, 
            text="Описание приложения",
            font=('Helvetica', 20)
        )
        title_label.pack(pady=20)
        
        description_text = tk.Text(
            self.main_frame,
            height=10,
            width=50,
            wrap=tk.WORD,
            font=('Helvetica', 12)
        )
        description_text.pack(pady=20, padx=50)
        
        try:
            with open('Описание.txt', 'r', encoding='utf-8') as file:
                description = file.read()
                description_text.insert('1.0', description)
        except FileNotFoundError:
            description_text.insert('1.0', "Файл с описанием не найден.")
        
        description_text.config(state='disabled')
        
        back_button = ttk.Button(
            self.main_frame,
            text="Вернуться на главную",
            command=self.show_main_page
        )
        back_button.pack(pady=20)

    def show_authors(self):
        self.clear_frame()
        
        title_label = ttk.Label(
            self.main_frame, 
            text="Авторы",
            font=('Helvetica', 20)
        )
        title_label.pack(pady=20)
        
        authors_text = tk.Text(
            self.main_frame,
            height=10,
            width=50,
            wrap=tk.WORD,
            font=('Helvetica', 12)
        )
        authors_text.pack(pady=20, padx=50)
        
        try:
            with open('Авторы.txt', 'r', encoding='utf-8') as file:
                authors = file.read()
                authors_text.insert('1.0', authors)
        except FileNotFoundError:
            authors_text.insert('1.0', "Файл со списком авторов не найден.")
        
        authors_text.config(state='disabled')
        
        back_button = ttk.Button(
            self.main_frame,
            text="Вернуться на главную",
            command=self.show_main_page
        )
        back_button.pack(pady=20)

    def show_support(self):
        self.clear_frame()
        
        title_label = ttk.Label(
            self.main_frame, 
            text="Поддержать команду",
            font=('Helvetica', 20)
        )
        title_label.pack(pady=20)
        
        support_text = tk.Text(
            self.main_frame,
            height=10,
            width=50,
            wrap=tk.WORD,
            font=('Helvetica', 12)
        )
        support_text.pack(pady=20, padx=50)
        
        try:
            with open('Поддержка.txt', 'r', encoding='utf-8') as file:
                support = file.read()
                support_text.insert('1.0', support)
        except FileNotFoundError:
            support_text.insert('1.0', "Файл с информацией о поддержке не найден.")
        
        support_text.config(state='disabled')
        
        back_button = ttk.Button(
            self.main_frame,
            text="Вернуться на главную",
            command=self.show_main_page
        )
        back_button.pack(pady=20)

    def show_mode_selection(self):
        self.clear_frame()
        
        title_label = ttk.Label(
            self.main_frame, 
            text="Выберите режим",
            font=('Helvetica', 24)
        )
        title_label.pack(pady=20)
        
        # Создаем фрейм для кнопок, чтобы они были одинакового размера
        buttons_frame = ttk.Frame(self.main_frame)
        buttons_frame.pack(pady=10)
        
        # Задаем одинаковую ширину для всех кнопок
        button_width = 20
        
        beer_button = ttk.Button(
            buttons_frame,
            text="Легкие персонажи",
            width=button_width
        )
        beer_button.pack(pady=10)
        
        girl_button = ttk.Button(
            buttons_frame,
            text="Сложные персонажи",
            width=button_width
        )
        girl_button.pack(pady=10)

        dynamics_button = ttk.Button(
            buttons_frame,
            text="Активные персонажи",
            width=button_width
        )
        dynamics_button.pack(pady=10)
        
        long_game_button = ttk.Button(
            buttons_frame,
            text="Долгая игра",
            width=button_width
        )
        long_game_button.pack(pady=10)
        
        back_button = ttk.Button(
            buttons_frame,
            text="Вернуться на главную",
            command=self.show_main_page,
            width=button_width
        )
        back_button.pack(pady=10)

    def create_block(self, parent_frame, block_index, row_start):
        block_frame = ttk.Frame(parent_frame)
        block_frame.grid(row=row_start, column=0, pady=(20 if row_start > 0 else 0))
        
        block_frame.grid_rowconfigure((0, 1, 2), weight=0)
        block_frame.grid_columnconfigure(tuple(range(10)), weight=1)
        
        names, values = self.blocks_data[block_index]
        
        for row in range(3):
            for col in range(10):
                idx = row * 10 + col
                if idx < len(names):
                    value = float(values[idx])
                    if value > 52.00:
                        border_color = 'green'
                    elif value < 49.00:
                        border_color = 'red'
                    else:
                        border_color = 'black'
                    
                    window_frame = tk.Frame(
                        block_frame, 
                        relief='solid', 
                        borderwidth=2,
                        highlightthickness=1,
                        highlightbackground=border_color
                    )
                    window_frame.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
                    
                    text_widget = tk.Text(window_frame, height=3, width=12)
                    text_widget.pack(expand=True, fill='both', padx=1, pady=1)
                    text_widget.insert('1.0', f'"{names[idx]}"\n{values[idx]}')
                    text_widget.tag_configure("center", justify='center')
                    text_widget.tag_add("center", "1.0", "end")
                    text_widget.config(state='disabled')
                    
                    text_widget.bind('<Button-1>', 
                        lambda e, num=idx, block=block_index: self.window_click(num, block))
        
        return block_frame
    
    def show_windows_page(self):
        self.clear_frame()
        
        history_frame = ttk.Frame(self.main_frame)
        history_frame.pack(fill='x', padx=2, pady=(0, 2))
        
        history_frame.grid_columnconfigure(tuple(range(5)), weight=1)
        
        self.history_windows = []
        for i in range(5):
            window_frame = ttk.Frame(history_frame, relief='solid', borderwidth=1)
            window_frame.grid(row=0, column=i, padx=2, pady=2, sticky='nsew')
            
            label_text = f"Пик {i+1}" if i < 4 else "Предсказание"
            label = ttk.Label(window_frame, text=label_text)
            
            if i == 0 or i == 3:  # Пик 1 и Пик 4
                label.configure(foreground='green')
            elif i == 1 or i == 2:  # Пик 2 и Пик 3
                label.configure(foreground='red')
                
            label.pack()
            
            text_widget = tk.Text(window_frame, height=3, width=15)
            text_widget.pack(expand=True, fill='both', padx=1, pady=1)
            text_widget.tag_configure("center", justify='center')
            text_widget.config(state='disabled')
            self.history_windows.append(text_widget)
        
        all_blocks_frame = ttk.Frame(self.main_frame)
        all_blocks_frame.pack(fill='both', expand=True)
        
        for i in range(4):
            self.create_block(all_blocks_frame, i, i * 4)
        
        back_button = ttk.Button(
            self.main_frame,
            text="Вернуться на главную",
            command=self.show_main_page
        )
        back_button.pack(pady=10)
    
    def window_click(self, window_num, block_index):
        if len(self.button_history) < 4:
            self.button_history.append((block_index, window_num))
            self.update_history_windows()
    
    def update_history_windows(self):
        for window in self.history_windows:
            window.config(state='normal')
            window.delete(1.0, tk.END)
            window.config(state='disabled')
        
        for i, (block_index, window_num) in enumerate(self.button_history):
            if i < 4:
                window = self.history_windows[i]
                window.config(state='normal')
                window.delete(1.0, tk.END)
                window.insert('1.0', self.blocks_data[block_index][0][window_num])
                window.tag_add("center", "1.0", "end")
                window.config(state='disabled')
        
        if len(self.button_history) == 4:
            green_values = [float(self.blocks_data[block][1][num]) 
                          for block, num in [self.button_history[0], self.button_history[3]]]
            red_values = [float(self.blocks_data[block][1][num]) 
                         for block, num in [self.button_history[1], self.button_history[2]]]
            
            green_avg = sum(green_values) / 2
            red_avg = sum(red_values) / 2
            
            difference = abs(green_avg - red_avg) + 50
            
            result_window = self.history_windows[4]
            result_window.config(state='normal')
            result_window.delete(1.0, tk.END)
            if green_avg > red_avg:
                result_window.insert('1.0', f"Зеленые\n{difference:.2f}")
            else:
                result_window.insert('1.0', f"Красные\n{difference:.2f}")
            result_window.tag_add("center", "1.0", "end")
            result_window.config(state='disabled')
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FullscreenApp()
    app.run()
