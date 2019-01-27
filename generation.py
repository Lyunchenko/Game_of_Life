

class Generation:

	def __init__(self, checked_cells, gui, widht, height):
		self.widht = widht
		self.height = height
		self.gui = gui
		self.generation = checked_cells

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return(self.generation == other.generation)
		else:
			return(False)


	def get_count(self):
		return(len(self.generation))

	def get_next_generation(self):
		self.next_generation = []
		self.list_check = []
		for cell in self.generation:
			if cell not in self.list_check:
				self._check_cell(cell)
		return(Generation(self.next_generation, self.gui, self.widht, self.height))


	def _check_cell(self, cell):

		life = True if cell in self.generation else False
		neighbors = self._get_neighbors(cell)
		count_life_neighbors = self._count_life(neighbors)
				
		# Переход в следующеее поколение
		if ((count_life_neighbors == 3)
			or (life and count_life_neighbors == 2)):
			self.next_generation.append(cell)
			self.gui.set_cell(cell, True)
		else: self.gui.set_cell(cell, False)

		self.list_check.append(cell)

		# Рекурсивная проверка для соседей живой клетки
		if life:
			for neighbor in neighbors:
				if neighbor not in self.list_check:
					self._check_cell(neighbor)


	def _get_neighbors(self, cell):
		neighbors = []
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i==j==0: continue
				
				x = i + cell[0]
				if x<0: x = self.height-1
				elif x>=self.height: x=0

				y = j + cell[1]
				if y<0: y = self.widht-1
				elif y>=self.widht: y=0

				neighbors.append([x, y])
		return(neighbors)


	def _count_life(self, cells):
		count = 0
		for cell in cells:
			if cell in self.generation:
				count += 1
		return(count)