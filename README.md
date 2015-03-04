MPCS 50101: Homework for Week 9
===============================

### Bubble Sort

Open the `bubble_sort.py` file.

1. Make the code all of the assertions pass.
2. Modify the print() statement at the bottom of the file to display the Big-O notation for this algorithm.

The bubble-sort strategy is as follows:

1. Go through every element in the list.
2. For each element, compare it to the element following it.
3. If necessary, swap those two elements, and advance to the next element.
4. If you make it through the entire list without doing any swaps, then the list is sorted.

#### Here's an example

Let us take the array of numbers "6 1 4 2 9", and sort the array from lowest number to greatest number using bubble sort. In each step, elements written in bold are being compared. Three passes will be required.

**First Pass:**

( **6 1** 4 2 9 ) --> ( **1 6** 4 2 9 ), Swap since 6 > 1.

( 1 **6 4** 2 9 ) --> ( 1 **4 6** 2 9 ), Swap since 6 > 4

( 1 4 **6 2** 9 ) --> ( 1 4 **2 6** 9 ), Swap since 6 > 2

( 1 4 2 **6 9** ) --> ( 1 4 2 **6 9** )

**Second Pass:**

( **1 4** 2 6 9 ) --> ( **1 4** 2 6 9 )

( 1 **4 2** 6 9 ) --> ( 1 **2 4** 6 9 ), Swap since 4 > 2

( 1 2 **4 6** 9 ) --> ( 1 2 **4 6** 9 )

( 1 2 4 **6 9** ) --> ( 1 2 4 **6 9** )

Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.

**Third Pass**

( **1 2** 4 6 9 ) --> ( **1 2** 4 6 9 )

( 1 **2 4** 6 9 ) --> ( 1 **2 4** 6 9 )

( 1 2 **4 6** 9 ) --> ( 1 2 **4 6** 9 )

( 1 2 4 **6 9** ) --> ( 1 2 4 **6 9** )

Good luck and have fun!  Post a message to Piazza if you have any questions.


