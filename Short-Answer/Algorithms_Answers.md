#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) I believe the time complexity to be O(n) because although we have a loop that is O(n**3) we have an operation being done inside that is
decreasing our number of operations by O(a + n**2) ignoring the constant being a it will be O(n**2) so we are decreasing our number of steps by
O(n**2) every time

b) The time complexity for this function is O(nlogn) because we are going throught the entire input for the for loop O(n) and inside the while loop
we are going through the loop at double the iterator each step so we are halving the work we have to do every time. so O(n \* logn) = O(nlogn)

c) The function is a recursive one that only decreases the input by 1 each time it passes through to the next recursive call so the time complexity is
O(n)

## Exercise II

I think the strategy I would use is a guess where I would take between the highest and lowest floors drop and egg and see if it breaks and if it breaks
then I drop halway between the floor I just dropped from and the ground until it doesn't break then I would go back up half way until I eventually meet
a point that I would call f where if I went one higher it would break but not the current floor

Start at random floor
repeat line below until I reach floor f
if breaks go down halway between ground and current floor
if doesn't break go up half way between ground and where I last broke egg

The time complexity should be O(logn) it takes on the idea of the binary search guessing and so I am halving my choices every time. No matter how
many floors the building would have this would be the best way to break a minimal number of eggs
