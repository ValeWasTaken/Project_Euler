<?php

$num = 1;
$solutionFound = false;

while(!$solutionFound)
{
	$count = 0;
	for($x = 1; $x < 21; $x++)
	{
		if($num % $x != 0)
		{	
			$count += 1;
			break;
		}
	}
	if($count == 0)
	{
		echo "The smallest multiple is $num"; // This should output 232792560.
		$solutionFound = true;
	}
	$num++;
}

?>
