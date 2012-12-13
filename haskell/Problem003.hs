
main = print solveTarget

solveSample = solve exampleTarget
solveTarget = solve target

target = 600851475143
exampleTarget = 13195
exampleAnswer = 29

isSuccessSample = solveSample == exampleAnswer

solve :: Int -> Int
solve target = solve' target prime
  where
    solve' :: Int -> [Int] -> Int
    solve' 1 (p:ps) = p
    solve' target (p:ps) = if target `mod` p == 0
                           then solve' (target `div` p) (p:ps)
                           else solve' target ps
prime :: [Int]
prime = 2:f [3] [3,5..]
    where f (x:xs) ys = let (ps, qs) = span (< x^2) ys
                        in  ps ++ f (xs ++ ps) [z | z <- qs, mod z x /= 0]
