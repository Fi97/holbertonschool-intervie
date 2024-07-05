def canUnlockAll(boxes): 
    Keys = [0]
    for key in Keys:
        for boxKey in boxes[key]:
            if boxKey not in Keys and boxKey < len(boxes):
                Keys.append(boxKey)
    if len(Keys) == len(boxes):
        return True
    return False
      

