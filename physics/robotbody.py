import Box2D as b2
import math

class RobotBody():

    width = 0.09
    height = 0.09
    grabber_width = 0.03
    grabber_height = 0.02
    density = 7.4
    grabber_density = 7.4

    def __init__(self, world, ID, body_position, heading=0):
        self.ID = ID
        self.body = world.CreateDynamicBody(position=body_position)
        ps = b2.b2PolygonShape()
        ps.SetAsBox(self.width/2, self.height/2)
        ps1 = b2.b2PolygonShape()
        ps1.SetAsBox(self.grabber_width/2, self.grabber_height/2,
                     b2.b2Vec2((-self.width/2 - self.grabber_width/2),
                               (self.height/2 - self.grabber_height/2)),0)
        ps2 = b2.b2PolygonShape()
        ps2.SetAsBox(self.grabber_width/2, self.grabber_height/2,
                     b2.b2Vec2((-self.width/2 - self.grabber_width/2),
                               (self.grabber_height/2 - self.height/2)),0)

        self.body.CreateFixture(shape=ps, density=self.density)
        self.body.CreateFixture(shape=ps1, density=self.grabber_density)
        self.body.CreateFixture(shape=ps2, density=self.grabber_density)

    # def set_linear_impulse(self, lws, rws, dt):
    #     theta = (rws-lws) * dt / self.width
    #     beta = self.body.angle + theta/2
    #     v0 = self.body.linearVelocity
    #     v1 = b2.b2Vec2((lws+rws) * math.cos(beta) / 2,
    #                    (lws+rws) * math.sin(beta) / 2)
    #     li = (v1-v0) * self.body.mass
    #     self.body.ApplyLinearImpulse(li, self.body.worldCenter, 1)
    #     return li

    # def set_angular_impulse(self, lws, rws, dt):
    #     next_angle = self.body.angularVelocity * dt
    #     desire_angle = (rws-lws) * dt  / self.width
    #     total_angle = desire_angle - next_angle
    #     if total_angle >= 0:
    #         total_angle %= 2 * math.pi
    #     else:
    #         total_angle %= -2 * math.pi
    #     desire_angular_velocity = total_angle / dt
    #     angular_impulse = self.body.inertia * desire_angular_velocity
    #     self.body.ApplyAngularImpulse(angular_impulse, 1)
    #     return angular_impulse

    def set_linear_impulse(self, v_t, v_r, dt):
        beta = self.body.angle + math.pi/2 + v_r*dt/2
        v0 = self.body.linearVelocity
        v1 = b2.b2Vec2(v_t * math.cos(beta), -v_t * math.sin(beta))
        print v1
        li = (v1-v0) * self.body.mass
        self.body.ApplyLinearImpulse(li, self.body.worldCenter, 1)
        return li

    def set_angular_impulse(self, v_t, v_r, dt):
        next_angle = self.body.angularVelocity * dt
        desire_angle = v_r * dt
        total_angle = desire_angle - next_angle
        if total_angle >= 0:
            total_angle %= 2 * math.pi
        else:
            total_angle %= -2 * math.pi
        desire_angular_velocity = total_angle / dt
        angular_impulse = self.body.inertia * desire_angular_velocity
        self.body.ApplyAngularImpulse(angular_impulse, 1)
        return angular_impulse

    def get_pos(self):
        return self.body.worldCenter

    def get_angle(self):
        return self.body.angle
