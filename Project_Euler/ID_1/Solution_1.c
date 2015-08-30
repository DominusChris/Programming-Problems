#include <stdio.h>
int main()
{
  int sum = 0;
  int index;
  for (index = 3; index < 1000; index++)
  {
    if (index%3 == 0 || index%5 == 0)
    {
      sum += index;
    }
  }
  printf("%d\n", sum);
  // 233168
  return 0;
}