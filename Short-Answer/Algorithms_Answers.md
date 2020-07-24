#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) For `n*n*n = n^3`, as `n` gets bigger, the amount of loops in the while loop increases exponentially. However, in the loop, value `a` increases by `a+n*n` in each iteration, which reduces the amount of loop down to `n*n*n*/(a+n*n)`, which is less than `n`. We can drop whatever constant `n` has after and call it `O(n)` complexity.

b) First for loop has the time complexity of `0(n)`. The inner while loop can be considered `O(log n)` because value `j` is doubling in each iteration. Doubling/halving behavior always gets `O(log n)` time complexity since the amount of change is increasing/decreasing in double/half amount of the input.

c) This is a classic recursive operation. The function calls itself only once with `(n-1)` parameter in its return statement. Therefore, The stack size will be directly proportinal to the input size since the base case is `n = 0`. Time complexity is `O(n)`

## Exercise II

If the speed of finding the safe floor is a concern, my naive approach would be a binary search. I would half the value `n` in a while loop and compare it to `n` until `n` is equal to `f`. In the worst case scenario in such a program, I would only break `log n` amount of eggs to find the safe floor.

If we are stingy on the eggs, then the optimal solution would be:
Start dropping eggs from floor 1 all the way up until it breaks. That way when the egg breaks, that is the floor number we are looking for. In this case, we would break only one egg but the time complexity of this solution would be `O(n)` since in the first case scenario, the last floor maybe what we are looking for.

However, mathmatically, there is an optimal solution if we are being greedy with both eggs and amount of tries.
`n(n+1)/2` gives us the sum of arithmetically increasing numbers. `(n=4 => 1+2+3+4)`
I would find the `n` in this equation for the number of maximum floors.
Let's say there is 100 floors. I would find the sum of `n` numbers that would be less than or equal to the floor number, 100. (1+2+3+4+5+.....+13)
I would start a counter from 1 and start throwing eggs starting from the biggest number in the sequence (13) and increase my counter by that number if it doesn't break.
Let's say we throw it from floor 13 and it did not break. We increase the counter by 13 (now it's 14) and this time throw it from 13+12 (25th) floor (also save this value for maximum tried floor value). Let's assume it broke. This time, we start throwing eggs from the last counter value by increasing the floor one each time until we find the `f`. So far we know that value `f` is greater than or equal to our counter value and less than our maximum tried floor.
Maximum try it would take to find the floor is:
`n(n+1)/2 + (max_floor - n(n+1)/2)`
