# Project Euler #3: Largest Prime Factor - Step by Step Solution

## Problem Statement
Find the largest prime factor of the number 600851475143.

## Understanding the Problem
A prime factor is a prime number that divides the given number exactly. We need to find all prime factors and return the largest one.

## Algorithm Approach

### Step 1: Optimize with Factor of 2
- Check if the number is even
- If yes, divide by 2 repeatedly until it becomes odd
- Keep track of the largest factor found (initially 2 if applicable)

### Step 2: Check Odd Factors
- Start from 3 and check only odd numbers
- For each potential factor `factor`, divide the number while `factor` divides it evenly
- Update the largest factor when a new one is found
- Only check up to √n for efficiency

### Step 3: Handle Remaining Prime
- If after all divisions, the remaining number is > 1, it's a prime factor
- This remaining number would be the largest prime factor

## Time Complexity
- O(√n) - We only check factors up to the square root of n
- Much more efficient than checking all numbers up to n

## Example Walkthrough
For n = 600851475143:
1. Not divisible by 2, so skip Step 1
2. Check odd factors: 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...
3. Find factors and keep dividing
4. The largest prime factor will be 6857

## Key Insights
- We don't need to check if each factor is prime - the algorithm naturally finds prime factors
- By dividing out each factor completely, we ensure we only get prime factors
- The remaining number after all small factors are removed is guaranteed to be prime (if > 2)
