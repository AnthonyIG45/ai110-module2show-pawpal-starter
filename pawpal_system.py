class Owner:
    def __init__(self, name: str, available_minutes: int, preferences: dict = None):
        self.name = name
        self.available_minutes = available_minutes
        self.preferences = preferences or {}

    def get_available_time(self) -> int:
        pass

    def set_preference(self, key: str, value: str) -> None:
        pass


class Pet:
    def __init__(self, name: str, species: str, breed: str, age: int, owner: Owner):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.owner = owner

    def get_info(self) -> str:
        pass


class Task:
    def __init__(
        self,
        name: str,
        duration_minutes: int,
        priority: str,
        category: str,
        recurrence: str = "daily",
        preferred_time_of_day: str = "morning",
    ):
        self.name = name
        self.duration_minutes = duration_minutes
        self.priority = priority
        self.category = category
        self.recurrence = recurrence
        self.preferred_time_of_day = preferred_time_of_day
        self.is_completed = False

    def get_priority_value(self) -> int:
        pass

    def is_due_today(self) -> bool:
        pass

    def mark_complete(self) -> None:
        pass


class ScheduledTask:
    def __init__(self, task: Task, start_time: str, end_time: str):
        self.task = task
        self.start_time = start_time
        self.end_time = end_time

    def get_duration(self) -> int:
        pass

    def conflicts_with(self, other: "ScheduledTask") -> bool:
        pass

    def to_display_string(self) -> str:
        pass


class DailyPlan:
    def __init__(self, pet: Pet, date: str):
        self.pet = pet
        self.date = date
        self.scheduled_tasks: list[ScheduledTask] = []
        self.total_duration = 0

    def add_task(self, task: ScheduledTask) -> None:
        pass

    def get_total_duration(self) -> int:
        pass

    def get_summary(self) -> str:
        pass

    def explain_reasoning(self) -> str:
        pass


class Scheduler:
    def __init__(self, pet: Pet, tasks: list[Task], available_minutes: int):
        self.pet = pet
        self.tasks = tasks
        self.available_minutes = available_minutes

    def sort_by_priority(self, tasks: list[Task]) -> list[Task]:
        pass

    def filter_by_time(self, tasks: list[Task], remaining: int) -> list[Task]:
        pass

    def assign_time_slots(self, tasks: list[Task]) -> list[ScheduledTask]:
        pass

    def resolve_conflicts(self, scheduled: list[ScheduledTask]) -> list[ScheduledTask]:
        pass

    def generate_plan(self) -> DailyPlan:
        pass
