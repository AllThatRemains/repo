# Deep merge
#
# - Write a function that takes two dictionaries and returns a new dictionary
#   containing the keys and values from both dictionaries.
# - Neither input should be modified.
# - If the key exists in both dictionaries...
#   ...merge the values if they are both dictionaries.
#   ...give the values in the second dictionary (b) precedence otherwise.

def merge(source, destination):

  for key, value in destination.items():
    if isinstance(value, dict):
      node = source.setdefault(key,{})
      merge(node, value)
    else:
      source[key] = value

  return source

# Input for tests
a = {
  "hello": "who?",
  "foo": {
    "bar": 1,
  },
  "first": True,
}

b = {
  "hello": "world!",
  "foo": {
    "baz": 2,
  },
  "second": False,
}

print merge(a, b)

'''
# Test that the merge gives us the expected results
assert merge(b, a) == {
  "hello": "world!",
  "foo": {
    "bar": 1,
    "baz": 2,
  },
  "first": True,
  "second": False,
}

# Test that we have not modified the input
assert a == {
  "hello": "who?",
  "foo": {
    "bar": 1,
  },
  "first": True,
}

assert b == {
  "hello": "world!",
  "foo": {
    "baz": 2,
  },
  "second": False,
}

print "All tests pass!"
'''
