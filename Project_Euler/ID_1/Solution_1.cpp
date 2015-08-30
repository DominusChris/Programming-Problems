#include <iostream>
int main() 
{
  int sum = 0;
  for (int index = 3; index < 1000; index++)
  {
    if (index%3 == 0 || index%5 == 0)
    {
      sum += index;
    }
  }
	std::cout << sum << "\n";
	// 233168
	return 0;
}