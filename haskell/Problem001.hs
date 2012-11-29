
main = print $ sum_multiple_of_3_or_5 max
  where
    max = 1000

sum_multiple_of_3_or_5 :: Integer -> Integer
sum_multiple_of_3_or_5 max = sum [x| x <- [1..max],
                                  x `mod` 3 == 0 || x `mod` 5  == 0]
