from audiovisual import theme
from resources import constants, tools

#the player
class Hero:
	def __init__(self):
		self.pos = tools.Vector2(constants.DEF_Px, constants.DEF_Py)
		self.direction = constants.STOP
		self.sprite = theme.sprite('default/hero.png', 0.4)
	
	def able_to_move_x(self, where):
		if where > 0:
			return self.pos.x < constants.SCREEN_SIZE[0] - constants.HERO_SIZE[0]
		return self.pos.x > 0

	def able_to_move_y(self, where):
		if where > 0:
			return self.pos.y < constants.SCREEN_SIZE[1] - constants.HERO_SIZE[1]	
		return self.pos.y > 0	

	#update position on screen
	def update(self, key, press):
		if press: #press button
			if key in constants.keys:
				self.direction = constants.keys[key] #change direction of movement
		else: #release button
			if key in constants.keys and constants.keys[key] == self.direction:
				self.direction = constants.STOP #stop movement

		#moving hero
		if self.direction in constants.move_x and self.able_to_move_x(constants.move_x[self.direction]):
			self.pos.x += constants.move_x[self.direction]
		elif self.direction in constants.move_y and self.able_to_move_y(constants.move_y[self.direction]):
			self.pos.y += constants.move_y[self.direction]