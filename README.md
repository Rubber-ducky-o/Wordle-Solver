# Wordle Solver
![Py()n](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green?logo=playwright)
<p>An Entropy-Based Wordle Solver</p>  

## Overview
An automated Wordle solver that uses entropy and information gain to evaluate a best possible guess.

The solver filters through a 3,000+ word set using green, yellow, and gray feedback, reducing the search space after each guess.

## Performance
Tested across 1,000 automated local wordle games:

| Metric | Result | 
|--------|--------|
|Win Rate| 97.9%  |
|Avg guesses| 3.87  |
|Avg Comp. Time| 191 ms/game|


## How it works

1. Submits a random first wordle guess through Playwright.
2. Reads tile colors from the browser DOM.
3. Converts readings into numerical feedback scores.
4. Filters impossible candidate words based on color constraints.
5. Simulates feedback patterns for remaining candidate guesses.
6. Calculates expected information gain of each candidate.
7. Selects highest-scoring word as next guess.
8. Repeats until wordle is solved, or guess limit is reached.


## Installation

### 1. Dependent Libraries
From project root:

```bash
pip install -r requirements.txt
playwright install chromium
```
### 2. Starting Local Wordle server
Ensure having 2 terminals, in first terminal HTTP server must be started within the Local_wordle directory:
```bash
cd Local_wordle
python -m http.server 8000
```

Ensure server is running before moving on.

### 3. Run the Solver

In the second terminal from project root: 

```bash
python -m Machine_Learning.comms
```

A browser window will open the local Wordle instance. The same terminal you will be prompted to enter the number of amount of games you'd like the solver to run.

### quick run-down:
```text
Terminal 1:
Sordle/Local_wordle
> python -m http.server 8000

Terminal 2:
Sordle
>python -m Machine_Learning.comms
```
## Starting Wordle Online
The wordle solver can also interact with the NYT website with Playwright.

### Online Mode 

From project root, in a terminal, run:
```bash
python -m Machine_Learning.online
```

Playwright will directly open the NYT wordle page and begin solving the daily wordle.

>**NOTE:** NYT Wordle only provides a single daily puzzle, running the online version multiple times will result in the same word being solved for. 

## Visualizations
### Information Gain Landscape

<img width="640" height="480" alt="Updated_3d" src="https://github.com/user-attachments/assets/a2d1783b-038e-4d3d-9102-f9b18566e5b3" />


Displays 3d model of information-gain scores of candidate words across solver iterations.

### Candidate Search Space Reduction
<img width="640" height="480" alt="Updated_2d" src="https://github.com/user-attachments/assets/03aff01b-6635-4874-b73d-42316c3b583a" />

Displays the decrease of remaining candidate guesses through the solvers process.
### Enable Graphing

If you'd like to see the graphic models, within 
```text
>Sordle/Machine_Learning/comms.py
```
you may change the graphing feature to `True`.
```python
#line 48
solver.data.initialize(Debug =False, graphing = True)
```
To disable graphing:
```python
#line 48
solver.data.initialize(Debug = False,graphing =False)
```

>**NOTE:** graphing is shown per game ran, if you're running more than 1 game ensure to close both graphs upon appearing for the solver to continue.
Usage
