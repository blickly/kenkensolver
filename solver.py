import prettyprinter

def get_solution(rules, n):
  # FIXME: Write a real solver!
  return [0]*(n*n)

def solve(rules, n):
  print "For a starting board of:"
  print prettyprinter.format_board(n, rules)
  print "The solution is:"
  solution = get_solution(rules, n)
  print prettyprinter.format_board(n, rules, solution)

def main():
  rules4 = [
      ('-', 1, [0,1]),
      ('*', 24, [2,5,6]),
      ('-', 1, [3,7]),
      ('/', 2, [4,8]),
      ('+', 5, [9,10,14]),
      ('*', 12, [11,15]),
      ('-', 2, [12,13])
      ]
  solve(rules4, 4)

if __name__ == "__main__":
  main()
