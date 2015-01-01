<?php

$a = 0; $b = 1; $c = 0; $d = 0;
while ($c < 3500000)
{
	$c = $a + $b;
	$a = $b;
	$b = $c;
	if ($c % 2 == 0)
	{
		$d += $c;
	}
}	echo "The sum of all EVEN fibonacci values under 4 million is: " + $d; // Expected answer: 4613732
?>
