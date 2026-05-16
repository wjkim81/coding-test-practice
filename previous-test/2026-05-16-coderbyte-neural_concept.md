## 1. Moving Median

Create a function `ArrayChallenge(arr)` to perform a Moving Median on the array of integers stored in `arr` which will contain an odd number of integers. The first element in the array is the size of the window for the moving median. For example:

If `arr` is `[3, 1, 3, 5, 10, 6, 4, 3, 1]`

then the window size is `3` and there are `3` moving windows of medians:

* `[1]` → median = `1`
* `[1,3]` → median = `2`
* `[1,3,5]` → median = `3`
* `[3,5,10]` → median = `5`
* `[5,10,6]` → median = `6`
* `[10,6,4]` → median = `6`
* `[6,4,3]` → median = `4`
* `[4,3,1]` → median = `3`

Therefore your program should return:

```text
1,2,3,5,6,6,4,3
```

---

## 2. Caesar Cipher

Create a function `StringChallenge(strParam, num)` that takes the `strParam` parameter being passed and returns a Caesar Cipher shift by `num`.

A Caesar Cipher works by shifting each letter in the string `num` positions in the alphabet.

Examples:

```text
Input: ("Hello", 4)
Output: Lipps
```

```text
Input: ("abc", 1)
Output: bcd
```

Rules:

* Preserve uppercase/lowercase
* Non-alphabetic characters remain unchanged
* Wrap around alphabet:

  * `z + 1 -> a`
  * `Z + 1 -> A`

---

## 3. Array Rotation

Create a function `ArrayChallenge(arr)` that rotates the array to the left by the number stored in the first element.

Example:

```text
Input: [3,2,1,6]
```

* Rotate left by `3`
* Result:

  * `[6,3,2,1]`

Return the final result as a concatenated string:

```text
6321
```

Another example:

```text
Input: [2,4,5,6,7]
Output: 6745
```

---

## 4. Equal Set Partition

Create a function `ArrayChallenge(arr)` that takes an array of positive integers and determines whether it can be split into two sets of equal size such that the sum of both sets is equal.

If there are two sets, return the integers separated by commas in the following format:

```text
set1,set2
```

Where:

* Each set is sorted in ascending order
* The set whose first element is smaller should appear first

Example:

```text
Input: [1,2,3,4]
```

Possible partition:

```text
[1,4] and [2,3]
```

Both have:

* equal size (`2`)
* equal sum (`5`)

Return:

```text
1,4,2,3
```

If no valid partition exists, return:

```text
-1
```
