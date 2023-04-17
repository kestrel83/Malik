import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the grid
N = 500

# Create the initial grid with random values
grid = np.random.choice([0, 1], size=(N, N))

# Define the update function for each frame of the animation
def update(frame_num, grid, img):
    # Copy the current grid to a new grid to update
    new_grid = grid.copy()

    # Iterate over every cell in the grid
    for i in range(N):
        for j in range(N):
            # Count the number of neighbors that are alive
            neighbors = (
                grid[(i-1) % N, (j-1) % N]
                + grid[(i-1) % N, j]
                + grid[(i-1) % N, (j+1) % N]
                + grid[i, (j-1) % N]
                + grid[i, (j+1) % N]
                + grid[(i+1) % N, (j-1) % N]
                + grid[(i+1) % N, j]
                + grid[(i+1) % N, (j+1) % N]
            )

            # Apply the rules of the game
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    # Update the grid and the image
    grid[:] = new_grid[:]
    img.set_data(grid)

    return img

# Create the animation figure
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation="nearest")

# Define the animation object
ani = animation.FuncAnimation(fig, update, fargs=(grid, img), frames=100, interval=100, save_count=50)

# Show the animation
plt.show()
