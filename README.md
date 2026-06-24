# study-habit-analyzer
python-based study habit analyzer that calculates a productivity score based on study time, sleep and procrastination.

## Overview
This project takes user input for daily study habits and evaluates productivity using a weighted scoring system. It is designed to explore how behavioural factors like procrastination affect learning outcomes and overall productivity.

## Features
- takes input (study hrs, sleep time, procrastination lvl)
- calculates productivity score out of 10
- provides personalized feedback
- detects unhealthy habits
- prevents unrealistic score values
- supports daily study goals
- provides personalized suggestions
- awards productivity badges
- saves daily records in a text file
- automatically stores the date with each record
- uses functions for better code organization

## How to run
1. Python IDLE is installed
2. Download `main.py`
3. Open file
4. Run

```
python main.py
```

## Example output

```
Your score is: 8/10
🏆 Badge Earned: Productive Day!
🎯 Goal achieved!

Suggestions:
- Great balance! Keep it up!

Today's data has been saved successfully!
```

## Data storage

The program automatically creates and updates a file named `study_log.txt`, where each session is saved for future analysis.

Example:

```
Date: 2026-06-24 | Study Hours: 4 | Sleep Hours: 8 | Procrastination Level: 3 | Score: 7.8/10
```

## Future improvements
- view previous records
- weekly and monthly productivity analysis
- streak system
- graphs and data visualization
- web-based interface

## Programmer
Ashmira <3
