# Mazes
A Python application for generating mazes and finding paths through them.
> **This application is a work in progress.** Features may change, and bugs may exist.

<img width="459" height="347" alt="Image" src="https://github.com/user-attachments/assets/ef49bb5b-8f28-4295-80e7-78cd944e1c79" />
<img width="502" height="552" alt="Image" src="https://github.com/user-attachments/assets/3c44aadb-283a-4ebc-a21d-30ca66ca4014" />
<img width="502" height="552" alt="Image" src="https://github.com/user-attachments/assets/0c234b6c-d775-466a-bc77-8aa40704ca6a" />
<img width="502" height="552" alt="Image" src="https://github.com/user-attachments/assets/40157c84-808f-4fbb-a6d1-2476f1945737" />

## How to use
- Choose a maze-generation algorithm.
- Choose the maze size, start position and goal position.
- Choose a maze-search algorithm.
- Click the **Maze** button to generate and display a maze.
- Click the **Search** button to run and display the selected search algorithm.
- Click the **Path** button to reconstruct and display the shortest path from the start to the goal.
- To save the generated image once it opens, go to File > Save As.

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
