function r=fib(n)

if n==1 || n==2,
	r=1;
else,
	r=fib(n-1)+fib(n-2);
end;
