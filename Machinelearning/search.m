function pos=search(name,k)

load(name);
n=length(name);
for i=1:n,
	if name(i)==k,
		pos=i;
		break
	end,
end,
