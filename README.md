# Smart EV Charging Routing Optimization System

## Project Overview

This project focuses on optimizing electric vehicle (EV) charging station routing in smart cities using network optimization techniques.

The system:
- finds the shortest and most efficient route,
- considers traffic density,
- excludes unavailable charging stations,
- checks battery feasibility.

The project simulates the routing logic used in real-world EV charging applications.

---

## Real-World Problem Context

As electric vehicle adoption increases worldwide, finding an efficient charging station has become an important challenge for smart transportation systems.

Drivers may experience:
- long travel distances,
- traffic congestion,
- unavailable charging stations,
- battery limitations.

This project provides a smart routing model that helps optimize EV charging accessibility in urban environments.

---

## Selected Algorithm

### Dijkstra Shortest Path Algorithm

The project uses Dijkstra’s algorithm to calculate the most efficient route between the driver’s location and an available charging station.

The algorithm minimizes:
- travel distance,
- traffic-related cost,
- overall routing cost.

---

## Technologies Used

- Python
- NetworkX
- Pandas
- Matplotlib
- SciPy

---

## Features

- Shortest path optimization
- Traffic-aware routing
- Dynamic charging station availability
- Battery feasibility check
- Network visualization

---

## Dataset Structure

| Source | Target | Distance | Traffic |
|---|---|---|---|
| Kadikoy | Moda Coast | 2 | 2 |
| Kadikoy | Emaar Mall | 8 | 3 |
| Moda Coast | EV Station Metro | 3 | 2 |

---

## Project Structure

```text
smart-ev-routing-system/

│── README.md
│── requirements.txt

│── data/
│     └── network_data.csv

│── src/
│     └── solution.py

│── results/
│     ├── highlighted_route.png
│     └── solution_output.txt

│── references/
│     └── references.md

```

## Network Visualization

![Network Visualization](results/highlighted_route.png)
