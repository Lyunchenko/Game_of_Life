import time
import gui
import generation as gn

def start_game(checked_cells):
	history = []
	generation = gn.Generation(checked_cells, gui, widht, height)
	while not (generation.get_count()==0 
				or generation in history):
		history.append(generation)
		generation = generation.get_next_generation()
		time.sleep(0.1)

if __name__ == '__main__':
	widht = 50
	height = 20
	gui = gui.GUI(start_game, widht, height)
	gui.create_window()
