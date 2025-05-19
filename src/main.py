from window import Window
from maze import Maze


def main():
    width = 1700
    height = 950
    test_size = 50
    padding = test_size // 2
    win = Window(width, height)

    numrows = (width - test_size) // test_size
    numcols = (height - test_size) // test_size
    print(numrows)
    print(numcols)

    test_maze = Maze(
        padding,
        padding,
        numrows,
        numcols,
        test_size,
        test_size,
        win,
    )
    win.wait_for_close()


main()
