# Mazes
A Python application for generating mazes and finding paths through them.
> **This application is a work in progress.** Features may change, and bugs may exist.

<img width="572" height="432" alt="Image" src="https://github.com/user-attachments/assets/18a409a5-3b67-485b-92d5-28a6e6952dc2" />
<img width="641" height="641" alt="Image" src="https://github.com/user-attachments/assets/8950e599-c664-4058-93d1-c413773374bb" />
<img width="641" height="641" alt="Image" src="https://github.com/user-attachments/assets/1ae916c4-8e57-440e-a10a-9337df329b1a" />
<img width="641" height="641" alt="Image" src="https://github.com/user-attachments/assets/9d304134-7ddb-47c3-8f6a-0282b3fad5ff" />

## How to use
- Choose a maze-generation algorithm.
- Choose the maze size, start position and goal position.
- Choose a maze-search algorithm.
- Click the **Maze** button to generate and display a maze.
- Click the **Search** button to run and display the selected search algorithm.
- Click the **Path** button to reconstruct and display the shortest path from the start to the goal.
- To save the generated image once it opens in Windows Photos app, go to Edit > Save Options.

## Requirements
- Python 3.10 or newer
- Pillow

## How to Run on Windows
- You can open the project in IDE and run gui/app.py
- Alternatively, open a terminal in the project root folder and run 'py -m gui.app'
- If needed, you can install the missing packages by running 'py -m pip install -r requirements.txt'

## Main sources

- [Mazes for Programmers](http://www.mazesforprogrammers.com/) by Jamis Buck
- [Python translation of parts of the book](https://github.com/crux888/mazes-for-programmers-python) by crux888
- [Pathfinding and algorithms](https://www.redblobgames.com/pathfinding/) by Amit Patel
