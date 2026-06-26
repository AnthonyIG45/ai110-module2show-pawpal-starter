from datetime import date, datetime, time, timedelta


class Owner:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        available_minutes: int,
        preferences: dict = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.available_minutes = available_minutes
        self.preferences = preferences or {}
        self.pets: list["Pet"] = []

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def add_pet(self, pet: "Pet") -> None:
        if any(p.name == pet.name for p in self.pets):
            raise ValueError(f"Pet '{pet.name}' already exists for {self.name}.")
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        pet = self._find_pet(pet_name)
        if pet is None:
            raise ValueError(f"Pet '{pet_name}' not found for {self.name}.")
        self.pets.remove(pet)

    def get_all_tasks(self) -> list["Task"]:
        return [task for pet in self.pets for task in pet.tasks]

    def get_available_time(self) -> int:
        return self.available_minutes

    def set_preference(self, key: str, value: str) -> None:
        self.preferences[key] = value

    def _find_pet(self, pet_name: str) -> "Pet | None":
        for pet in self.pets:
            if pet.name == pet_name:
                return pet
        return None


class Pet:
    def __init__(self, name: str, species: str, breed: str, age: int, owner: Owner):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.owner = owner
        self.tasks: list["Task"] = []

    def add_task(self, task: "Task") -> None:
        if any(t.name == task.name for t in self.tasks):
            raise ValueError(f"Task '{task.name}' already exists for {self.name}.")
        self.tasks.append(task)

    def remove_task(self, task_name: str) -> None:
        task = self._find_task(task_name)
        if task is None:
            raise ValueError(f"Task '{task_name}' not found for {self.name}.")
        self.tasks.remove(task)

    def edit_task(self, task_name: str, **updates) -> None:
        task = self._find_task(task_name)
        if task is None:
            raise ValueError(f"Task '{task_name}' not found for {self.name}.")
        for key, value in updates.items():
            if not hasattr(task, key):
                raise ValueError(f"Task has no attribute '{key}'.")
            setattr(task, key, value)

    def get_info(self) -> str:
        return f"{self.name} ({self.species} — {self.breed}, age {self.age})"

    def _find_task(self, task_name: str) -> "Task | None":
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None


class Task:
    def __init__(
        self,
        name: str,
        duration_minutes: int,
        priority: str,
        category: str,
        recurrence: str = "daily",
        preferred_time_of_day: str = "morning",
        last_completed_date: date = None,
    ):
        self.name = name
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.category = category
        self.recurrence = recurrence
        self.preferred_time_of_day = preferred_time_of_day
        self.last_completed_date = last_completed_date
        self.is_completed = False

    def get_priority_value(self) -> int:
        priority_map = {"high": 3, "medium": 2, "low": 1}
        return priority_map.get(self.priority.lower(), 0)

    def is_due_today(self) -> bool:
        if self.recurrence == "daily":
            return self.last_completed_date != date.today()
        if self.recurrence == "weekly":
            if self.last_completed_date is None:
                return True
            return (date.today() - self.last_completed_date).days >= 7
        return False

    def mark_complete(self) -> None:
        self.is_completed = True
        self.last_completed_date = date.today()


class Scheduler:
    def __init__(self, pet: Pet, day_start: time = time(8, 0)):
        self.pet = pet
        self.available_minutes = pet.owner.available_minutes
        self.preferences = pet.owner.preferences
        self.day_start = day_start

    def sort_by_priority(self, tasks: list[Task]) -> list[Task]:
        # Primary: highest priority first. Tiebreaker: shortest task first to fit more in.
        return sorted(tasks, key=lambda t: (-t.get_priority_value(), t.duration_minutes))

    def filter_by_time(self, tasks: list[Task], remaining: int) -> tuple[list[Task], list[Task]]:
        scheduled, skipped = [], []
        for task in tasks:
            if task.duration_minutes <= remaining:
                scheduled.append(task)
                remaining -= task.duration_minutes
            else:
                skipped.append(task)
        return scheduled, skipped

    def assign_time_slots(self, tasks: list[Task], day: date) -> list[dict]:
        slots = []
        current = datetime.combine(day, self.day_start)
        for task in tasks:
            start = current.time()
            end = (current + timedelta(minutes=task.duration_minutes)).time()
            slots.append({
                "task_name": task.name,
                "category": task.category,
                "priority": task.priority,
                "start_time": start,
                "end_time": end,
                "duration_minutes": task.duration_minutes,
            })
            current += timedelta(minutes=task.duration_minutes)
        return slots

    def resolve_conflicts(self, slots: list[dict]) -> list[dict]:
        resolved = []
        for slot in slots:
            if not resolved or slot["start_time"] >= resolved[-1]["end_time"]:
                resolved.append(slot)
        return resolved

    def generate_plan(self, period: str = "daily") -> dict:
        period_days = {"daily": 1, "weekly": 7, "monthly": 30}
        if period not in period_days:
            raise ValueError(f"Unknown period '{period}'. Use 'daily', 'weekly', or 'monthly'.")

        num_days = period_days[period]
        all_days = []
        all_scheduled = []
        all_skipped = []

        for day_offset in range(num_days):
            day = date.today() + timedelta(days=day_offset)
            due_tasks = [t for t in self.pet.tasks if self._is_due_on(t, day_offset)]
            sorted_tasks = self.sort_by_priority(due_tasks)
            scheduled_tasks, skipped_tasks = self.filter_by_time(sorted_tasks, self.available_minutes)
            slots = self.assign_time_slots(scheduled_tasks, day)
            slots = self.resolve_conflicts(slots)

            all_scheduled.extend(scheduled_tasks)
            all_skipped.extend(skipped_tasks)

            all_days.append({
                "date": day.isoformat(),
                "slots": slots,
                "skipped": [
                    {"task_name": t.name, "reason": "Insufficient time remaining"}
                    for t in skipped_tasks
                ],
            })

        return {
            "pet": self.pet.get_info(),
            "period": period,
            "days": all_days,
            "total_scheduled": len(all_scheduled),
            "total_skipped": len(all_skipped),
            "reasoning": self._build_reasoning(all_scheduled, all_skipped),
        }

    def _is_due_on(self, task: Task, day_offset: int) -> bool:
        if day_offset == 0:
            return task.is_due_today()
        if task.recurrence == "daily":
            return True
        if task.recurrence == "weekly":
            return day_offset % 7 == 0
        return False

    def _build_reasoning(self, scheduled: list[Task], skipped: list[Task]) -> str:
        lines = [f"Scheduled {len(scheduled)} task(s) for {self.pet.name}:"]
        for task in scheduled:
            lines.append(f"  - {task.name} (priority: {task.priority}, {task.duration_minutes} min)")
        if skipped:
            lines.append(f"Skipped {len(skipped)} task(s) due to time constraints:")
            for task in skipped:
                lines.append(f"  - {task.name} ({task.duration_minutes} min, priority: {task.priority})")
        return "\n".join(lines)
