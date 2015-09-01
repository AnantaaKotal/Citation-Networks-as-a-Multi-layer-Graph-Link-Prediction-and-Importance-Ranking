def find_str(s, char):
    index = 0

    if char in s:
        char = char[0]
        for ch in s:
                if ch in s:
                    index += 1
                if ch == char:
                        return index

    else:
	 return -1

