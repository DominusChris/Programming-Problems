local sum = 0
for index = 3, 1000 - 1 do
  if index%5 == 0 or index%3 == 0 then
    sum = sum + index
  end
end
print(sum)
-- 233168