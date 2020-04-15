## Define string:
myString = "ab-cd!ghi*qqm"

## Define function to process string:
def specialReversalForDeepti(StringToReverse):
	
	## 0. Ask the user how they ant the program to work
	nonAlpabetCharactersKeepExactIndex = input('Enter "1" if non alpabetic characters should keep their exact index positions.\nEnter "2" if the grouping of characters should stay together\n\nEnter 1 or 2: ')
	
	
	## 1. Get the indexes of all the non alphabetic characters:
	indexList = [] ## Store indexes in this list
	indexCounter = 0
	for i in StringToReverse:
		if i not in 'abcdefghijklmnopqrstuvwxyz1234567890':
			indexList.append(indexCounter)
			indexCounter += 1
		else:
			indexCounter += 1
		
	## 2. Start assembling the groups of letters together reversed: 
	groupingLengths = []
	newString = ''
	counter = 0
	for i in indexList:
		if counter == 0:
			temp = StringToReverse[:i]
			counter = i
			for i in temp:
				newString = i + newString
			groupingLengths.insert(0, len(temp))
		else:
			temp = StringToReverse[counter + 1:i]
			counter = i
			for i in temp:
				newString = i + newString
			groupingLengths.insert(0, len(temp))

	## 3. Special case to get the final letter grouping:
	temp = StringToReverse[indexList[-1] + 1:]
	for i in temp:
		newString = i + newString
	groupingLengths.insert(0, len(temp))


	## 4. Convert new string into a list so you can insert non alphabet characters at specific indexes:
	newString = list(newString)
	
	if nonAlpabetCharactersKeepExactIndex == 1:		
		for i in indexList:
			character = StringToReverse[i]
			newString.insert(i, character)
	else:
		special = 0
		counter = 0
		for i in indexList:
			if counter == 0:
				character = StringToReverse[i]
				newString.insert((groupingLengths[counter]), character)
				counter += 1
				special += groupingLengths[counter]
			else:
				character = StringToReverse[i]
				newString.insert(special + counter + groupingLengths[counter], character)
				counter += 1
				special += 1 + groupingLengths[counter]
					
		
	## 5. Join newString backtogether into a string type for final output.
	newString = ''.join(newString)

	## 6. Return the final output
	return newString

## Begin Main Code:
print(specialReversalForDeepti(myString))