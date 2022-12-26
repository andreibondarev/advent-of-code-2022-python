LINE_LENGTH = 99 - 1 # Counting position 0

def is_visible(forest, row_idx, tree_idx, count):
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

with open('./input.txt') as f:
  forest = []
  visible_tree_count = 0

  for line in f:
    row = line.strip()
    # Break each row into an array and append to the forest layout
    forest.append(list(row))

  for row_idx, row in enumerate(forest):
    for tree_idx, item in enumerate(row):
      if is_visible(forest, row_idx, tree_idx, visible_tree_count):
        visible_tree_count += 1

  print(visible_tree_count)