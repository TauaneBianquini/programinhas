bissexto = ([1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020])
naobissexto = ([1989, 1990, 1991, 1993, 1995, 1997, 1998, 1999, 2001, 2002, 2003, 2005,
2006, 2007, 2009, 2010, 2011, 2013, 2014, 2015, 2017, 2018, 2019])
ano = int(input('Insira um ano para saber se é bissexto, de 1988 a 2020:  '))
if (ano in bissexto):
    print('o ano é bissexto!')
else:
    print('o ano não é bissexto')
