from tkinter import *


class GUI:

	def __init__(self, start_handler, widht, height):
		self.start_handler = start_handler
		self.widht = widht
		self.height = height
		self.checked_cells = [] # адреса выделенных клеток


	def create_window(self):
		root = Tk()
		root.title("Conway's Game of Life")

		# Область рисования
		SIZE = 20 # размер клетки
		self.c = Canvas(root, width=self.widht * SIZE, height=self.height * SIZE + 1)
		self.c.pack()
		for i in range(self.widht):
			for j in range(self.height):
				self.c.create_rectangle(i * SIZE, j * SIZE,
										i * SIZE + SIZE,
										j * SIZE + SIZE, fill='white')
		self.c.bind("<Button-1>", self._click_left)
		self.c.bind("<Button-3>", self._click_right)

		# Кнопка старт и ее обработчик
		self.btn = Button(root, text="Start", width=20, height=2, bg="green", fg="black")
		self.btn.bind("<Button-1>", self._click_start)
		self.btn.pack(fill = 'both')
		
		# Запуск GUI
		root.mainloop()


	def set_cell(self, address, value):
		''' address - координаты клетки в формате: [строка, столбец] или id
			value - True - выделить клетку, False - снять выделение'''
		ids = self._to_id(address)
		if value: color = "gray"
		else: color = "white"
		self.c.itemconfig(ids, fill=color)
		self.c.update()
		

	def _click_left(self, event):
		# Выделение клетки
		ids = self.c.find_withtag(CURRENT)[0]
		self.set_cell(ids, True)
		# Добавление в список
		address = self._to_address(ids)
		if address not in self.checked_cells:
			self.checked_cells.append(address)

	def _click_right(self, event):
		# Снятие выделения клетки
		ids = self.c.find_withtag(CURRENT)[0]  
		self.set_cell(ids, False)
		# Удаление из списка
		address = self._to_address(ids)
		if address in self.checked_cells:
			self.checked_cells.remove(address)

	def _click_start(self, event):
		self.start_handler(self.checked_cells)
		self.checked_cells = []
		self.btn.config(text="Clear board", bg="red")
		self.btn.bind("<Button-1>", self._click_clear)

	def _click_clear(self, event):
		for i in range(self.widht*self.height):
			self.set_cell(i, False)
		self.btn.config(text="Start", bg="green")
		self.btn.bind("<Button-1>", self._click_start)

	def _to_id(self, value):
		if type(value) == list:
			ids = value[1] * self.height + value[0] + 1
			return(ids)
		return(value)

	def _to_address(self, value):
		if type(value) == int:
			y = int((value-1)/self.height)
			x = (value-1) - y*self.height
			return([x,y])
		return(value)