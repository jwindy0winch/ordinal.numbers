# ordinal.numbers

# Overview
Program Requirements: 
●	Store the numbers 1-9 in a list 
●	Use a loop through the list
●	Use an if-elif-else chain inside the loop to print ordinal numbers 
●	Each printed ordinal number should be on a separate line

Defined Scope:
●	Print a series of ordinal numbers (1-9) each on separate lines with their corresponding suffixes

Intended Usage:
●	Create a numbered list of ordinal numbers for rankings (1-9)

# Processing Logic
Control of the Program:
This Python program defines a list ‘ordinal_numbers’ containing numbers 1 thru 9. The program iterates through the list of numbers using a ‘for’ loop. Using the modulo operator ‘%’ (this operator reviews the integer) in an if-elif-else chain the modulo operator reviews the integer and assigns the integer its correct suffix, saving it in the ‘ordinal’ variable. This is repeated in the loop for all numbers 1 thru 9. Last, a print statement concatenates the two variables (‘ordinal_numbers’, ‘ordinal’)  into the string using an f-string. END PROGRAM.

Data Flow of the Program:
●	Input: of  ‘ordinal_numbers’ list, using a range 1-9
●	Iteration: repeats through each numbered element in the ‘ordinal_numbers’ list
○	For each iteration, the modulo operator calculates the value of the ‘ordinal_numbers’ in the list and assigns a suffix to the ‘ordinal’ variable
●	Output: Prints formatted and concatenated ‘ordinal_numbers’ and ‘ordinal’ variables

# Process Specification
Program Design Language:
○	DEFINE ‘ordinal_numbers’ AS list with integers FROM 1 TO 9
○	FOR EACH ‘ordinal_number IN ordinal_numbers DO:
■	IF ‘ordinal_number’ MOD 10 EQUALS 1 THEN
●	SET ‘ordinal’ TO “st”
■	ELSE IF ‘ordinal_number’ MOD 10 EQUALS 2 THEN
●	SET ‘ordinal’ TO “nd”
■	ELSE IF ‘ordinal_number’ MOD 10 EQUALS 3 THEN
●	SET ‘ordinal’ TO “rd”
■	ELSE
●	SET ‘ordinal’ TO “th”
■	END IF output ‘ordinal_number’ concatenated WITH ‘ordinal 
○	END PROGRAM

Pseudo Code:
○	INITIALIZE ‘ordinal_numbers’ list with integers FROM 1 TO 9
○	FOR EACH ‘ordinal_number’ IN ‘ordinal_numbers’:
■	IF ‘ordinal_number MOD 10 EQUALS 1. SET ‘ordinal’ TO “st”
■	ELSE IF ‘ordinal_number’ MOD 10 EQUALS 2. SET ‘ordinal’ TO “nd”
■	ELSE IF ‘ordinal_number’ MOD 10 EQUALS 3. SET ‘ordinal’ TO “rd”
■	ELSE, SET ‘ordinal’ TO “th”
■	PRINT ‘ordinal_number’ CONCATENATED WITH ‘ordinal’
○	END LOOP
○	END PROGRAM

# Process Specification
Flow Chart
START:
○	INITIALIZE ‘ordinal_numbers list FROM 1 TO 9
■	LOOP EACH ‘ordinal_number’
○	Check IF ‘ordinal_number MOD 10 EQUALS 1
■	SET ‘ordinal’ TO “st”
■	PRINT CONCATENATED ‘ordinal_number’ + ‘ordinal’
○	Check IF ‘ordinal_number MOD 10 EQUALS 2
■	SET ‘ordinal’ TO “nd”
■	PRINT CONCATENATED ‘ordinal_number’ + ‘ordinal’
○	Check IF ‘ordinal_number MOD 10 EQUALS 3
■	SET ‘ordinal’ TO “rd”
■	PRINT CONCATENATED ‘ordinal_number’ + ‘ordinal’
○	ELSE SET ‘ordinal’ TO “th”
■	PRINT CONCATENATED ‘ordinal_number’ + ‘ordinal’
○	END IF
○	END LOOP 
END PROGRAM


Subroutines/Methods/Functions:
●	No Subroutines, methods, or functions used
Specific Algorithms:
●	Ordinal_numbers = list(range(1,10))
○	This algorithm creates a list of numbers from 1 to 9


# Data (INPUT/OUTPUT)
Element Descriptions:
●	‘Ordinal_numbers’: list containing numbers 1 to 9
○	Type: List of integers
○	Dimension: 1-dimensional
●	(LOOP) ‘ordinal_number’: represents each number in the ‘ordinal_numbers’ list while inside the loop
○	Type: List of integers
○	Dimension: Scalar
●	(LOOP) ‘ordinal’: represents ordinal suffixes
○	Type: String
○	Dimension: Scalar
●	‘print( )’: outputs ‘ordinal_number’ with corresponding ‘ordinal’ suffix
○	Type: Function
○	Dimension: Output
●	(PRINT) ‘f”{ordinal_number}{ordinal}”: creates correct formatting
○	Type: String
○	Dimension: Scalar

 Relationships between Elements:
●	‘Ordinal_numbers’: Input List
●	(LOOP) ‘ordinal_number’: derived from ‘ordinal_numbers’list from outside the Loop
●	(LOOP) ‘ordinal’: derived from modulo operator then applied to ‘ordinal_number’
●	‘print( )’: derived from ‘ordinal_number’ with corresponding ‘ordinal’ suffix
●	(PRINT) ‘f”{ordinal_number}{ordinal}”: derived from ‘ordinal_number’ and ‘ordinal’

Range of Possible Values:
●	‘Ordinal_numbers’: 1,2,3,4,5,6,7,8,9
●	(LOOP) ‘ordinal_number’: 1,2,3,4,5,6,7,8,9
●	(LOOP) ‘ordinal’: st, nd, rd, th
●	‘print( )’: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
●	(PRINT) ‘f”{ordinal_number}{ordinal}”: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th

Initial Values of Each Element:
●	‘Ordinal_numbers’: 1,2,3,4,5,6,7,8,9
●	(LOOP) ‘ordinal_number’: 1,2,3,4,5,6,7,8,9
●	(LOOP) ‘ordinal’: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
●	‘print( )’: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
●	(PRINT) ‘f”{ordinal_number}{ordinal}”: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th

# Software Components
●	Number Generator: to generate ordinal numbers with their corresponding suffixes

UML Class Diagram:
●	Number Generator
○	Ordinal_numbers list (Integers)
○	Generate_ordinals: Print Function

Properties and Constraints:
●	‘Ordinal_numbers’: list containing numbers 1 to 9
○	Type: List of integers
○	Constraints: Integers must range from 1 to 9

Algorithms defined in Processing Logic:
●	‘If-elif-else’: Conditional Statement that generates ordinal numbers from ‘ordinal_numbers’ list and the ‘ordinal’ variable then proceeds to print them. 
# Testing
Input Data:
●	‘Ordinal_numbers’ = 1,2,3,4,5,6,7,8,9,25,39,61etc
Expected Output Data:
●	1st, 5th, 9th, 25th, 39th, 61st, etc
Success Criteria:
●	Output matches expected output for each ordinal number
●	Handles all special cases correctly
