<?php

$answer = 0;
for ($x = 0; $x<1000; $x++)
{
	if ($x % 5 == 0 || $x % 3 == 0)
	{
		$answer += $x;
	}
}
echo "The sum of all multiples of 3 and 5 is $answer."; // The answer should be 233168.
?>
