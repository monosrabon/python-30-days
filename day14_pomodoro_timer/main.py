# main.py
from timer import pomodoro_cycle

def main():
    print("🍅 Welcome to the Pomodoro Focus Timer (Minimal Pro Edition)!")
    print("Work smarter, not harder 😎\n")
    print("Controls: [p] Pause | [r] Resume | [q] Quit\n")

    # === Get user-defined durations ===
    try:
        work_duration = int(input("Enter work session duration (minutes): ")) * 60
        break_duration = int(input("Enter break duration (minutes): ")) * 60
        cycles = int(input("Enter total Pomodoro work sessions: "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")
        return

    pomodoro_cycle(work_duration, break_duration, cycles)


if __name__ == "__main__":
    main()
