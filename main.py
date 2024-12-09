# Griffin King
# 

from StackClass import ArrayStack
import os


def main():
  original = "Sphinx of black quartz, judge my vow"
  new = ""
  
  stack = ArrayStack()
  for a in range(len(original)):
    stack.push(original[a])
  for a in range(len(stack)):
    new += stack.top()
    stack.pop()
  
  print("\n\n<>-----------------")
  print(f"  Original Text: {original}\n")
  print(f"  Reversed Text: {new}")
  print("<>-----------------\n\n")


if __name__ == "__main__":
    os.system("clear")
    main()