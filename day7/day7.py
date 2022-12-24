# How the file tree will be represented
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
PWD = []

# Missing Ruby right now
def dig(self, *keys):
  for key in keys:
    if type(self) in [dict, list]:
      self = self[key]
    else:
      raise IndexError('Bad index')
  return self

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

        process_output(f, pwd, FILE_SYSTEM)

with open('./input.txt') as f:
  # Current working directory
  pwd = []

  # Skip the first line which is:
  # $ cd /
  f.readline()

  process_output(f, pwd, FILE_SYSTEM)

print(FILE_SYSTEM)

# Get rid of files in the root dir
# We don't need to count them
# for k,v in FILE_SYSTEM.copy().items():
#   if isinstance(v, int):
#     del FILE_SYSTEM[k]
