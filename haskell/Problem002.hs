
main = print $ sum_fibonacci max
  where
    max = 4 * 1000 * 1000

sum_fibonacci :: Integer -> Integer
sum_fibonacci max = sum . takeWhile (\x -> x <= max) . filter even $ fibonacci

fibonacci :: [Integer]
fibonacci = 1 : 1 : zipWith (+) fibonacci (tail fibonacci)
