import contextlib

@contextlib.contextmanager
def my_context_manager():
    print("Entering context")
    try:
        yield "Context value"
    except Exception as exc:
        print(f"Exception occurred: {exc}")
        print("Rolling back changes")
    finally:
        print("Exiting context")

with my_context_manager() as value:
    print(f"Inside context: {value}")
    raise ValueError("An error occurred")