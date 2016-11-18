-- Doubles a number
double x = x + x

-- Doubles two numbers and adds them
doubleAndSum x y = double x + double y

-- Doubles a number iff it is equal to or less than 100
doubleIfSmall x = if x < 101 then double x else x
 
-- Returns a list containing the values of the input doubled
doubleList y = [double x | x <- y]

-- Returns a list containing the values of the input that are less than 5, doubled
doubleSmallListValues y = [double x | x <- y, x < 5]

-- Returns a list containing the odd values of the input that are less than 5, doubled
doubleOddSmallListValues y = [double x | x <- y, x < 5, odd x]

-- Returns triples containing the lengths of the sides of the right-angled triangles that have sides 10 units or shorter, and a perimeter of 24
smallRightTriangles = [ (a,b,c) | c <- [1..10], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a+b+c == 24]

-- Pattern matching as a function definition. Note that x is just a label, any non-literal value will catch all other inputs
lucky :: (Integral a) => a -> String
lucky 7 = "LUCKY NUMBER SEVEN!"
lucky x = "Sorry, you're out of luck, pal!"

-- First look at Haskell recursion
factorial :: (Integral a) => a -> a  
factorial 0 = 1  
factorial n = n * factorial (n - 1)

-- Pattern matching on tuple input. Note that the pattern IS a catch-all, as the function definition forces an input of two tuples.
addVectors :: (Num a) => (a, a) -> (a, a) -> (a, a)  
addVectors (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

-- Higher order function - takes another function as a parameter
applyTwice :: (a -> a) -> a -> a  
applyTwice f x = f (f x) 