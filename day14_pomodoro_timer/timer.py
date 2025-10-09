# timer.py
import time
import sys
import threading
from threading import Event
try:
    import msvcrt  # For Windows
    _has_msvcrt = True
except ImportError:
    # fallback for Unix-like systems
    try:
        import getch   # type: ignore
        _has_msvcrt = False
    except ImportError:
        # If neither is available, we'll read from stdin as a last resort
        _has_msvcrt = False

from utils import format_time

# Shared state
paused = False
stop_event = Event()
_listener_started = False

def _read_key():
    """Read a single keypress in a cross-platform way (best-effort)."""
    if _has_msvcrt:
        try:
            return msvcrt.getch().decode('utf-8').lower()
        except Exception:
            return ''
    else:
        try:
            # getch provides a blocking single-char read
            return getch.getch().lower()  # type: ignore
        except Exception:
            # last resort: non-blocking stdin read isn't trivial cross-platform,
            # so just return empty to avoid blocking.
            return ''

def key_listener():
    """Listens for key presses to pause, resume, or quit the timer."""
    global paused
    while not stop_event.is_set():
        key = _read_key()
        if not key:
            # avoid tight busy loop if no key reading method is available
            time.sleep(0.1)
            continue

        if key == 'p':
            paused = True
            print("\n⏸️  Timer paused. Press 'r' to resume.")
        elif key == 'r':
            if paused:
                paused = False
                print("▶️  Resumed.")
        elif key == 'q':
            print("\n🛑 Timer stopped early by user.")
            stop_event.set()
            # break loop and allow threads to exit
            break


def _ensure_listener():
    """Start the key listener thread once (daemon)."""
    global _listener_started
    if not _listener_started:
        listener_thread = threading.Thread(target=key_listener, daemon=True)
        listener_thread.start()
        _listener_started = True


def countdown(duration, label):
    """Runs a countdown for a given label and duration. Honors pause and stop_event."""
    global paused
    paused = False

    print(f"\n🔔 {label} started! ({duration // 60} minutes)")
    _ensure_listener()

    for remaining in range(duration, 0, -1):
        if stop_event.is_set():
            # stop requested by user
            return
        while paused and not stop_event.is_set():
            time.sleep(0.5)
        if stop_event.is_set():
            return
        print(f"⏳ Time left: {format_time(remaining)}", end="\r")
        time.sleep(1)

    print(f"\n✅ {label} completed!\n")


def pomodoro_cycle(work_duration, break_duration, cycles):
    """Runs multiple work sessions followed by one single break. Exits early if stop_event set."""
    # Clear stop_event in case it was set previously
    stop_event.clear()

    for i in range(1, cycles + 1):
        if stop_event.is_set():
            break
        print(f"\n🍅 Pomodoro {i}/{cycles}")
        countdown(work_duration, "Work Session")

    if not stop_event.is_set():
        # After all work sessions, one final break
        countdown(break_duration, "Break Time")
        if not stop_event.is_set():
            print("\n🎉 All work sessions complete! Take a good rest. 💤")
