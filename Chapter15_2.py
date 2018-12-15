from Chapter15_1 import point


class rectangle(object):
    def __init__(self, W, H, x, y):
        '''Represent a rectangle in 2D space
        which has Width <int> and Height <int>
        and a Corner point <Point>.'''
        self.W = W
        self.H = H
        self.corner = point(x, y)

    def show_rectangle(self):
        '''Show rectangle detail'''
        print('Width : ', self.W)
        print('Height : ', self.H)
        print('Corner:')
        self.corner.showCor()


def rec_center(rec_in):
    '''Find center point <point> of a rectangle <rectangle>'''
    cen_x = rec_in.corner.x + (rec_in.W) / 2
    cen_y = rec_in.corner.y + (rec_in.H) / 2
    rec_in.center = point(cen_x, cen_y)


def rec_grow(rec_in, dW, dH):
    '''add dW<f> and dH<f> to Rec_in dimension <rectangle>'''
    rec_in.W += dW
    rec_in.H += dH


def rec_move(rec_in, dx, dy):
    '''Move rec_in <rectangle> by adding
    dx<f> and dy<f> to corner <point>'''
    rec_in.corner.x += dx
    rec_in.corner.y += dy


def rec_move_to_newRec(rec_in, dx, dy):
    '''Move rec_in <rectangle> by adding
    dx<f> and dy<f> to corner <point> but
    this time create new rectangle
    not touch the input one'''
    from copy import deepcopy
    rec_out = deepcopy(rec_in)
    rec_out.corner.x += dx
    rec_out.corner.y += dy
    return rec_out


if __name__ == '__main__':
    R = rectangle(100, 200, 0, 0)
    R.show_rectangle()
    rec_grow(R, 50, 100)
    R.show_rectangle()
    rec_move(R, 2, 3)
    R.show_rectangle()
    T = rec_move_to_newRec(R, 4, 5)
    T.show_rectangle()
    R.show_rectangle()
