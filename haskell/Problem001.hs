{-
http://odz.sakura.ne.jp/projecteuler/index.php?cmd=read&page=Problem%201

10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.

同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ.
-}
main = print $ sum_multiple_of_3_or_5 max
  where
    max = 1000

-- |
-- max 未満の 3 か 5の倍数になっている数字の合計を求める
--
-- 問題文より
--
-- >>> sum_multiple_of_3_or_5 10
-- 23
sum_multiple_of_3_or_5 :: Integer -> Integer
sum_multiple_of_3_or_5 max = sum [x| x <- [1..max-1],
                                  x `mod` 3 == 0 || x `mod` 5  == 0]
