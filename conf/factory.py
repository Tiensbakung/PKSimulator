import behaviour
import coord
import physics
import ui

def create_ball(name, position, world):
    body = physics.BallBody(world, name, position)
    r = int(body.radius*coord.bg_ratio)
    size = 4 * r, 4 * r
    sprite = ui.BallSprite(name, size, coord.b2g_pos(position))
    return body, sprite

def create_playground(world):
    lwall = create_wall(world, (-1, -30.55), (1, 30.5))
    rwall = create_wall(world, (69.66, -30.55), (1, 30.5))
    twall = create_wall(world, (34.33, 1), (34.3, 1))
    bwall = create_wall(world, (34.33, -62.1), (34.3, 1))
    return lwall, rwall, twall, bwall

def create_robot(ID, position, heading, world, leader, role, team):
    body = physics.RobotBody(world, ID, position, heading)
    size = 2*int(body.width*coord.bg_ratio), 2*int(body.height*coord.bg_ratio)
    color = (255, 0, 0) if team == 'red' else (0, 0, 255)
    sprite = ui.RobotSprite(ID, color, size, coord.b2g_pos(position),
                            coord.b2g_angle(heading))
    role = behaviour.RobotRole(ID, leader, role, team)
    return body, sprite, role

def create_wall(world, pos, (hw, hh)):
    wall = world.CreateStaticBody(position=pos)
    wall.CreatePolygonFixture(box=(hw,hh), density=0, restitution=0.9)
    return wall
