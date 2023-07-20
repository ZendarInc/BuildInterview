from ascii_shapes.pixel_ellipse import Ellipse
import unittest

class TestEllipseSolver(unittest.TestCase):
    def test_representative_example(self):
        expected_inner_coordinates = [
            (-14.1507258, -5.0000000),
            (-14.1252785, -6.0000000),
            (-14.0686103, -4.0000000),
            (-14.0000000, -6.8894094),
            (-14.0000000, -3.5531295),
            (-13.9769119, -7.0000000),
            (-13.8892531, -3.0000000),
            (-13.6821035, -8.0000000),
            (-13.6195872, -2.0000000),
            (-13.2640736, -1.0000000),
            (-13.2026033, -9.0000000),
            (-13.0000000, -9.3204576),
            (-13.0000000, -0.3761857),
            (-12.8252150, 0.0000000),
            (-12.4693817, -10.0000000),
            (-12.3038185, 1.0000000),
            (-12.0000000, -10.4705346),
            (-12.0000000, 1.5197869),
            (-11.6990769, 2.0000000),
            (-11.3316701, -11.0000000),
            (-11.0084877, 3.0000000),
            (-11.0000000, -11.2163946),
            (-11.0000000, 3.0115426),
            (-10.2275897, 4.0000000),
            (-10.0000000, -11.7294650),
            (-10.0000000, 4.2705086),
            (-9.3494501, 5.0000000),
            (-9.2683645, -12.0000000),
            (-9.0000000, -12.0809600),
            (-9.0000000, 5.3678993),
            (-8.3637477, 6.0000000),
            (-8.0000000, -12.3086134),
            (-8.0000000, 6.3414483),
            (-7.2551259, 7.0000000),
            (-7.0000000, -12.4351638),
            (-7.0000000, 7.2138944),
            (-6.0000624, 8.0000000),
            (-6.0000000, -12.4754204),
            (-6.0000000, 8.0000466),
            (-5.0000000, -12.4395037),
            (-5.0000000, 8.7100255),
            (-4.5603070, 9.0000000),
            (-4.0000000, -12.3345192),
            (-4.0000000, 9.3509367),
            (-3.0000000, -12.1654944),
            (-3.0000000, 9.9278075),
            (-2.8668303, 10.0000000),
            (-2.2546972, -12.0000000),
            (-2.0000000, -11.9359308),
            (-2.0000000, 10.4441395),
            (-1.0000000, -11.6481383),
            (-1.0000000, 10.9022427),
            (-0.7688636, 11.0000000),
            (0.0000000, -11.3034331),
            (0.0000000, 11.3034331),
            (0.7688636, -11.0000000),
            (1.0000000, -10.9022427),
            (1.0000000, 11.6481383),
            (2.0000000, -10.4441395),
            (2.0000000, 11.9359308),
            (2.2546972, 12.0000000),
            (2.8668303, -10.0000000),
            (3.0000000, -9.9278075),
            (3.0000000, 12.1654944),
            (4.0000000, -9.3509367),
            (4.0000000, 12.3345192),
            (4.5603070, -9.0000000),
            (5.0000000, -8.7100255),
            (5.0000000, 12.4395037),
            (6.0000000, -8.0000466),
            (6.0000000, 12.4754204),
            (6.0000624, -8.0000000),
            (7.0000000, -7.2138944),
            (7.0000000, 12.4351638),
            (7.2551259, -7.0000000),
            (8.0000000, -6.3414483),
            (8.0000000, 12.3086134),
            (8.3637477, -6.0000000),
            (9.0000000, -5.3678993),
            (9.0000000, 12.0809600),
            (9.2683645, 12.0000000),
            (9.3494501, -5.0000000),
            (10.0000000, -4.2705086),
            (10.0000000, 11.7294650),
            (10.2275897, -4.0000000),
            (11.0000000, -3.0115426),
            (11.0000000, 11.2163946),
            (11.0084877, -3.0000000),
            (11.3316701, 11.0000000),
            (11.6990769, -2.0000000),
            (12.0000000, -1.5197869),
            (12.0000000, 10.4705346),
            (12.3038185, -1.0000000),
            (12.4693817, 10.0000000),
            (12.8252150, 0.0000000),
            (13.0000000, 0.3761857),
            (13.0000000, 9.3204576),
            (13.2026033, 9.0000000),
            (13.2640736, 1.0000000),
            (13.6195872, 2.0000000),
            (13.6821035, 8.0000000),
            (13.8892531, 3.0000000),
            (13.9769119, 7.0000000),
            (14.0000000, 3.5531295),
            (14.0000000, 6.8894094),
            (14.0686103, 4.0000000),
            (14.1252785, 6.0000000),
            (14.1507258, 5.0000000)
        ]

        expected_outer_coordinates = [
            (-18.0838722, -5.0000000),
            (-18.0762111, -6.0000000),
            (-18.0178442, -4.0000000),
            (-18.0000000, -6.9162322),
            (-18.0000000, -3.8336181),
            (-17.9895478, -7.0000000),
            (-17.8820452, -3.0000000),
            (-17.8167257, -8.0000000),
            (-17.6792880, -2.0000000),
            (-17.5480359, -9.0000000),
            (-17.4114679, -1.0000000),
            (-17.1700487, -10.0000000),
            (-17.0796795, 0.0000000),
            (-17.0000000, -10.3677370),
            (-17.0000000, 0.2151006),
            (-16.6842807, 1.0000000),
            (-16.6635782, -11.0000000),
            (-16.2249136, 2.0000000),
            (-16.0000000, -11.9997884),
            (-16.0000000, 2.4443659),
            (-15.9998401, -12.0000000),
            (-15.7004835, 3.0000000),
            (-15.1323580, -13.0000000),
            (-15.1090953, 4.0000000),
            (-15.0000000, -13.1308952),
            (-15.0000000, 4.1726866),
            (-14.4479361, 5.0000000),
            (-14.0000000, -13.9827610),
            (-14.0000000, 5.6217663),
            (-13.9768560, -14.0000000),
            (-13.7130878, 6.0000000),
            (-13.0000000, -14.6453035),
            (-13.0000000, 6.8815227),
            (-12.8992373, 7.0000000),
            (-12.3454315, -15.0000000),
            (-12.0000000, -15.1657508),
            (-12.0000000, 7.9991839),
            (-11.9992280, 8.0000000),
            (-11.0033509, 9.0000000),
            (-11.0000000, -15.5725502),
            (-11.0000000, 9.0031972),
            (-10.0000000, -15.8843613),
            (-10.0000000, 9.9122223),
            (-9.8981766, 10.0000000),
            (-9.5383503, -16.0000000),
            (-9.0000000, -16.1141458),
            (-9.0000000, 10.7392207),
            (-8.6645188, 11.0000000),
            (-8.0000000, -16.2712731),
            (-8.0000000, 11.4935619),
            (-7.2735935, 12.0000000),
            (-7.0000000, -16.3627050),
            (-7.0000000, 12.1822077),
            (-6.0000000, -16.3937068),
            (-6.0000000, 12.8104233),
            (-5.6789242, 13.0000000),
            (-5.0000000, -16.3682961),
            (-5.0000000, 13.3822266),
            (-4.0000000, -16.2895361),
            (-4.0000000, 13.9006805),
            (-3.7962350, 14.0000000),
            (-3.0000000, -16.1597323),
            (-3.0000000, 14.3680906),
            (-2.0966452, -16.0000000),
            (-2.0000000, -15.9805650),
            (-2.0000000, 14.7861372),
            (-1.4376233, 15.0000000),
            (-1.0000000, -15.7531787),
            (-1.0000000, 15.1559648),
            (0.0000000, -15.4782392),
            (0.0000000, 15.4782392),
            (1.0000000, -15.1559648),
            (1.0000000, 15.7531787),
            (1.4376233, -15.0000000),
            (2.0000000, -14.7861372),
            (2.0000000, 15.9805650),
            (2.0966452, 16.0000000),
            (3.0000000, -14.3680906),
            (3.0000000, 16.1597323),
            (3.7962350, -14.0000000),
            (4.0000000, -13.9006805),
            (4.0000000, 16.2895361),
            (5.0000000, -13.3822266),
            (5.0000000, 16.3682961),
            (5.6789242, -13.0000000),
            (6.0000000, -12.8104233),
            (6.0000000, 16.3937068),
            (7.0000000, -12.1822077),
            (7.0000000, 16.3627050),
            (7.2735935, -12.0000000),
            (8.0000000, -11.4935619),
            (8.0000000, 16.2712731),
            (8.6645188, -11.0000000),
            (9.0000000, -10.7392207),
            (9.0000000, 16.1141458),
            (9.5383503, 16.0000000),
            (9.8981766, -10.0000000),
            (10.0000000, -9.9122223),
            (10.0000000, 15.8843613),
            (11.0000000, -9.0031972),
            (11.0000000, 15.5725502),
            (11.0033509, -9.0000000),
            (11.9992280, -8.0000000),
            (12.0000000, -7.9991839),
            (12.0000000, 15.1657508),
            (12.3454315, 15.0000000),
            (12.8992373, -7.0000000),
            (13.0000000, -6.8815227),
            (13.0000000, 14.6453035),
            (13.7130878, -6.0000000),
            (13.9768560, 14.0000000),
            (14.0000000, -5.6217663),
            (14.0000000, 13.9827610),
            (14.4479361, -5.0000000),
            (15.0000000, -4.1726866),
            (15.0000000, 13.1308952),
            (15.1090953, -4.0000000),
            (15.1323580, 13.0000000),
            (15.7004835, -3.0000000),
            (15.9998401, 12.0000000),
            (16.0000000, -2.4443659),
            (16.0000000, 11.9997884),
            (16.2249136, -2.0000000),
            (16.6635782, 11.0000000),
            (16.6842807, -1.0000000),
            (17.0000000, -0.2151006),
            (17.0000000, 10.3677370),
            (17.0796795, 0.0000000),
            (17.1700487, 10.0000000),
            (17.4114679, 1.0000000),
            (17.5480359, 9.0000000),
            (17.6792880, 2.0000000),
            (17.8167257, 8.0000000),
            (17.8820452, 3.0000000),
            (17.9895478, 7.0000000),
            (18.0000000, 3.8336181),
            (18.0000000, 6.9162322),
            (18.0178442, 4.0000000),
            (18.0762111, 6.0000000),
            (18.0838722, 5.0000000)
        ]

        outer_a = 20
        outer_b = 14
        theta = 0.64
        inner_a = 16
        inner_b = 10

        min_x = -20
        max_x = 20
        min_y = -20
        max_y = 20

        inner_ellipse = Ellipse(inner_a, inner_b, theta)
        outer_ellipse = Ellipse(outer_a, outer_b, theta)

        inner_set = set()
        for x in range(min_x, max_x + 1, 1):
            y_pair = inner_ellipse.solve_y(x)
            if y_pair:
                inner_set.add((x, y_pair[0]))
                inner_set.add((x, y_pair[1]))

        for y in range(min_y, max_y + 1, 1):
            x_pair = inner_ellipse.solve_x(y)
            if x_pair:
                inner_set.add((x_pair[0], y))
                inner_set.add((x_pair[1], y))

        outer_set = set()
        for x in range(min_x, max_x + 1, 1):
            y_pair = outer_ellipse.solve_y(x)
            if y_pair:
                outer_set.add((x, y_pair[0]))
                outer_set.add((x, y_pair[1]))

        for y in range(min_y, max_y + 1, 1):
            x_pair = outer_ellipse.solve_x(y)
            if x_pair:
                outer_set.add((x_pair[0], y))
                outer_set.add((x_pair[1], y))

        inner_list = list(inner_set)
        inner_list.sort()

        self.assertEqual(len(inner_list), len(expected_inner_coordinates))
        for i in range(len(inner_list)):
            self.assertAlmostEqual(inner_list[i][0], expected_inner_coordinates[i][0])
            self.assertAlmostEqual(inner_list[i][1], expected_inner_coordinates[i][1])

        outer_list = list(outer_set)
        outer_list.sort()

        self.assertEqual(len(outer_list), len(expected_outer_coordinates))
        for i in range(len(outer_list)):
            self.assertAlmostEqual(outer_list[i][0], expected_outer_coordinates[i][0])
            self.assertAlmostEqual(outer_list[i][1], expected_outer_coordinates[i][1])

if __name__ == '__main__':
    unittest.main()

