<?php

// Start of "Square of sums" block
$n = 0;
for($x = 0; $x < 101; $x++)
{
	$n += $x;
}
$final_num = $n*$n;
echo "The square of the sum of the first 100 natural numbers is $final_num</br>"; // Expected output: 25502500

// Start of "Sum of squares" block
$num = 0;
for($y = 0; $y < 101; $y++)
{
	$num += ($y*$y);
}
echo "The sum of the squares of the first 100 natural numbers is: $num</br>"; // Expected output: 338350

// Final calculation
$difference = $final_num - $num;
echo "The difference between the two sums is: $difference</br>"; // Expected output 25164150
?>
