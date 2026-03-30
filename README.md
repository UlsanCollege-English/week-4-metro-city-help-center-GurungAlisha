[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KuuIFSwK)
# Weekly Coding #3 — Metro City Help Center

## Summary
This homework uses one connected story to practice stack and queue behavior in Python.

Metro City Help Center needs a small support system for recent staff actions, waiting citizens, request-note checks, and service-line processing.

## How to run
```bash
pytest -q
```

## Complexity

### `ActionStack.pop`
- **Time:** O(1)
- **Why:** Python's `list.pop()` removes the last element in constant time — no shifting of other elements is needed.

### `RequestQueue.dequeue`
- **Time:** O(1)
- **Why:** `collections.deque.popleft()` removes from the front in constant time. A plain list would cost O(n) here because every element would need to shift left by one.

### `is_note_balanced`
- **Time:** O(n), where n is the length of the note string
- **Why:** We scan every character exactly once. Each character causes at most one push or one pop on the stack, both O(1), so the total work is linear.

### `process_request_line`
- **Time:** O(n), where n is the number of citizens
- **Why:** We enqueue all n citizens (n × O(1)) and then dequeue all n citizens (n × O(1)), giving O(n) overall.

## Edge-case checklist
- [x] empty action stack
- [x] empty request queue
- [x] empty string for `is_note_balanced`
- [x] note with no brackets
- [x] empty citizen list

## Assistance & sources
- **AI used?** Yes
- **What it helped with:** Generating the initial implementations and explaining why `deque.popleft()` is O(1) while `list.pop(0)` is O(n).
- **Other sources:** Week 4 lecture slides on stacks and queues.