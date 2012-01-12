

def one_full_row(n, width):
  return row_divider(width, [False] * n)

def calculate_row_connections(n, rules, row):
  return [is_connected_bottom(n*row+col, rules, n) for col in xrange(n)]

def is_connected_bottom(square, rules, n):
  if (square + n < n*n and
      search_rules(rules, square) == search_rules(rules, square+n)):
    return True
  else:
    return False

def row_divider(width, connections):
  tile = '-' * width
  empty = ' ' * width
  result = '#'
  for is_connected in connections:
    if is_connected:
      result += empty
    else:
      result += tile
    result += '#'
  return result + '\n'

def pad_to_n_left(s, n):
  return s + ' ' * (n - len(s))
def pad_to_n_right(s, n):
  return ' ' * (n - len(s)) + s

def search_rules(rules, square):
  for r in rules:
    if square in r[2]:
      return r

def is_connected_right(square, rules, n):
  if ((square+1) % n != 0
      and search_rules(rules, square+1) == search_rules(rules, square)):
    return True
  else:
    return False

def get_connector(square, rules, n):
  if is_connected_right(square, rules, n):
    return ' '
  else:
    return '|'

def get_text(results, square):
  if square < len(results):
    return str(results[square])
  else:
    return ''

def square_expression(rules, square):
  rule = search_rules(rules, square)
  if rule == None:
    return ''
  return str(rule[1])+rule[0]

def format_board(n, rules, results=[]):
  width = 12
  height = int(width/3.0+0.5)
  result = one_full_row(n, width)
  for row in xrange(n):
    thisrow = ''
    for i in xrange(height):
      thisrow += '|'
      for col in xrange(n):
        square = row*n+col
        if i == 0:
          text = square_expression(rules, square)
          thisrow += pad_to_n_left(text,width)
        elif i == height-1:
          text = get_text(results, square)
          thisrow += pad_to_n_right(text,width)
        else:
          thisrow += ' '*width
        thisrow += get_connector(square, rules, n)
      thisrow += '\n'
    row_connections = calculate_row_connections(n, rules, row)
    result += thisrow + row_divider(width, row_connections)
  return result

## Test code
def test_print_board():
  rules2 = [
      ('+', 5, [0,1,2]),
      ('*', 1, [3])
      ]
  rules3 = [
      ('+', 5, [0,3]),
      ('+', 3, [1,2]),
      ('+', 3, [4]),
      ('+', 4, [5,8]),
      ('+', 3, [6,7]),
      ]
  rules4 = [
      ('-', 1, [0,1]),
      ('*', 24, [2,5,6]),
      ('-', 1, [3,7]),
      ('/', 2, [4,8]),
      ('+', 5, [9,10,14]),
      ('*', 12, [11,15]),
      ('-', 2, [12,13])
      ]
  print format_board(2, rules2, ["You","can","write","here"])
  print format_board(4, rules4)
  print format_board(3, rules3)

if __name__ == "__main__":
  test_print_board()
