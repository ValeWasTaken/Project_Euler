var answer = 0;
for (var x=0; x<1000; x++)
{
        if(x % 5 === 0 || x % 3 === 0)
        {answer += x;}
}
alert("The sum of all multiples of 3 or 5 below 1000 is: " + answer); // The answer should be: 233168
