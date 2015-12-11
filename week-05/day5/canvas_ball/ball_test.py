import unittest
from ball import Ball

class TestBall(unittest.TestCase):
    def test_existence(self):
        ball = Ball((40, 50), (10, 10), 10)

    def test_ball_parameters(self):
        ball = Ball((40, 50), (10, 10), 10)
        self.assertEqual(ball.pos, (40, 50))
        self.assertEqual(ball.size, (20, 20))
        self.assertEqual(ball.velocity, (10, 10))

    def test_get_bounding_box(self):
        ball = Ball((40, 50), (10, 10), 10)
        bbox = ball.get_bbox()
        self.assertEqual(bbox, (30, 40, 50, 60))

    def test_move(self):
        ball = Ball((40, 50), (10, 10), 10)
        ball.move()
        self.assertEqual(ball.pos, (50, 60))

unittest.main()
