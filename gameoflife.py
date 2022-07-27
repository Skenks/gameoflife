import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0


class Game:
    def __init__(self, n):
        self.n = n
        self.grid = np.random.choice([ON, OFF], n * n, p=[0.15, 0.85]).reshape(n, n)

    def update(self, frameNum, img, grid, n):
        updatedGrid = self.grid.copy()
        for i in range(n):
            for j in range(n):
                total = int((self.grid[i, (j - 1) % n] + self.grid[i, (j + 1) % n] +
                             self.grid[(i - 1) % n, j] + self.grid[(i + 1) % n, j] +
                             self.grid[(i - 1) % n, (j - 1) % n] + self.grid[(i - 1) % n, (j + 1) % n] +
                             self.grid[(i + 1) % n, (j - 1) % n] + self.grid[(i + 1) % n, (j + 1) % n]) / 255)

                if self.grid[i, j] == ON:
                    if (total < 2) or (total > 3):
                        updatedGrid[i, j] = OFF
                else:
                    if total == 3:
                        updatedGrid[i, j] = ON

        img.set_data(updatedGrid)
        self.grid[:] = updatedGrid[:]
        return img,

    def play(self):
        updateInterval = 1

        # set up animation
        fig, ax = plt.subplots()
        img = ax.imshow(self.grid, interpolation='nearest')
        ani = animation.FuncAnimation(fig, self.update, fargs=(img, self.grid, self.n, ),
                                      frames=self.n + 1,
                                      interval=updateInterval,
                                      save_count=50)
        plt.show()


game = Game(200)
game.play()
