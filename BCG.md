## 🧠 BCG CodeSignal Kit: Concepts, Notes, Patterns & Practice Problems

---

### ✅ 1. String Manipulation (Module 1)

#### 🔹 Concepts:

* Reversing strings
* Checking palindromes
* Substring operations
* Character filters (`isalnum`, `isalpha`)

#### 🔹 1-Liner Patterns:

```python
s[::-1]                              # Reverse string
''.join(reversed(s))                # Another way to reverse
''.join(filter(str.isalnum, s))     # Keep only alphanumerics
```

#### 🔹 Practice Problems:

* [FizzBuzz](https://leetcode.com/problems/fizz-buzz/)
* [Add Digits](https://leetcode.com/problems/add-digits/)
* [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
* [Reverse String](https://leetcode.com/problems/reverse-string/)
* [Reverse Integer](https://leetcode.com/problems/reverse-integer/)
* [First Unique Character](https://leetcode.com/problems/first-unique-character-in-a-string/)
* [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)
* [Ransom Note](https://leetcode.com/problems/ransom-note/)

---

### ✅ 2. HashMap & Frequency Counting (Module 2)

#### 🔹 Concepts:

* `dict` for value lookup
* `collections.Counter`
* Grouping with dict
* Tuple/hashable key use

#### 🔹 1-Liner Patterns:

```python
Counter(s)                       # Count freq of characters
''.join(sorted(s))              # For anagram grouping
sorted(d.items(), key=lambda x: x[1])  # Sort dict by values
```

#### 🔹 Practice Problems:

* [Two Sum](https://leetcode.com/problems/two-sum/)
* [Group Anagrams](https://leetcode.com/problems/group-anagrams/)
* [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
* [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
* [Majority Element](https://leetcode.com/problems/majority-element/)
* [Sort Characters by Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
* [Custom Sort String](https://leetcode.com/problems/custom-sort-string/)
* [Find the Difference](https://leetcode.com/problems/find-the-difference/)

---

### ✅ 3. 2D Arrays & Matrix Traversal (Module 3)

#### 🔹 Concepts:

* Row/column scanning
* In-place update vs extra space
* Spiral, diagonal traversal

#### 🔹 1-Liner Patterns:

```python
zip(*matrix)                     # Transpose matrix
matrix[::-1]                     # Reverse rows
list(map(list, zip(*matrix)))    # Convert to list of lists after transpose
```

#### 🔹 Practice Problems:

* [Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse/)
* [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
* [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
* [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)
* [Rotate Image](https://leetcode.com/problems/rotate-image/)
* [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
* [Word Search](https://leetcode.com/problems/word-search/)
* [Flood Fill](https://leetcode.com/problems/flood-fill/)

---

### ✅ 4. Sliding Window & Two Pointers (Module 4)

#### 🔹 Concepts:

* Fixed-length and variable window
* Window expansion/shrinkage
* Longest/shortest substrings

#### 🔹 1-Liner Patterns:

```python
while right < len(s):
    # expand window, then shrink if needed
    if condition: left += 1
```

#### 🔹 Practice Problems:

* [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
* [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
* [Longest Substring Without Repeating](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
* [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
* [Permutation in String](https://leetcode.com/problems/permutation-in-string/)
* [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
* [3Sum](https://leetcode.com/problems/3sum/)

---

### ✅ 5. Prefix Sum, Sorting, Greedy & Intervals (Module 4 contd)

#### 🔹 Concepts:

* Prefix sum array
* Custom sort with lambda
* Interval merge logic
* Basic greedy for profit

#### 🔹 1-Liner Patterns:

```python
prefix = [0] * (len(nums)+1)
for i in range(1, len(prefix)): prefix[i] = prefix[i-1] + nums[i-1]
```

#### 🔹 Practice Problems:

* [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)
* [Merge Intervals](https://leetcode.com/problems/merge-intervals/)
* [Insert Interval](https://leetcode.com/problems/insert-interval/)
* [Sort Colors](https://leetcode.com/problems/sort-colors/)
* [Sort Integers by Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)
* [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)