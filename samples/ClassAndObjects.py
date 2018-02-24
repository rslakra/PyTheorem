#!/usr/bin/env python
class atom(object):
	def __init__(self, atno, x, y, z):
		self.atno = atno
		self.position = (x, y, z)
	def symbol(self):
		return Atno_to_Symbol[atno]
	def __repr__(self):
		return '%d %10.4f %10.4f %10.4f' %(self.atno, self.position[0], self.position[1], self.position[2])
