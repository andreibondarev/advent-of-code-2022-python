# How the file tree will be represented
# "i": 583 # <= file
# "e": { ... } # <= directory
example = {
  "a": {
    "e": {
      "i": 583
    },
    "f": 29116,
    "g": 2557,
    "h.lst": 62596
  },
  "b.txt": 14848514,
  "c.dat": 8504156,
  "d": {
    "j": 4060174,
    "d.log": 8033020,
    "d.ext": 5626152,
    "k": 7214296
  }
}

GO_UP = '..'
FILE_SYSTEM = {}

def dig(self, *keys):
  """
  Method to traverse the hash by specifying multiple keys

  :self: The hash itself
  :*keys: N hash key names
  :return: Hash key value
  """
  for key in keys:
    if type(self) in [dict, list]:
      self = self[key]
    else:
      raise IndexError('Bad index')
  return self

DIR_SIZES = {}
def calculate_dir_size(pwd, size):
  # Copy the original pwd to avoid directly modifying it
  path_array = pwd.copy()

  # As we go up the pwd tree,
  # adds up directory size and pop off an element 
  # for the next iteration
  while len(path_array) > 0:
    path = ''.join(path_array)
    if DIR_SIZES.get(path):
      DIR_SIZES[path] += int(size)
    else:
      DIR_SIZES[path] = int(size)
    
    path_array.pop()

  # import pdb; pdb.set_trace()

def process_output(f, pwd, FILE_SYSTEM):
  output = f.readline().strip()

  if output:

    if output.startswith('$'): # User command
      # Strip the $
      output = output.replace('$ ', '')

      if output == 'ls':
        process_output(f, pwd, FILE_SYSTEM)

      elif output.startswith('cd'):
        _, destination_dir = output.split(' ')
        if destination_dir == GO_UP:
          pwd.pop()
        else:
          pwd.append(destination_dir)

        process_output(f, pwd, FILE_SYSTEM)

    else: # Not user command
      if output.startswith('dir'):
        _, dir_name = output.split(' ')

        dig(FILE_SYSTEM, *pwd)[dir_name] = {}

        process_output(f, pwd, FILE_SYSTEM)
      else:
        size, file_name = output.split(' ')
        
        dig(FILE_SYSTEM, *pwd)[file_name] = size

        calculate_dir_size(pwd, size)

        process_output(f, pwd, FILE_SYSTEM)

with open('./example.txt') as f:
  # Current working directory
  pwd = []

  # Skip the first line which is:
  # $ cd /
  f.readline()

  process_output(f, pwd, FILE_SYSTEM)

total = 0
for k,v in DIR_SIZES.items():
  if v <= 100000:
    total += v
print(total)
