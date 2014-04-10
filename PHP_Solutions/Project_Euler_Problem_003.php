<?php

$num = 600851475143;
$x = 2;

while ($x * $x < $num)
{
	while($num % $x == 0)
	{
		$num = $num / $x;
	}
	$x++;
}

echo "$num"; // This should output "6857"
?>
