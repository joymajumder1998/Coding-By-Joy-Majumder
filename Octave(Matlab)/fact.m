function y=fact(n)

if n==0,
	y=1;
else
	y=n*fact(n-1);
end;
