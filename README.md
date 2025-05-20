# N-Queens Problem – Tkinter GUI Game 🎯♕  

A Python GUI-based interactive implementation of the classic **N-Queens Problem** using `Tkinter`. Users can play the game by placing queens on a customizable `NxN` chessboard such that no two queens threaten each other.  

## 🧠 About the N-Queens Problem  
The goal of the N-Queens problem is to place N queens on an `N×N` chessboard so that no two queens attack each other — meaning no two queens share the same row, column, or diagonal.

## 🛠 Features  
- Interactive GUI with a grid created using Tkinter
- Image-based queens loaded using Pillow (PIL)
- Visual validation of valid/invalid moves
- Dynamic board size (minimum 4×4)
- Win/lose feedback with message boxes
- Fun and educational for learning recursion, constraints, and GUI design

## 🚀 How to Run

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/nqueens-tkinter.git
    cd nqueens-tkinter
    ```

2. Make sure you have Python installed (version ≥ 3.6)

3. Install required libraries:
    ```bash
    pip install Pillow
    ```

4. Update the image path in the code:
    > Replace  
    ```python
    img[nq] = Image.open("E:/python 1/bq.png")
    ```  
    with the actual path to your queen image (`bq.png`)

## 🎨 Tech Stack
- Python 3
- Tkinter – GUI library
- Pillow (PIL) – for handling image resizing
- Math – to handle diagonal constraints




