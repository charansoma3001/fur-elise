import copy

class point():
    """rep"""
blank=point()
blank.x=3.9
blank.y=4.0

'(%g, %g)'%(blank.x, blank.y)

class rectangle:
    """rep"""
box=rectangle()
box.width=100.0
box.height=200.0
box.corner=point()
box.corner.x=3.0
box.corner.y=4.0

box2=copy.copy(box)
box3=copy.deepcopy(box)

print(box3.height is box.height)