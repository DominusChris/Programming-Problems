class Main {
  public static void main(String[] args) {
    int sum = 0;
    for (int index = 3; index < 1000; index++)
    {
      if (index%3 == 0 || index%5 == 0)
      {
        sum += index;
      }
    }
    System.out.println(sum);
    // 233168
  }
}