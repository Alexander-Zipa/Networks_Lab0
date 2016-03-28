clear;
clc;

n=1000;
p=0.2;
A=zeros(100);
for i = 1:n
    for j = 1:n
        if (i~=j) && (rand<p)
            A(i,j) = 1;
        end
    end
end

for i = 1:n
    k(i) = 0;
    for j = 1:n
        k(i) = k(i) + A(i,j);
    end
end

s=zeros(max(k));
for i = 1:n
    s(k(i)) = s(k(i)) + 1;
end

plot(1:max(k),s);