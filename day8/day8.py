LINE_LENGTH = 99 - 1 # Counting position 0
# Constant to be used for example.txt
# LINE_LENGTH = 5 - 1 # Counting position 0

def is_visible(forest, row_idx, tree_idx):
  # Trees on the edges are always visible
  if (row_idx == 0) or (tree_idx == 0) or (row_idx == LINE_LENGTH) or (tree_idx == LINE_LENGTH):
    return(True)
  else:
    columns_top =  [ forest[idx][tree_idx] for idx in range(row_idx) ] 
    columns_bottom = [ forest[idx][tree_idx] for idx in range(row_idx+1, LINE_LENGTH+1) ]

    # Check to the left
    if max(forest[row_idx][:tree_idx]) < forest[row_idx][tree_idx]:
      return(True)
    # Check to the right
    elif max(forest[row_idx][tree_idx+1:]) < forest[row_idx][tree_idx]:
      return(True)
    # Check the top
    elif max(columns_top) < forest[row_idx][tree_idx]:
      return(True)
    # Check the bottom
    elif max(columns_bottom) < forest[row_idx][tree_idx]:
      return(True)

    return(False)

def calculate_scenic_side_score(current_tree, columns):
  score = 0

  for tree in columns:
    if int(tree) < int(current_tree):
      score += 1
    elif int(tree) >= int(current_tree):
      score += 1
      break

  return score

def calculate_scenic_score(forest, row_idx, tree_idx):
  columns_top =  [ forest[idx][tree_idx] for idx in range(row_idx) ] 
  columns_bottom = [ forest[idx][tree_idx] for idx in range(row_idx+1, LINE_LENGTH+1) ]
  columns_left = forest[row_idx][:tree_idx]
  columns_right = forest[row_idx][tree_idx+1:]

  current_tree = forest[row_idx][tree_idx]

  # Calculate top
  columns_top.reverse()
  top_score = calculate_scenic_side_score(current_tree, columns_top or [])
  # Calculate bottom
  bottom_score = calculate_scenic_side_score(current_tree, columns_bottom or [])
  # Calculate left
  columns_left.reverse()
  left_score = calculate_scenic_side_score(current_tree, columns_left or [])
  # Calculate right
  right_score = calculate_scenic_side_score(current_tree, columns_right or [])

  return(top_score * bottom_score * left_score * right_score)

with open('./input.txt') as f:
  forest = []
  visible_tree_count = 0
  max_scenic_score = 0

  for line in f:
    row = line.strip()
    # Break each row into an array and append to the forest layout
    forest.append(list(row))

  for row_idx, row in enumerate(forest):
    for tree_idx, item in enumerate(row):
      if is_visible(forest, row_idx, tree_idx):
        visible_tree_count += 1

      scenic_score = calculate_scenic_score(forest, row_idx, tree_idx)
      if scenic_score > max_scenic_score:
        max_scenic_score = scenic_score

  print(max_scenic_score)