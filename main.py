from pawpal_system import Owner, Pet, Task, Scheduler


def print_plan(plan: dict) -> None:
    print(f"\n{'=' * 50}")
    print(f"  Schedule for {plan['pet']}  ({plan['period'].capitalize()} Plan)")
    print(f"{'=' * 50}")

    for day in plan["days"]:
        print(f"\n  {day['date']}")
        print(f"  {'-' * 30}")

        if day["slots"]:
            for slot in day["slots"]:
                start = slot["start_time"].strftime("%I:%M %p")
                end = slot["end_time"].strftime("%I:%M %p")
                print(f"    {start} - {end}  |  {slot['task_name']} [{slot['priority']}]  ({slot['duration_minutes']} min)")
        else:
            print("    No tasks scheduled.")

        if day["skipped"]:
            print(f"\n    Skipped:")
            for s in day["skipped"]:
                print(f"      - {s['task_name']} ({s['reason']})")

    print(f"\n  Total scheduled: {plan['total_scheduled']} task(s)")
    print(f"  Total skipped:   {plan['total_skipped']} task(s)")
    print(f"\n  Reasoning:\n  {plan['reasoning'].replace(chr(10), chr(10) + '  ')}")
    print(f"{'=' * 50}\n")


def main():
    # --- Owner ---
    owner = Owner(
        first_name="Anthony",
        last_name="Goines",
        email="anthonyig45@gmail.com",
        available_minutes=90,
    )

    # --- Pets ---
    biscuit = Pet(name="Biscuit", species="Dog", breed="Golden Retriever", age=3, owner=owner)
    whiskers = Pet(name="Whiskers", species="Cat", breed="Tabby", age=5, owner=owner)

    owner.add_pet(biscuit)
    owner.add_pet(whiskers)

    # --- Tasks for Biscuit ---
    biscuit.add_task(Task(
        name="Morning Walk",
        duration_minutes=30,
        priority="high",
        category="exercise",
        recurrence="daily",
    ))
    biscuit.add_task(Task(
        name="Feeding",
        duration_minutes=10,
        priority="high",
        category="feeding",
        recurrence="daily",
    ))
    biscuit.add_task(Task(
        name="Grooming",
        duration_minutes=20,
        priority="low",
        category="grooming",
        recurrence="weekly",
    ))

    # --- Tasks for Whiskers ---
    whiskers.add_task(Task(
        name="Feeding",
        duration_minutes=10,
        priority="high",
        category="feeding",
        recurrence="daily",
    ))
    whiskers.add_task(Task(
        name="Litter Box",
        duration_minutes=15,
        priority="medium",
        category="hygiene",
        recurrence="daily",
    ))
    whiskers.add_task(Task(
        name="Playtime",
        duration_minutes=20,
        priority="low",
        category="enrichment",
        recurrence="daily",
    ))

    # --- Generate and print schedules ---
    print("\nGenerating daily plan for Biscuit...")
    biscuit_scheduler = Scheduler(pet=biscuit)
    biscuit_plan = biscuit_scheduler.generate_plan(period="daily")
    print_plan(biscuit_plan)

    print("Generating weekly plan for Whiskers...")
    whiskers_scheduler = Scheduler(pet=whiskers)
    whiskers_plan = whiskers_scheduler.generate_plan(period="weekly")
    print_plan(whiskers_plan)


if __name__ == "__main__":
    main()
