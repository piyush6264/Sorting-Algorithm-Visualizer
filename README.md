# Sorting-Algorithm-Visualizer

A Python application that visualizes the sorting process of different algorithms, providing an interactive way to understand the mechanics of sorting algorithms like Bubble Sort, Merge Sort, and Quick Sort.

**Features**

Algorithms Supported: Visualizes Bubble Sort, Merge Sort, and Quick Sort.
Color-coded Visualization:
Green for sorted elements.
Red for unsorted or active elements during comparisons.
Intuitive GUI: Built with Tkinter, the GUI allows users to:
Select a sorting algorithm.
Start the sorting process with visual feedback.
Getting Started
Prerequisites
Python 3.x installed on your system.
Required Libraries:
tkinter: For the GUI (included with Python on most systems).
time: For adding delay in visualization.
random: For generating random data sets.

**Installation**

Clone or download this repository to your local machine.
Open a terminal or command prompt.
Navigate to the directory containing the project files.
Running the Application
To run the visualizer, execute the following command:

python sorting_visualizer.py
Usage
Select an Algorithm: Choose from Bubble Sort, Merge Sort, or Quick Sort in the dropdown menu.
Start Sorting: Press the "Start" button to initiate the visualization.
Observe the Sorting Process: The visualization will show each algorithm step-by-step, with active comparisons in red and sorted elements in green.

**Code Structure**

sorting_visualizer.py: Main file containing sorting algorithms and GUI code.
Sorting Algorithms: Functions for Bubble Sort, Merge Sort, and Quick Sort, each designed to visually illustrate the sorting steps.

**Sorting Algorithms Overview**

1. Bubble Sort
Compares each pair of adjacent elements and swaps them if they're in the wrong order.
Visualized with gradual coloring as elements are sorted.
2. Merge Sort
Divides the list into sub-lists, sorts them, and merges them back together.
Colors are used to indicate the merging process.
3. Quick Sort
Selects a pivot element and partitions the list, recursively sorting each part.
Visualization highlights elements compared to the pivot.

**Future Enhancements**

Add more sorting algorithms (e.g., Insertion Sort, Heap Sort).
Adjustable speed control for the visual delay.
Enhanced GUI layout and design.
