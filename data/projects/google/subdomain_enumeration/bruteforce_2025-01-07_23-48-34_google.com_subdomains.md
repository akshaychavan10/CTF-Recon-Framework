# FFUF Report

  Command line : `ffuf -w ./wordlist.lst -u http://google.com -H Host: FUZZ.google.com -o data/projects/google/subdomain_enumeration/bruteforce_2025-01-07_23-48-34_google.com_subdomains.md -of md`
  Time: 2025-01-07T23:48:42&#43;01:00

  | FUZZ | URL | Redirectlocation | Position | Status Code | Content Length | Content Words | Content Lines | Content Type | Duration | ResultFile | ScraperData | Ffufhash
  | :- | :-- | :--------------- | :---- | :------- | :---------- | :------------- | :------------ | :--------- | :----------- | :------------ | :-------- |
  | adviser | http://google.com | https://www.google.com/advisor | 5 | 301 | 227 | 9 | 7 | text/html; charset=UTF-8 | 25.515273ms |  |  | 2302d5
  | ai | http://google.com | https://ai.google/?utm_source=ai-google-com&amp;utm_medium=redirect&amp;utm_campaign=ai-google-com-website-redirect | 6 | 302 | 312 | 9 | 7 | text/html; charset=UTF-8 | 29.978573ms |  |  | 2302d6
  | help | http://google.com | https://support.google.com/ | 13 | 301 | 224 | 9 | 7 | text/html; charset=UTF-8 | 31.382321ms |  |  | 2302dd
  | about | http://google.com | https://about.google/ | 1 | 301 | 218 | 9 | 7 | text/html; charset=UTF-8 | 32.300491ms |  |  | 2302d1
  | account | http://google.com | https://myaccount.google.com/ | 10 | 302 | 226 | 9 | 7 | text/html; charset=UTF-8 | 32.428094ms |  |  | 2302da
  | about | http://google.com | https://about.google/ | 14 | 301 | 218 | 9 | 7 | text/html; charset=UTF-8 | 30.902582ms |  |  | 2302de
  | cloud | http://google.com | https://cloud.google.com/ | 4 | 301 | 0 | 1 | 1 | application/binary | 79.580954ms |  |  | 2302d4
  