# 1<=n<=d;
# p(k, n)
# p(0, 1) = p(1, 1) = 1
# p(k, 1) = 0 , k>=2
# p(k, n) = p(k, n-1) * ((suma i z zakresu od 1 do n-1 liczba urodzen i) / (suma i z zakresu od 1 do n liczba urodzen i)) ^ k
#           + p(k-1, n-1) * (lu n / (suma i od 1 do n lu i) *
#           * k * ((suma i z zakresu 1 do n-1 lu i) / (suma i od 1 do n lu i)) ^ (k-1)