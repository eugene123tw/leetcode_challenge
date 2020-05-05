# Bit Manipulation

* Objectives:
  * Be very comfortable with the **bitwise operators**, particularly XOR
  * Understand how to use **masks** and create them in an **machine independent** way
  * Know fast ways to **clear the lowermost set bit** (and by extension, set the lowermost  0, get it's index, etc)
  * Understanding signedness and its implications to **shifting**
  * Consider using a **cache** to accelerate operations by using it to brute-force small inputs
  * 

## Some useful debug functions

* Convert an integer number to a binary string prefixed with “0b”. Some examples:
```python
>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'
```

* Convert integer to bits and formats the output to fit in 10 characters width - 2 characters for `0b` prefix, 8 for rest binary digits. 
```python
>>> format(14, '#010b')
'0b00001110'
```

* Convert bits to integer
```python
>>> int('11111111', 2)
255
```

## AND `&` Operator (Set intersection)
### Masking
AND takes two equal-length bit patterns. If both bits in the compared position of the bit patterns are 1, the bit in the resulting bit pattern is 1, otherwise 0.

For example:

```
 A: 0000 0011 = 3
&B: 0000 0010 = 2
----------------------------
    0000 0010 = 2
```

From result `0010`, we know the second bit in the original pattern was set. This is often called bit **masking**. (In this case, the `0` values mask the bits that are not of interest). This operator can help us locate intersected bits between 2 patterns.

### Odd/Even number check (Parity check)
Because of the previous property, it becomes easy to check the [parity] of a binary number by using a mask equals to 1. 

```
 A: 0000 0011 = 3
&M: 0000 0001 = 1
----------------------------
    0000 0001 = 1
```
Because `3` AND mask (`M=1`) is one, which means `3` is not divisible by two and therefore odd.

Let's look another example with even number `6`:

```
 A: 0000 0110 = 6
&M: 0000 0001 = 1
----------------------------
    0000 0000 = 0
```

Because `6` AND mask (`M=1`) is zero, which means `6` is divisible by two and therefore even.

[Parity]: https://en.wikipedia.org/wiki/Parity_(mathematics)

## OR `|` operator (Set union)
* Syntax `x | y`: 
  * Returns each bit of the output 0 if the corresponding bit of `x` AND of `y` is `0`, otherwise it's `1`.

```
 A: 0000 0011 = 3
|B: 0000 0010 = 2
----------------------------
    0000 0011 = 3
```

## NOT `~` Operator
* Syntax `~x`: 
  * Returns the complement of `x` - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as `-x-1`.

It's an artifact of two's complement integer representation.

In 16 bits, 1 is represented as `0000 0000 0000 0001`. Inverted, you get `1111 1111 1111 1110`, which is -2 (-1-1). Similarly, 15 is `0000 0000 0000 1111`. Inverted, you get `1111 1111 1111 0000`, which is -16 (-15-1).

```
Origin: 0000 0000 0000 0001 = 1
Invert: 1111 1111 1111 1110 = -2 (in two's complement representation)
```

## XOR `^` Operator

Bitwise XOR also takes two equal-length bit patterns. If both bits in the compared position of the bit patterns are 0 or 1, the bit in the resulting bit pattern is 0, otherwise 1.  

```
 A: 0000 0101 
^B: 0000 0011
----------------------------
    0000 0110 
```

```
 A: 0101 
^B: 1010
----------------------------
    0000
```

> ref:  
> https://en.wikipedia.org/wiki/Two%27s_complement  
> https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%A3%9C%E6%95%B8  
> https://stackoverflow.com/questions/7278779/bit-wise-operation-unary-invert  
> https://stackoverflow.com/questions/14326900/how-does-c-do-bitwise-or-operations-on-negative-numbers


## Left Shifts `<<` operator

* Syntax: `x << y`: 
  * This returns `x` with the bits shifted to the left by `y` places (and new bits on the right-hand-side are zeros). This is the same as **multiplying** `x` by `2**y`.

For example, shift `x=26` 1 bit to the left (`y=1`), and shift 1 bit left again from the previous result.
```
>>> 26 << 1, 26 << 1 << 1
Origin: 0001 1010 = 26 
    LS: 0011 0100 = 26 * (2**1) = 52
    LS: 0110 1000 = 26 * (2**2) = 104
```

## Right Shifts `>>` operator

* Syntax: `x << y`: 
  * This returns `x` with the bits shifted to the right by `y` places (and new bits on the left-hand-side are zeros). This is the same as **dividing** `x` by `2**y`.

For example, shift `x=26` 1 bit to the right (`y=1`)
```
>>> 104 >> 1, 104 >> 1 >> 1
Origin: 0110 1000 = 104
    RS: 0011 0100 = 104 / (2**1) = 52
    RS: 0001 1010 = 104 / (2**2) = 26
```
As you can see we are back at 26 again! 

## Common usages

### Get Bit
* Syntax `(x & (1 << y)) != 0`:
  * Returns the `y+1`th bit you would like to get from `x`
    * `(1 << y)` creates a mask 1 located at `y+1`
    * Then mask `y+1`th bit with the mask we created above of `x` with `&` operator
    * This returns True if `y+1`th bit is 1, otherwise 0 

For example, get the 1st bit (`y=0`) of value 7 (`x=7`) (syntax: `(7 & (1 << 0)) != 0`): 
```
Origin: 0000 0111
     &
1 << 0: 0000 0001 
----------------------------
        0000 0001 
```

For example, get the 2nd bit (`y=1`) of value 7 (`x=7`) (syntax: `(7 & (1 << 1)) != 0`): 
```
Origin: 0000 0111
     &
1 << 1: 0000 0010 
----------------------------
        0000 0010 
```

### Set Bit
* Syntax `x | (1 << y)`:
  * Set the `y+1`th bit to 1 to `x`
    * `(1 << y)` creates a mask 1 located at `y+1`
    * Then set `y+1`th bit with the mask we created above of on `x` with `|` operator

For example, set the 4th bit (`y=3`) of value 7 (`x=7`) (syntax: `7 | (1 << 3)`): 
```
Origin: 0000 0111 = 7
     |
1 << 3: 0000 1000 
----------------------------
        0000 1111 = 15
```

### Clear Bit
* Syntax `x & ~(1 << y)`:
  * Clear the `y+1`th bit of `x`
    * `(1 << y)` creates a mask 1 located at `y+1`, then invert the mask with XOR
    * Then clear `y+1`th bit with the mask we created above of `x` with `&` operator

For example, set the 4th bit (`y=3`) of value 7 (`x=7`) (syntax: `7 | (1 << 3)`): 
```
Origin: 0000 0111 = 7
     |
1 << 3: 0000 1000 
----------------------------
        0000 1111 = 15
```


# 136. Single Number

Given an array of integers, every element appears twice except for one. Find that single one.

**Note:**
Your algorithm should have a linear runtime complexity.

> Could you implement it without using extra memory?

**Example:**
Input: [2,2,1]  
Output: 1

Input: [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]  
Output: 16

## My solution:

```py
class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1: return nums[0]
        sort_nums = sorted(nums) # Too much computation
        for i in range(0, len(nums), 2):
            if i >= len(nums) - 1:
                return sort_nums[-1]
            if sort_nums[i] != sort_nums[i + 1]:
                return sort_nums[i]
```

## Approach #2 Hash Table:

Runtime: 72 ms  
Time complexity: $O(n)$  
Space complexity: $O(n)$

```py
class Solution:
    def singleNumber(self, nums):
        hash = {}
        for i in range(0,len(nums)):
            if nums[i] not in hash:
                hash[nums[i]] = 0
            else:
                hash.pop(nums[i])

        return list(hash.keys())[0]
```

## Approach #3 Math:

Concept:

> 2 \* (a + b + c) - (a + a + b + b + c) = c  
> I don't know how to implement this

## Approach #4 Bit Manipulation:

XOR ( ^ ): Bitwise XOR takes two equal-length bit patterns. If both bits in the compared position of the bit patterns are 0 or 1, the bit in the resulting bit pattern is 0, otherwise 1.

Since $A \oplus 0 = A$,  
And, $A \oplus A = 0$,  
Then, $A \oplus B \oplus A = (A \oplus A) \oplus B = 0 \oplus B = B$

```py
class Solution:
    def singleNumber(self, nums):
        num = 0
        for i in range(0,len(nums)):
            num = operator.xor(num, nums[i])
        return num
```

or

```py
class Solution:
    def singleNumber(self, nums):

        return operator.xor(num, nums[i])
```

# 137. Single Number II

Given an array of integers, every element appears **three times** except for one, which appears **exactly once**. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example:**
Input: [2,2,3,2]
Output: 3

## Hash Table Solution:

Time complexity: $O(n)$  
Space complexity: $O(n)$

```py
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table={}

        for i in range(len(nums)):
            if nums[i] not in hash_table :
                hash_table[nums[i]]=1
            else:
                hash_table[nums[i]]+=1

        num = [k for k,v in hash_table.items() if v<3 ]
        return num[0]
```

## Bit Operation

The code makes use of 2 variables.

ones - At any point of time, this variable holds XOR of all the elements which have
appeared "only" once.  
twos - At any point of time, this variable holds XOR of all the elements which have
appeared "only" twice.

So if at any point time,

A new number appears - It gets XOR'd to the variable "ones".  
A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the
variable "twos".  
A number appears for the third time - It gets removed from both "ones" and "twos".  
The final answer we want is the value present in "ones" - coz, it holds the unique element.

So if we explain how steps 1 to 3 happens in the code, we are done.  
Before explaining above 3 steps, lets look at last three lines of the code,

```py
common_bit_mask = ~(ones & twos)
ones & = common_bit_mask
twos & = common_bit_mask
```

All it does is, common 1's between "ones" and "twos" are converted to zero.

```py
class Solution(object):
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            two = two | (one & x)
            one = operator.xor(one,x)
            common_bit_mask = ~(one & two)
            one, two = common_bit_mask & one , common_bit_mask & two

        return one
```

# 190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as `00000010100101000001111010011100`), return 964176192 (represented in binary as `00111001011110000010100101000000`).

Follow up:
If this function is called many times, how would you optimize it?

**Example**:
Input: 43261596  
Output: 964176192

## My solution:

```py
class Solution:
    def reverseBits(self, n):

        sum = 0
        count = 31
        remain = n
        list = []
        while remain>0:
            if remain%2==0:
                list.append(0)
            else:
                list.append(1)
                sum = sum + 1 * 2 ** count
            remain = remain//2
            count = count -1
        return sum
```

## Optimized solution

```py
class Solution:
    def reverseBits(self, n):
        result = 0
        mask = 1
        for i in range(32):
            result <<= 1
            result |= n&mask
            n>>=1
        return result
```

Algorithm:

1. Left shift `result`
2. Apply `mask` to filter the first bit of `n`
3. After masking, apply `or` operation with the masking result and `result`
4. Right shift `n`
5. Repeat

```py
# Example
Input: 0010
Output: 0100

Initialize:
    mask   = 0001
    result = 0000

Iteration1:
    result <<= 1,     result = 0000
    result |= n&mask, result = 0000|(0010&0001) = 0000
    n>>=1,            n      = 0001

Iteration2:
    result <<= 1,     result = 0000
    result |= n&mask, result = 0000|(0001&0001) = 0001
    n>>=1,            n      = 0000

Iteration3:
    result <<= 1,     result = 0010
    result |= n&mask, result = 0010|(0000&0001) = 0010
    n>>=1,            n      = 0000

Iteration4:
    result <<= 1,     result = 0100
    result |= n&mask, result = 0100|(0000&0001) = 0100
    n>>=1,            n      = 0000

Return: result= 0100
```

# 201. Bitwise AND of Numbers Range

Given a range `[m, n]` where `0 <= m <= n <= 2147483647`, return the bitwise AND of all numbers in this range, inclusive.
For example, given the range `[5, 7]`, you should return 4.

Hint: Just compare the leading digits of m,n if the leading digits match, return `2**i`

```py
Example = [m=5,n=7]
m = 0101
n = 0111
Iteration1:
    m!=n, m>>1 = 0010, n>>1 = 0011, fac = 1
Iteration2:
    m!=n, m>>1 = 0001, n>>1 = 0001, fac = 2
Iteration3:
    m==n(stop)
Result: (m&n)*2**fac
```

```py
import operator
from functools import reduce

class Solution:
    def rangeBitwiseAnd(self, m, n):
        fac = 0

        while(m!=n):
            m >>= 1
            n >>= 1
            fac+=1

        return (m&n)*2**fac
```
