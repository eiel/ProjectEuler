{-
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%202

フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
数列の項の値が400万を超えない範囲で, 偶数値の項の総和を求めよ.
-}

main = print $ sum_fibonacci max
  where
    max = 4 * 1000 * 1000

-- |
-- max より小さい偶数値の項の総和を求める
--
-- >>> sum_fibonacci 90
-- 44
sum_fibonacci :: Integer -> Integer
sum_fibonacci max = sum . takeWhile (\x -> x <= max) . filter even $ fibonacci

fibonacci :: [Integer]
fibonacci = 1 : 1 : zipWith (+) fibonacci (tail fibonacci)
