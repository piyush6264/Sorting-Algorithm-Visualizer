import tkinter as tk
import random
import time

# Sorting algorithms with visualization
def bubble_sort(data, draw_data, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_data(data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                time.sleep(delay)
    draw_data(data, ['green' for x in range(len(data))])

def merge_sort(data, draw_data, delay):
    merge_sort_algorithm(data, 0, len(data)-1, draw_data, delay)
    draw_data(data, ['green' for x in range(len(data))])

def merge_sort_algorithm(data, left, right, draw_data, delay):
    if left < right:
        mid = (left + right) // 2
        merge_sort_algorithm(data, left, mid, draw_data, delay)
        merge_sort_algorithm(data, mid+1, right, draw_data, delay)
        merge(data, left, mid, right, draw_data, delay)

def merge(data, left, mid, right, draw_data, delay):
    left_copy = data[left:mid+1]
    right_copy = data[mid+1:right+1]
    left_idx, right_idx = 0, 0
    sorted_idx = left

    while left_idx < len(left_copy) and right_idx < len(right_copy):
        if left_copy[left_idx] <= right_copy[right_idx]:
            data[sorted_idx] = left_copy[left_idx]
            left_idx += 1
        else:
            data[sorted_idx] = right_copy[right_idx]
            right_idx += 1
        sorted_idx += 1
        draw_data(data, ['green' if x >= left and x <= right else 'red' for x in range(len(data))])
        time.sleep(delay)

    while left_idx < len(left_copy):
        data[sorted_idx] = left_copy[left_idx]
        left_idx += 1
        sorted_idx += 1

    while right_idx < len(right_copy):
        data[sorted_idx] = right_copy[right_idx]
        right_idx += 1
        sorted_idx += 1

def quick_sort(data, draw_data, delay):
    quick_sort_algorithm(data, 0, len(data) - 1, draw_data, delay)
    draw_data(data, ['green' for x in range(len(data))])

def quick_sort_algorithm(data, low, high, draw_data, delay):
    if low < high:
        pivot = partition(data, low, high, draw_data, delay)
        quick_sort_algorithm(data, low, pivot - 1, draw_data, delay)
        quick_sort_algorithm(data, pivot + 1, high, draw_data, delay)

def partition(data, low, high, draw_data, delay):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
            draw_data(data, ['green' if x == i or x == j else 'red' for x in range(len(data))])
            time.sleep(delay)
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1
# GUI Code
class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")
        self.root.maxsize(900, 600)
        
        self.selected_algo = tk.StringVar()
        self.data = []
        
        # UI for algorithm selection and visualization speed
        ui_frame = tk.Frame(root, width=600, height=200)
        ui_frame.grid(row=0, column=0, padx=10, pady=5)
        
        tk.Label(ui_frame, text="Algorithm:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        algo_menu = tk.OptionMenu(ui_frame, self.selected_algo, "Bubble Sort", "Merge Sort", "Quick Sort")
        algo_menu.grid(row=0, column=1, padx=5, pady=5)
        tk.Button(ui_frame, text="Start", command=self.start_sorting).grid(row=1, column=1, padx=5, pady=5)
        self.canvas = tk.Canvas(root, width=800, height=400, bg="white")
        self.canvas.grid(row=1, column=0, padx=10, pady=5)
        
    def start_sorting(self):
        if not self.data:
            self.data = [random.randint(1, 100) for _ in range(50)]
        if self.selected_algo.get() == "Bubble Sort":
            bubble_sort(self.data, self.draw_data, 0.1)
        elif self.selected_algo.get() == "Merge Sort":
            merge_sort(self.data, self.draw_data, 0.1)
        elif self.selected_algo.get() == "Quick Sort":
            quick_sort(self.data, self.draw_data, 0.1)
    
    def draw_data(self, data, color):
        self.canvas.delete("all")
        c_height = 400
        c_width = 800
        x_width = c_width / len(data)
        for i, height in enumerate(data):
            x0 = i * x_width
            y0 = c_height - height * 3
            x1 = (i + 1) * x_width
            y1 = c_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    SortingVisualizer(root)
    root.mainloop()
