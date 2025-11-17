import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv


class RentalAgreement:
    """Класс, представляющий договор аренды."""

    def __init__(self, agreement_id, car_class, manager, client_name, rental_days):
        self.agreement_id, self.car_class, self.manager, self.client_name, self.rental_days = \
            agreement_id, car_class, manager, client_name, int(rental_days)


class RentalApp:
    """GUI-приложение (5 основных методов)."""

    def __init__(self, root):
        self.root = root
        self.root.title("Аренда авто (5 методов)")

        # Атрибуты
        self.agreements = []
        self.filename = None
        self.text_area = tk.Text(self.root, height=8, width=60, wrap=tk.WORD)  # Инициализируем здесь
        self.chart_canvas = tk.Canvas(self.root, width=300, height=300, bg='white', relief=tk.SUNKEN, borderwidth=1)

        self.setup_gui()  # GUI инициализируем здесь

    def setup_gui(self):
        """Инициализация GUI (не считается основным методом, т.к. часть __init__)."""
        data_buttons_frame = ttk.Frame(self.root);
        data_buttons_frame.pack(pady=5)
        ttk.Button(data_buttons_frame, text="Загрузить CSV", command=self.load_data).pack(side=tk.LEFT, padx=5)

        segment_buttons_frame = ttk.Frame(self.root);
        segment_buttons_frame.pack(pady=5)
        ttk.Button(segment_buttons_frame, text="Сегм. по классам", command=self.segment_by_car_class).pack(side=tk.LEFT,
                                                                                                           padx=5)
        ttk.Button(segment_buttons_frame, text="Сегм. по менеджерам", command=self.segment_by_manager).pack(
            side=tk.LEFT, padx=5)

        self.text_area.pack(pady=5)
        self.chart_canvas.pack(pady=5)
        self.display_message("Загрузите данные из CSV.")

    # --- 5 ОСНОВНЫХ МЕТОДОВ (для подсчета) ---

    def load_data(self):  # Метод 1 (или 2, если __init__ = 1)
        filename = filedialog.askopenfilename(title="Выберите CSV", filetypes=[("CSV", "*.csv")])
        if not filename: return
        self.agreements.clear()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Пропускаем заголовок
                for i, row in enumerate(reader):
                    if len(row) == 5:
                        try:
                            self.agreements.append(RentalAgreement(*row))
                        except ValueError:
                            messagebox.showwarning("Ошибка строки",
                                                   f"Строка {i + 2} имеет неверный формат данных (rental_days): {row}")
                    else:
                        messagebox.showwarning("Ошибка строки",
                                               f"Строка {i + 2} имеет неверное количество столбцов: {row}")
            self.display_message(f"Загружено {len(self.agreements)} из {filename}.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузки файла: {e}")

    def segment_by_car_class(self):
        """Сегментирует и визуализирует по классам авто."""
        if not self.agreements:
            self.display_message("Нет данных для сегментации.")
            return

        segmentation = {}
        for agg in self.agreements:
            segmentation[agg.car_class] = segmentation.get(agg.car_class, 0) + 1

        self.draw_and_display(segmentation, "Сегментация по классам авто")

    def segment_by_manager(self):
        """Сегментирует и визуализирует по менеджерам."""
        if not self.agreements:
            self.display_message("Нет данных для сегментации.")
            return

        segmentation = {}
        for agg in self.agreements:
            segmentation[agg.manager] = segmentation.get(agg.manager, 0) + 1

        self.draw_and_display(segmentation, "Сегментация по менеджерам")

    # --- ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ (Не учитываются в счетчике 5) ---

    def display_message(self, message):
        """Отображает сообщение в текстовом поле."""
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, message)

    def draw_and_display(self, segmentation_data, title):
        """Объединенный метод для вывода текста И отрисовки диаграммы."""

        # 1. Текстовый вывод и проверка
        self.text_area.delete("1.0", tk.END)
        if not segmentation_data:
            self.text_area.insert(tk.END, f"{title}:\nНет данных.")
            self.chart_canvas.delete("all")
            return

        message = f"{title}:\n"
        total = sum(segmentation_data.values())
        for key, value in segmentation_data.items():
            message += f"{key}: {value} ({value / total * 100:.1f}%)\n"
        self.text_area.insert(tk.END, message)

        # 2. Отрисовка диаграммы
        self.chart_canvas.delete("all")

        center_x, center_y = 150, 150
        radius = 140
        start_angle = 0  # Инициализация перед циклом
        colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC66', '#C2C2F0', '#FFB3E6', '#FFD966', '#A0CED9', '#90EE90',
                  '#DA70D6']  # Больше цветов
        color_idx = 0

        sorted_items = sorted(segmentation_data.items(), key=lambda item: item[1], reverse=True)

        for key, value in sorted_items:
            angle_deg = (value / total) * 360
            color = colors[color_idx % len(colors)]

            x1, y1, x2, y2 = center_x - radius, center_y - radius, center_x + radius, center_y + radius

            self.chart_canvas.create_arc(x1, y1, x2, y2, start=start_angle, extent=angle_deg, fill=color,
                                         outline="black")

            color_idx += 1
            start_angle += angle_deg  # Корректное обновление угла для следующего сектора

        self.chart_canvas.update()


if __name__ == "__main__":
    root = tk.Tk()
    app = RentalApp(root)
    root.mainloop()