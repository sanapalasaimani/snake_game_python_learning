# 🐍💧🔫 Snake, Water, Gun Game

> **Day 1 Learning Project** 🚀  
> A practice project to refresh Python concepts and learn web framework integration (Flask) in preparation for placements.

---

## 📖 About The Project

This is a web-based adaptation of the classic childhood game **Snake, Water, Gun** (which is similar to Rock, Paper, Scissors). The user plays a best-of-3 match against the computer. 

Initially started as a simple console-based Python script, this project has been upgraded with a full-stack approach using **Flask** for the backend and a premium, modern frontend using **HTML/CSS**.

### 🎮 Game Rules
- **Snake vs Water:** Snake drinks the water. *(Snake wins)*
- **Water vs Gun:** Water rusts the gun / gun sinks in water. *(Water wins)*
- **Gun vs Snake:** Gun shoots the snake. *(Gun wins)*

## ✨ Features
- **Web Frontend:** A beautiful, responsive interface featuring a modern "Glassmorphism" design with animated gradient backgrounds.
- **State Management:** Uses Flask Sessions to track the current round, the player's score, and the computer's score across HTTP requests.
- **Game Logic Engine:** Python backend handles randomized computer choices and determines round winners instantly.
- **Match History:** Displays a clean, color-coded log of what both players chose during previous rounds of the match.

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML5, Vanilla CSS3
- **Design:** CSS Variables, Flexbox, Keyframe Animations, Google Fonts (*Outfit*)

## 🚀 How to Run Locally

To play this game on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sanapalasaimani/snake_game_python_learning.git
   cd snake_game_python_learning
   ```

2. **Install dependencies:**
   Make sure you have Python installed, then install Flask:
   ```bash
   pip install flask
   ```

3. **Run the server:**
   ```bash
   python app.py
   ```

4. **Play the game:**
   Open your web browser and go to: `http://127.0.0.1:5000`

---
*Built as a learning milestone for placement preparation.*
