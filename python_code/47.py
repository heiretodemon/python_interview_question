if hasattr(Parent, 'x'):
    print(getattr(Parent, 'x'))
    setattr(Parent, 'x', 3)

print(getattr(Parent, 'x'))