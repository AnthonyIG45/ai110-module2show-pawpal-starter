# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Generating daily plan for Biscuit...

==================================================
  Schedule for Biscuit (Dog — Golden Retriever, age 3)  (Daily Plan)
==================================================

  2026-06-25
  ------------------------------
    08:00 AM - 08:10 AM  |  Feeding [high]  (10 min)
    08:10 AM - 08:40 AM  |  Morning Walk [high]  (30 min)
    08:40 AM - 09:00 AM  |  Grooming [low]  (20 min)

  Total scheduled: 3 task(s)
  Total skipped:   0 task(s)

  Reasoning:
  Scheduled 3 task(s) for Biscuit:
    - Feeding (priority: high, 10 min)
    - Morning Walk (priority: high, 30 min)
    - Grooming (priority: low, 20 min)
==================================================

Generating weekly plan for Whiskers...

==================================================
  Schedule for Whiskers (Cat — Tabby, age 5)  (Weekly Plan)
==================================================

  2026-06-25
  ------------------------------
    08:00 AM - 08:10 AM  |  Feeding [high]  (10 min)
    08:10 AM - 08:25 AM  |  Litter Box [medium]  (15 min)
    08:25 AM - 08:45 AM  |  Playtime [low]  (20 min)

  2026-06-26
  ------------------------------
    08:00 AM - 08:10 AM  |  Feeding [high]  (10 min)
    08:10 AM - 08:25 AM  |  Litter Box [medium]  (15 min)
    08:25 AM - 08:45 AM  |  Playtime [low]  (20 min)

  2026-06-27
  ------------------------------
    08:00 AM - 08:10 AM  |  Feeding [high]  (10 min)
    08:10 AM - 08:25 AM  |  Litter Box [medium]  (15 min)
    08:25 AM - 08:45 AM  |  Playtime [low]  (20 min)

  2026-06-28
  ------------------------------
    08:00 AM - 08:10 AM  |  Feeding [high]  (10 min)
    08:10 AM - 08:25 AM  |  Litter Box [medium]  (15 min)
    08:25 AM - 08:45 AM  |  Playtime [low]  (20 min)

  2026-06-29
  ------------------------------
    08:00 AM - 08:10 AM  |  Feeding [high]  (10 min)
    08:10 AM - 08:25 AM  |  Litter Box [medium]  (15 min)
    08:25 AM - 08:45 AM  |  Playtime [low]  (20 min)

  2026-06-30
  ------------------------------
    08:00 AM - 08:10 AM  |  Feeding [high]  (10 min)
    08:10 AM - 08:25 AM  |  Litter Box [medium]  (15 min)
    08:25 AM - 08:45 AM  |  Playtime [low]  (20 min)

  2026-07-01
  ------------------------------
    08:00 AM - 08:10 AM  |  Feeding [high]  (10 min)
    08:10 AM - 08:25 AM  |  Litter Box [medium]  (15 min)
    08:25 AM - 08:45 AM  |  Playtime [low]  (20 min)

  Total scheduled: 21 task(s)
  Total skipped:   0 task(s)

  Reasoning:
  Scheduled 21 task(s) for Whiskers:
    - Feeding (priority: high, 10 min)
    - Litter Box (priority: medium, 15 min)
    - Playtime (priority: low, 20 min)
    - Feeding (priority: high, 10 min)
    - Litter Box (priority: medium, 15 min)
    - Playtime (priority: low, 20 min)
    - Feeding (priority: high, 10 min)
    - Litter Box (priority: medium, 15 min)
    - Playtime (priority: low, 20 min)
    - Feeding (priority: high, 10 min)
    - Litter Box (priority: medium, 15 min)
    - Playtime (priority: low, 20 min)
    - Feeding (priority: high, 10 min)
    - Litter Box (priority: medium, 15 min)
    - Playtime (priority: low, 20 min)
    - Feeding (priority: high, 10 min)
    - Litter Box (priority: medium, 15 min)
    - Playtime (priority: low, 20 min)
    - Feeding (priority: high, 10 min)
    - Litter Box (priority: medium, 15 min)
    - Playtime (priority: low, 20 min)
==================================================

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here

============================================================== test session starts ======================================================================
platform win32 -- Python 3.11.9, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\agoines\Desktop\Computer Shit (1)\Code\CodePath\ai110-module2show-pawpal-starter
collected 2 items                                                                                                                                                                                                                                 

tests\test_pawpal.py ..                                                                                                                                                                                                                     [100%]

===================================================== 2 passed in 0.01s =================================================================================

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
