import Box2D as b2

class BallBody:

    def __init__(self, world, name, pos, radius=0.022, density=1.0):
        self.name = name
        self.body = world.CreateDynamicBody(position=pos, linearDamping=1,
                                            angulardamping=1)
        ps = b2.b2CircleShape(radius=radius)
        self.body.CreateFixture(shape=ps, density=density)
        self.radius = radius
        self.body

    def get_pos(self):
        return self.body.worldCenter

    def get_angle(self):
        return self.body.angle
