class point():
    '''point class'''

class rectangle:
    '''rectangle area code'''

box = rectangle()
box.length = 100
box.width = 200
box.corner = point()
box.corner.x = 20
box.corner.y = 30

def area(l, w, c_x, c_y):
    mainLength = l - c_x
    mainWidth = w - c_y
    area = mainLength*mainWidth
    print('Area is: ' + str(area))

area(box.length, box.width, box.corner.x, box.corner.y)

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


def find_center(rect):
    p = point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.length/2
    return p

center = find_center(box)
print_point(center)