# Phase 1 – Foundations (Detailed Course)
# Duration: 8 Weeks (5 hours/week)

> **Mission**
>
> Do **not** memorize solutions.
>
> By the end of Phase 1 you should be able to:
>
> - Recognize the correct data structure.
> - Explain *why* it is the correct choice.
> - Derive the optimal solution from brute force.
> - Communicate your thinking like an interviewer expects.

---

# How to Solve EVERY Problem

Use this framework every time.

1. What is the problem really asking?
2. Can I simplify or restate it?
3. What does the brute-force solution look like?
4. Why is brute force too slow?
5. What operation is expensive?
6. Which data structure removes that expense?
7. What invariant am I maintaining?
8. Dry run by hand.
9. Complexity.
10. Explain your approach in 60 seconds.

---

# Weekly Schedule (5 hours)

## Session 1 (2h)
- Read lesson
- Study concept
- Solve guided problem

## Session 2 (2h)
- Solve 2–3 problems independently
- Explain solution aloud

## Session 3 (1h)
- Re-solve one old problem
- Review .NET topic
- Complete design exercise

---

# WEEK 1 — Arrays & Hash Maps

## Weekly Goal

By the end of this week you should immediately recognize:

- "Need fast lookup" → Hash Map
- "Need uniqueness" → Hash Set
- "Need counting" → Frequency Map
- "Need grouping" → Hash Map<List>

You should stop asking:
> "Which algorithm?"

and instead ask:
> "What information am I repeatedly searching for?"

---

## Lesson

### Arrays

Arrays provide O(1) index access but O(n) search.

Interview question:

"If I repeatedly search an array, what operation is expensive?"

Answer:
Searching.

Can another structure make searching faster?

Yes.

Hash Map.

---

### Hash Maps

A hash map stores:

Key → Value

Examples:

fruit → count

number → index

word → frequency

route → handler

Whenever you hear:

- find quickly
- already seen
- count
- group
- unique

Think Hash Map.

---

## Problem Order

### 1. Two Sum ⭐

Purpose:

Learn the fundamental lookup pattern.

Skill:

Store what you've already seen.

Recognition:

Repeated searching.

Takeaway:

Hash maps replace repeated scans.

---

### 2. Contains Duplicate

Purpose:

Learn uniqueness.

Skill:

HashSet

Recognition:

Need to know if something already exists.

---

### 3. Valid Anagram

Purpose:

Frequency counting.

Skill:

Dictionary<Character,int>

Recognition:

Comparing counts.

---

### 4. Group Anagrams

Purpose:

Designing hash keys.

Skill:

Composite keys.

Recognition:

Different inputs can map to same representation.

---

### 5. Top K Frequent Elements

Purpose:

Combine Hash Map + Heap.

New pattern:

Frequency counting followed by ordering.

---

### 6. Product of Array Except Self

Purpose:

Prefix/Suffix thinking.

Recognition:

Reuse previously computed work.

---

### 7. Longest Consecutive Sequence

Purpose:

HashSet traversal.

Recognition:

Fast membership testing.

---

## Weekly Reflection

You should now answer:

- Why not use an array?
- When is HashSet better than Dictionary?
- What makes a good hash key?

---

## .NET Lesson

Study:

- Dictionary<TKey,TValue>
- HashSet<T>
- EqualityComparer<T>
- Reference vs Value Types

Exercise:

Explain when Dictionary lookup is O(1) and when it degrades.

---

## Design Exercise

Implement:

Router

register(path, handler)

handle(path)

Focus:

HashMap design.

---

# WEEK 2 — Two Pointers & Sliding Window

## Weekly Goal

Recognize:

Two Pointers

vs

Sliding Window

---

## Lesson

Two Pointers

Use when solving a problem with two moving positions.

Sliding Window

Use when maintaining information about a continuous subarray/subsequence.

Key question:

Can I maintain an answer while expanding and shrinking a window?

If yes:

Sliding Window.

---

## Problem Order

1. Valid Palindrome
2. Two Sum II
3. Container With Most Water
4. Best Time to Buy/Sell Stock
5. Longest Substring Without Repeating Characters
6. Longest Repeating Character Replacement
7. Permutation in String
8. Minimum Window Substring

Each problem should answer:

- What invariant is maintained?
- Why move left?
- Why move right?

.NET:
Span<T>
ReadOnlySpan<T>

Design:
Log Rate Limiter

---

# WEEK 3 — Binary Search & Stack

## Weekly Goal

Recognize monotonicity.

Question:

Can I eliminate half the search space?

If yes:

Binary Search.

Stack lesson:

When do I need to remember the previous element?

Problems

1. Binary Search
2. Search Rotated Array
3. Find Minimum Rotated Array
4. Search 2D Matrix
5. Valid Parentheses
6. Min Stack
7. Daily Temperatures
8. Largest Rectangle Histogram

.NET

Stack<T>

Exceptions

Immutable collections

Design:

Browser History

---

# WEEK 4 — Linked Lists & Heaps

## Weekly Goal

Become comfortable manipulating pointers without drawing every node.

Heap lesson:

When do I repeatedly need the smallest/largest element?

Problems

1. Reverse Linked List
2. Merge Two Sorted Lists
3. Linked List Cycle
4. Reorder List
5. K Closest Points
6. Merge K Sorted Lists
7. Top K Frequent Words

.NET

PriorityQueue<TElement,TPriority>

Garbage Collection

IDisposable

Design

LRU Cache

---

# End of Phase 1 Assessment

You should be able to:

✓ Recognize the correct pattern within 2 minutes.

✓ Explain brute force before coding.

✓ Derive the optimal solution.

✓ Communicate tradeoffs.

✓ Implement clean Python and C# solutions.

If not, repeat the week's problems before moving on.
