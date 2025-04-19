# 🦌 Deer-Plant Population Dynamics

This project simulates the interaction between a population of deer and plant density in a shared habitat over time. The model is built as a discrete-time system using ecological assumptions and piecewise-defined functions.

## 📘 Problem Description

In this model, 100 deer are introduced into a patch of land consisting of both forest and grassland. The plant population grows logistically, with a growth rate of 0.8 at low density and zero growth at the maximum density of 3000 units.

Each year:
- Plants grow according to logistic growth.
- Deer consume the plant resources, up to a max of 1.2 units per deer when food is abundant.
- If insufficient food is available, the deer population declines at a rate of 1.1 per year.

The model investigates whether the system stabilizes, oscillates, or collapses depending on how the plant-deer interaction plays out over time.

## 📈 Model Overview
- Discrete time steps (1 step = 1 year)
- Plant growth and deer consumption are nonlinear and bounded
- Simulated for 30 time steps

## 💾 File
- `main.py`: Contains the full simulation script (no external libraries required)

## 🔧 Parameters
- Max plant density: 3000 units  
- Growth rate at low density: 0.8  
- Max deer consumption: 1.2 units per year  
- Starvation rate: 1.1 (if no food)

## 🧠 Key Features
- Logistic growth modeling
- Piecewise consumption function
- Visualization-ready output (if plotting is added)
