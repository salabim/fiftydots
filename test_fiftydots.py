import unittest

from textwrap import dedent

from fiftydots import grid, coordinates

def grid_to_str(grid, leftborder='<', rightborder='>'):
    result = ''
    for l in grid:
        result += leftborder + ("".join("*" if vl else " " for vl in l)) + rightborder + '\n'
    return result

class FiftdotsTest(unittest.TestCase):
    def test_grid_NonProportional_0(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=False, width=None, align='c')),
            dedent('''\
<                                                                       >
<      *                     *          *        *       *     *    *** >
<      *                     *         * *       *             *   *   *>
< ***  * **   ***         ** *  ***    *    **** * **   **     *   *   *>
<    * **  * *           *  ** *   *  ***  *   * **  *   *     *   *****>
< **** *   * *           *   * *****   *   *   * *   *   *     *   *   *>
<*   * *   * *   *       *   * *       *   *  ** *   *   *         *   *>
< ****  ***   ***         ****  ***    *    ** * *   *  ***    *   *   *>
<                                              *                        >
<                                           ***                         >
'''))

    def test_grid_NonProportional_1(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=False, width=80, align='c')),
            dedent('''\
<                                                                                >
<          *                     *          *        *       *     *    ***      >
<          *                     *         * *       *             *   *   *     >
<     ***  * **   ***         ** *  ***    *    **** * **   **     *   *   *     >
<        * **  * *           *  ** *   *  ***  *   * **  *   *     *   *****     >
<     **** *   * *           *   * *****   *   *   * *   *   *     *   *   *     >
<    *   * *   * *   *       *   * *       *   *  ** *   *   *         *   *     >
<     ****  ***   ***         ****  ***    *    ** * *   *  ***    *   *   *     >
<                                                  *                             >
<                                               ***                              >
'''))

    def test_grid_NonProportional_2(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=False, width=80, align='c')),
            dedent('''\
<                                                                                >
<          *                     *          *        *       *     *    ***      >
<          *                     *         * *       *             *   *   *     >
<     ***  * **   ***         ** *  ***    *    **** * **   **     *   *   *     >
<        * **  * *           *  ** *   *  ***  *   * **  *   *     *   *****     >
<     **** *   * *           *   * *****   *   *   * *   *   *     *   *   *     >
<    *   * *   * *   *       *   * *       *   *  ** *   *   *         *   *     >
<     ****  ***   ***         ****  ***    *    ** * *   *  ***    *   *   *     >
<                                                  *                             >
<                                               ***                              >
'''))

    def test_grid_NonProportional_3(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=False, width=80, align='c')),
            dedent('''\
<                                                                                >
<          *                     *          *        *       *     *    ***      >
<          *                     *         * *       *             *   *   *     >
<     ***  * **   ***         ** *  ***    *    **** * **   **     *   *   *     >
<        * **  * *           *  ** *   *  ***  *   * **  *   *     *   *****     >
<     **** *   * *           *   * *****   *   *   * *   *   *     *   *   *     >
<    *   * *   * *   *       *   * *       *   *  ** *   *   *         *   *     >
<     ****  ***   ***         ****  ***    *    ** * *   *  ***    *   *   *     >
<                                                  *                             >
<                                               ***                              >
'''))

    def test_grid_NonProportional_4(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=False, width=40, align='c')),
            dedent('''\
<                                        >
<             *          *        *      >
<             *         * *       *      >
<*         ** *  ***    *    **** * **   >
<         *  ** *   *  ***  *   * **  *  >
<         *   * *****   *   *   * *   *  >
< *       *   * *       *   *  ** *   *  >
<*         ****  ***    *    ** * *   *  >
<                               *        >
<                            ***         >
'''))

    def test_grid_NonProportional_5(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=False, width=40, align='c')),
            dedent('''\
<                                        >
<             *          *        *      >
<             *         * *       *      >
<*         ** *  ***    *    **** * **   >
<         *  ** *   *  ***  *   * **  *  >
<         *   * *****   *   *   * *   *  >
< *       *   * *       *   *  ** *   *  >
<*         ****  ***    *    ** * *   *  >
<                               *        >
<                            ***         >
'''))

    def test_grid_NonProportional_6(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=False, width=40, align='c')),
            dedent('''\
<                                        >
<             *          *        *      >
<             *         * *       *      >
<*         ** *  ***    *    **** * **   >
<         *  ** *   *  ***  *   * **  *  >
<         *   * *****   *   *   * *   *  >
< *       *   * *       *   *  ** *   *  >
<*         ****  ***    *    ** * *   *  >
<                               *        >
<                            ***         >
'''))

    def test_grid_NonProportional_7(self):
        self.assertEqual(
            grid_to_str(grid(s='', default=' ', intra=1, proportional=False, width=None, align='c')),
            dedent('''\
<>
<>
<>
<>
<>
<>
<>
<>
<>
<>
'''))

    def test_grid_NonProportional_8(self):
        self.assertEqual(
            grid_to_str(grid(s=' ', default=' ', intra=1, proportional=False, width=None, align='c')),
            dedent('''\
<     >
<     >
<     >
<     >
<     >
<     >
<     >
<     >
<     >
<     >
'''))

    def test_grid_Proportional_0(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=True, width=None, align='c')),
            dedent('''\
<                                                             >
<      *                  *         *        *      *  *  *** >
<      *                  *        * *       *         * *   *>
< ***  * **   ***      ** *  ***   *    **** * **  **  * *   *>
<    * **  * *        *  ** *   * ***  *   * **  *  *  * *****>
< **** *   * *        *   * *****  *   *   * *   *  *  * *   *>
<*   * *   * *   *    *   * *      *   *  ** *   *  *    *   *>
< ****  ***   ***      ****  ***   *    ** * *   * *** * *   *>
<                                          *                  >
<                                       ***                   >
'''))

    def test_grid_Proportional_1(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=True, width=80, align='c')),
            dedent('''\
<                                                                                >
<               *                  *         *        *      *  *  ***           >
<               *                  *        * *       *         * *   *          >
<          ***  * **   ***      ** *  ***   *    **** * **  **  * *   *          >
<             * **  * *        *  ** *   * ***  *   * **  *  *  * *****          >
<          **** *   * *        *   * *****  *   *   * *   *  *  * *   *          >
<         *   * *   * *   *    *   * *      *   *  ** *   *  *    *   *          >
<          ****  ***   ***      ****  ***   *    ** * *   * *** * *   *          >
<                                                   *                            >
<                                                ***                             >
'''))

    def test_grid_Proportional_2(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=True, width=80, align='c')),
            dedent('''\
<                                                                                >
<               *                  *         *        *      *  *  ***           >
<               *                  *        * *       *         * *   *          >
<          ***  * **   ***      ** *  ***   *    **** * **  **  * *   *          >
<             * **  * *        *  ** *   * ***  *   * **  *  *  * *****          >
<          **** *   * *        *   * *****  *   *   * *   *  *  * *   *          >
<         *   * *   * *   *    *   * *      *   *  ** *   *  *    *   *          >
<          ****  ***   ***      ****  ***   *    ** * *   * *** * *   *          >
<                                                   *                            >
<                                                ***                             >
'''))

    def test_grid_Proportional_3(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=True, width=80, align='c')),
            dedent('''\
<                                                                                >
<               *                  *         *        *      *  *  ***           >
<               *                  *        * *       *         * *   *          >
<          ***  * **   ***      ** *  ***   *    **** * **  **  * *   *          >
<             * **  * *        *  ** *   * ***  *   * **  *  *  * *****          >
<          **** *   * *        *   * *****  *   *   * *   *  *  * *   *          >
<         *   * *   * *   *    *   * *      *   *  ** *   *  *    *   *          >
<          ****  ***   ***      ****  ***   *    ** * *   * *** * *   *          >
<                                                   *                            >
<                                                ***                             >
'''))

    def test_grid_Proportional_4(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=True, width=40, align='c')),
            dedent('''\
<                                        >
<               *         *        *     >
<               *        * *       *     >
<   ***      ** *  ***   *    **** * **  >
<* *        *  ** *   * ***  *   * **  * >
<* *        *   * *****  *   *   * *   * >
<* *   *    *   * *      *   *  ** *   * >
<   ***      ****  ***   *    ** * *   * >
<                                *       >
<                             ***        >
'''))

    def test_grid_Proportional_5(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=True, width=40, align='c')),
            dedent('''\
<                                        >
<               *         *        *     >
<               *        * *       *     >
<   ***      ** *  ***   *    **** * **  >
<* *        *  ** *   * ***  *   * **  * >
<* *        *   * *****  *   *   * *   * >
<* *   *    *   * *      *   *  ** *   * >
<   ***      ****  ***   *    ** * *   * >
<                                *       >
<                             ***        >
'''))

    def test_grid_Proportional_6(self):
        self.assertEqual(
            grid_to_str(grid(s='abc defghi!A', default=' ', intra=1, proportional=True, width=40, align='c')),
            dedent('''\
<                                        >
<               *         *        *     >
<               *        * *       *     >
<   ***      ** *  ***   *    **** * **  >
<* *        *  ** *   * ***  *   * **  * >
<* *        *   * *****  *   *   * *   * >
<* *   *    *   * *      *   *  ** *   * >
<   ***      ****  ***   *    ** * *   * >
<                                *       >
<                             ***        >
'''))

    def test_grid_Proportional_7(self):
        self.assertEqual(
            grid_to_str(grid(s='', default=' ', intra=1, proportional=True, width=None, align='c')),
            dedent('''\
<>
<>
<>
<>
<>
<>
<>
<>
<>
<>
'''))

    def test_grid_Proportional_8(self):
        self.assertEqual(
            grid_to_str(grid(s=' ', default=' ', intra=1, proportional=True, width=None, align='c')),
            dedent('''\
<  >
<  >
<  >
<  >
<  >
<  >
<  >
<  >
<  >
<  >
'''))


if __name__ == "__main__":
    unittest.main(verbosity=2)    
